# Document to collect useful, custom-written functions.
# Author: Maurice Diesendruck
# Updated: 2015-09-20

import numpy as np

from scipy.spatial.distance import pdist, cdist


def check_symmetry(q): return("Symmetry: ", (q.transpose() == q).all())

def ising_likelihood(z, theta):
    """Computes Ising likelihood given z's and theta matrix.
    
    Note: Likelihood is up to proportionality, and does not compute the
        normalization factor.
        
    Args:
        z: Vector of node assignments.
        theta: Agreement parameter matrix.
    
    Returns:
        p: Probability of z configuration, given theta.
    """
    terms = [[theta[i, j]*z[i]*z[j] for j in range(n)] for i in range(n)]
    p = np.exp(np.sum(terms))
    return p

def sample_adj_matrix(n, p):
    """Builds random adjacency matrix.

    Creates nxn adjacency matrix (1s and 0s) representing edges between nodes.
    Each edge is sampled as an independent Bernoulli random variable with
    probability p.

    Args:
        n: Number of nodes, and size of matrix adjacency matrix.
        p: Bernoulli probabiity for each edge.

    Returns:
        adj: Adjacency matrix.
    """
    adj = np.asarray([[rbern(0.5) for j in range(n)] for i in range(n)])
    adj = sym_matrix(adj)
    np.fill_diagonal(adj, 0)
    return adj

def sample_ising(theta, adj):
    """Given a matrix of agreement parameters, samples binary ising vector.
    
    Samples vector of 1's and -1's from a Gibbs sampled Ising Distribution.
    
    Args:
        theta: Agreement parameter matrix; one agreement coefficient for each
            pair of nodes.
        adj: Adjacency matrix of pairwise edge connections (binary).
    
    Returns:
        z_sample: Vector of n values, each either 1 or -1. 
    """
    # Set up parameters and variable storage.
    n = len(theta)  # Number of nodes in graph.
    num_trials = 500  # Number of times to run the Gibbs sampler.
    burn_in = 100  # Number of Gibbs samples to discard; must be < num_trials.
    z_chain = np.zeros([num_trials, n])  # Storage for Gibbs samples, by row.
    
    # Initialize and store first configuration of z's.
    z0 = np.random.choice([-1, 1], n)  # Initialize z's.
    z_chain[0,:] = z0  # Store initial values as first row of z_chain.
    
    # Run Gibbs.
    for t in range(1, num_trials):
        z = z_chain[t-1,:]
        for i in range(n):
            # Sample each z from its full Ising model conditional.
            # pi(z_i|z_not_i) = (1/C)*exp(sum(theta*z_i*z_j)), for j's with
            #     edges to i. 
            # Use adjacency matrix as indicator to pick j's.
            # Evaluate for z_i=-1 and z_i=1, normalize, then sample.
            summation_terms_neg1 = [-adj[i, j]*theta[i, j]*z[j]
                if j>i else 0 for j in range(n)]
            summation_terms_pos1 = [+adj[i, j]*theta[i, j]*z[j]
                if j>i else 0 for j in range(n)]
            pn = unnorm_prob_neg1 = np.exp(sum(summation_terms_neg1))
            pp = unnorm_prob_pos1 = np.exp(sum(summation_terms_pos1))
            # Normalize probabilities.
            pr_neg1 = pn/(pn+pp)
            pr_pos1 = pp/(pn+pp)
            # Sample z_i
            z_i_value = np.random.choice([-1, 1], p=[pr_neg1, pr_pos1])
            # Store z_i value in z_chain.
            z_chain[t, i] = z_i_value

    # Sample a z from the z_chain.
    sample_index = np.random.randint(burn_in, len(z_chain))
    z_sample = z_chain[sample_index,:]
    return z_sample

def sym_matrix(matrix, part="upper"):
    """Returns a symmetric matrix, from a square matrix and a triangle flag.
    
    Requires: import numpy as np
    
    Supply a square matrix and a flag like "upper" or "lower", and copy the
    chosen matrix part, symmetrically, to the other part. Diagonals are left
    alone. For example:
    matrix <- [[8, 1, 2],
               [0, 8, 4],
               [0, 0, 8]]
    sym_matrix(matrix, "upper") -> [[8, 1, 2],
                                    [1, 8, 4],
                                    [2, 4, 8]]
    
    Args:
        matrix: Square matrix.
        part: String indicating "upper" or "lower".
    
    Returns:
        m: Symmetric matrix, with either upper or lower copied across the
            diagonal.
    """
    n = matrix.shape[0]  # Get number of rows.
    # Get upper triangular indices, and swap coordinates for the lower indices.
    upper_indices = np.triu_indices(n, k=1)
    lower_indices = upper_indices[1], upper_indices[0]
    m = np.copy(matrix)
    # Perform the copy across the diagonal.
    if part=="upper":
        m[lower_indices] = m[upper_indices]
    elif part=="lower":
        m[upper_indices] = m[lower_indices]
    else:
        print("Give a good 'part' definition, e.g. 'upper' or 'lower'.")
    
    return m

def rbern(p): 
    r = np.random.binomial(1, p)
    return r

def energy_distance(x, y, use_tf=False, method='linear'):
    """Distances are euclidean.
    See: https://github.com/syrte/ndtest/blob/master/ndtest.py
    """
    # TODO: Do tf version.
    if use_tf == True:
        sys.exit('TensorFlow version not complete.')

    dx, dy, dxy = pdist(x), pdist(y), cdist(x, y)
    n, m = len(x), len(y)
    if method == 'log':
        dx, dy, dxy = np.log(dx), np.log(dy), np.log(dxy)
    elif method == 'gaussian':
        raise NotImplementedError
    elif method == 'linear':
        pass
    else:
        raise ValueError

    # Energy is 2 * E[d(x, y)] - E[d(x, x) - E[d(y, y)].
    # Why the 2nd and 3rd factors of 2? dx and dy are computed with scipy's pdist,
    # which only returns upper triangular values of pairwise distance matrix.
    # Full computation of dx computes the full matrix, i.e. n**2 values, so the 
    # upper triangle must be doubled.
    z = 2.0 * dxy.sum() / (n * m) - 2.0 * dx.sum() / n**2 - 2.0 * dy.sum() / m**2
    return z
