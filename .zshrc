autoload -Uz promptinit
promptinit
prompt adam1

setopt histignorealldups sharehistory

bindkey -e

bindkey "[D" backward-word
bindkey "[C" forward-word


alias zshrc="source ~/.zshrc"
alias tf1="source ~/tensorflow-1.0.0/bin/activate; echo 'Using tensorflow 1.0.0 virtualenv for Python...'"
alias dcgan="cd ~/Google\ Drive/0_GAN/gan/dcgan/DCGAN-tensorflow"
alias tmn="tmux new -s "
alias tma="tmux a -t "
alias tmk="tmux kill-session -t "
alias tml="tmux ls"

# Other
alias ll="ls -l"
alias ..="cd .."
#alias ls="ls -l --color=auto -F"
#alias ll="ls -l --color=auto -F"
#PS1='\w\$ '

alias zshrc="vi ~/.zshrc"
alias vimrc="vi ~/.vimrc"
alias ohmyzsh="vi ~/.oh-my-zsh"
export VIRTUAL_ENV_DISABLE_PROMPT=

# Git aliases.
alias gb="git branch -avv"
alias gs="git status"
alias gc="git checkout"

alias tree="find . -print | sed -e 's;[^/]*/;|____;g;s;____|; |;g'"




# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=100000
SAVEHIST=100000
unsetopt beep
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/Users/mauricediesendruck/.zshrc'

autoload -Uz compinit
compinit

autoload -Uz up-line-or-beginning-search down-line-or-beginning-search
zle -N up-line-or-beginning-search
zle -N down-line-or-beginning-search

[[ -n "${key[Up]}"   ]] && bindkey "${key[Up]}"   up-line-or-beginning-search
[[ -n "${key[Down]}" ]] && bindkey "${key[Down]}" down-line-or-beginning-search
