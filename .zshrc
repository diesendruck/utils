autoload -Uz promptinit
promptinit
prompt adam1

setopt histignorealldups sharehistory

bindkey -e

bindkey "[D" backward-word
bindkey "[C" forward-word

# Get Oh My Zsh
# sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# RC aliases.
alias zshrc="source ~/.zshrc"
alias zshrc="vi ~/.zshrc"
alias vimrc="vi ~/.vimrc"
alias ohmyzsh="vi ~/.oh-my-zsh"

# Git aliases.
alias gb="git branch -avv"
alias gs="git status"
alias gc="git checkout"
alias isgit="git rev-parse --is-inside-work-tree"

# Linting aliases.
alias pep="autopep8 -da"
alias dopep="autopep8 -ia"
alias flake="flake8"

# Tmux aliases.
alias tmn="tmux new -s "
alias tma="tmux a -t "
alias tmk="tmux kill-session -t "
alias tml="tmux ls"

# Navigation aliases.
alias ll="ls -la"
alias ..="cd .."
#alias ls="ls -l --color=auto -F"
#alias ll="ls -l --color=auto -F"
#PS1='\w\$ '

# Misc aliases.
alias tree="find . -print | sed -e 's;[^/]*/;|____;g;s;____|; |;g'"
alias subdircounts='find . -maxdepth 1 -mindepth 1 -type d -exec sh -c '\''echo "{} : $(find "{}" -type f | wc -l)" file\(s\)'\'' \;'
alias sortbysize='sudo du -x -h . | sort -h | tail -40'
# Replace text recursively
# grep -rli 'old-word' * | xargs -I@ sed -i '' 's/old-word/new-word/g' @


export VIRTUAL_ENV_DISABLE_PROMPT=


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
