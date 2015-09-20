# Document to collect useful, custom-written functions.

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

def check_symmetry(q): return("Symmetry: ", (q.transpose() == q).all())

def rbern(p): 
    r = np.random.binomial(1, p)
    return r

