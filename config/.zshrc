neofetch
# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# Path to your oh-my-zsh installation.
export ZSH="$HOME/.oh-my-zsh"

ZSH_THEME="powerlevel10k/powerlevel10k"


# Add wisely, as too many plugins slow down shell startup.
plugins=(git zsh-autosuggestions docker docker-compose)

source $ZSH/oh-my-zsh.sh

# You may need to manually set your language environment
export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions

# Compilation flags
export ARCHFLAGS="-arch x86_64"

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/balde/Downloads/AUR/y/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/balde/Downloads/AUR/y/etc/profile.d/conda.sh" ]; then
        . "/home/balde/Downloads/AUR/y/etc/profile.d/conda.sh"
    else
        export PATH="/home/balde/Downloads/AUR/y/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

alias jnb="jupyter notebook"
alias jl="jupyter lab"
alias ca="conda activate"
alias da="conda deactivate"
alias mp='makepkg -si'
alias sv='sudo nvim'
alias v='nvim'
alias pr='paru -S'

alias rm='rm -rf'
alias lsa='ls -al'

# git custom shortcut
alias stat='git status'
alias cl='git clone'
alias push='git push origin'
alias addall='git add .'
alias add='git add'
alias commit='git commit -m'
alias pull='git pull origin'

#Pacman Shortcuts
alias sync="sudo pacman -Syyy"
alias install="sudo pacman -S"
alias update="sudo pacman -Syyu"
alias search="sudo pacman -Ss"
alias search-local="sudo pacman -Qs"
alias pkg-info="sudo pacman -Qi"
alias local-install="sudo pacman -U"
alias clr-cache="sudo pacman -Scc"
alias unlock="sudo rm /var/lib/pacman/db.lck"
alias remove="sudo pacman -R"
alias autoremove="sudo pacman -Rns"
alias orph='sudo pacman -Rns $(pacman -Qtdq)'
alias openz='zathura'


type nvim >/dev/null &&
    alias vi=nvim &&
    alias vim=nvim


alias rc="vim ~/.bashrc && source ~/.bashrc"
alias zc="vim ~/.zshrc && source ~/.zshrc"
alias kt='vim ~/.config/kitty/kitty.conf'
#alias vimrc=' vim ~/.vimro

export EDITOR=nvim

# pandoc
alias pandocpdf='pandoc test.md -t ms -o test.pdf'

alias al='ls | tree'

alias nm="ncmpcpp"


alias wif='~/.local/bin && ./wifimenu &'

alias dotn="~/.config/nvim"
alias dotq="~/.config/qtile"
alias dotc="~/.config"



# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
