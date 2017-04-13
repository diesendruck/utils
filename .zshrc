autoload -Uz promptinit
promptinit
prompt adam1

setopt histignorealldups sharehistory

bindkey -e

bindkey "[D" backward-word
bindkey "[C" forward-word

alias ll="ls -l"
alias ..="cd .."
alias zshrc="source ~/.zshrc"
alias tf1="source ~/tensorflow-1.0.0/bin/activate; echo 'Using tensorflow 1.0.0 virtualenv for Python...'"
alias dcgan="cd ~/Google\ Drive/0_GAN/gan/dcgan/DCGAN-tensorflow"
alias tmn="tmux new -s "
alias tma="tmux a -t "
alias tmk="tmux kill-session -t "
alias tml="tmux ls"

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
