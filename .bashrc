# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# If not running interactively, don't do anything
[ -z "$PS1" ] && return

# don't put duplicate lines or lines starting with space in the history.
# See bash(1) for more options
HISTCONTROL=ignoreboth

# append to the history file, don't overwrite it
shopt -s histappend

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=1000
HISTFILESIZE=2000

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# If set, the pattern "**" used in a pathname expansion context will
# match all files and zero or more directories and subdirectories.
#shopt -s globstar/

# make less more friendly for non-text input files, see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "$debian_chroot" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

# Alias definitions in ~/.bash_aliases
if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

chkload () { #gets the current 1m avg CPU load
    local CURRLOAD=`uptime|awk '{print $8}'`
    if [ "$CURRLOAD" > "1" ]; then
        local OUTP="HIGH"
    elif [ "$CURRLOAD" < "1" ]; then
        local OUTP="NORMAL"
    else
        local OUTP="UNKNOWN"
    fi
    echo $CURRLOAD
}


# ==================== Colors ====================
[ -e "$HOME/.dircolors" ] && DIR_COLORS="$HOME/.dircolors"
[ -e "$DIR_COLORS" ] || DIR_COLORS=""
#eval "`dircolors -b $DIR_COLORS`"

# Set colors
BLACK='\e[0;30m'
BLUE='\e[0;34m'
GREEN='\e[0;32m'
CYAN='\e[0;36m'
RED='\e[0;31m'
PURPLE='\e[0;35m'
BROWN='\e[0;33m'
LIGHTGRAY='\e[0;37m'
DARKGRAY='\e[1;30m'
LIGHTBLUE='\e[1;34m'
LIGHTGREEN='\e[1;32m'
LIGHTCYAN='\e[1;36m'
LIGHTRED='\e[1;31m'
LIGHTPURPLE='\e[1;35m'
YELLOW='\e[1;33m'
WHITE='\e[1;37m'
NC='\e[0m'            # No Color
DEFAULT='\[\033[0;39m\]'

# =========================== Prompt ==========================================
prompt_command_work () {
    if [ $? -eq 0 ]; then # set an error string for the prompt, if applicable
        ERRPROMPT="\[$LIGHTGREEN\] ==> $DEFAULT"
    else
        ERRPROMPT="\[$LIGHTRED\] ==> $DEFAULT"
    fi

    local __user_and_host="\[\033[01;32m\]\u@\h"
    local __cur_location="\[\033[01;34m\]\w"
    #local __git_branch='`git branch 2> /dev/null | grep -e ^* | sed -E  s/^\\\\\*\ \(.+\)$/\(\\\\\1\)\ /`'
    local __prompt_tail="\[\033[35m\]$"
    local __last_color="\[\033[00m\]"

    # Capture the output of the "git status" command.
    #git_status="$(git status 2> /dev/null)"

    export PS1="\n\[$YELLOW\] <\#> \[$LIGHTGREEN\]$PWD\n      \[$LIGHTRED\]\d \t \[$LIGHTPURPLE\]\u\[$NC\]@\[$LIGHTCYAN\]\h\[$NC\] $__prompt_tail$__last_color\n $ERRPROMPT"
}

prompt_command_laptop () {
    if [ $? -eq 0 ]; then # set an error string for the prompt, if applicable
        ERRPROMPT="\[$LIGHTGREEN\] ==> $DEFAULT"
    else
        ERRPROMPT="\[$LIGHTRED\] ==> $DEFAULT"
    fi

    local __user_and_host="\[\033[01;32m\]\u@\h"
    local __cur_location="\[\033[01;34m\]\w"
    local __git_branch='`git branch 2> /dev/null | grep -e ^* | sed -E  s/^\\\\\*\ \(.+\)$/\(\\\\\1\)\ /`'
    local __prompt_tail="\[\033[35m\]$"
    local __last_color="\[\033[00m\]"

    # Capture the output of the "git status" command.
    git_status="$(git status 2> /dev/null)"

    # Set color based on clean/staged/dirty.
    if [[ ${git_status} =~ "working tree clean" ]]; then
        state="${GREEN}"
    elif [[ ${git_status} =~ "Changes to be committed" ]]; then
        state="${YELLOW}"
    else
        state="${RED}"
    fi

    export PS1="\n\[$YELLOW\] <\#> \[$LIGHTGREEN\]$PWD\n      \[$LIGHTRED\]\d \t \[$LIGHTPURPLE\]\u\[$NC\]@\[$LIGHTCYAN\]\h\[$NC\] ${state}$__git_branch$__prompt_tail$__last_color\n $ERRPROMPT"
}


# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if [ -f /etc/bash_completion ] && ! shopt -oq posix; then
    . /etc/bash_completion
fi
    
# get big files
bigfiles () { 
    NUM_FILES=10;
    if [ $1 ]; then
        NUM_FILES=$1;
    fi;
    du * | sort -nr | head -n $NUM_FILES
}

# ============================= default bashrc  ================================
if [ "default" == "default" ]; then

    export BASHENV=~/dot_files

    export PATH=$PATH:$BASHENV/bin

    # git auto complete
    source $BASHENV/bin/git-completion.bash

    export SUBLIME_USER_PREFS="~/Library/Application Support/Sublime Text 3/Packages/User"

    # Prompt command
    # Tell bash to execute this function just before displaying its prompt.
    PROMPT_COMMAND=prompt_command_laptop

fi

# ========================== Set bashrc for elijah ============================
if [ $HOSTNAME == localhost.localdomain ] || [ $HOSTNAME == laptop ] ; then
    PATH=/usr/bin/:/bin/

    export HOME=/home/ezbc

    # Read in astro library for gdl
    export vnc=/usr/local/bin/.VNC-Viewer-5.0.5-Linux-x86
    export PATH=$PATH:/usr/local/bin/casa
    export PATH=$PATH:'/home/elijah/applications/miriad/bin/linux/miriad'
    export PATH=$PATH:/usr/local/bin/miriad
    export PATH=$PATH:/usr/local/bin
    export PATH=$PATH:~/bash_scripts/
    export PATH=$PATH:/sbin/
    export PATH=$PATH:/usr/games/
    export PATH=$PATH:/home/ezbc/opt/hdf5-1.8.13/hdf5/bin
    export PATH=$PATH:/home/ezbc/opt/otp_src_18.2.1/bin
    export PYTHONPATH=$PYTHONPATH:/home/ezbc/research/python_modules/
    export PYTHONPATH=$PYTHONPATH:/home/ezbc/brewing/modules/
    export PYTHONPATH=$PYTHONPATH:/home/ezbc/python/galactus

    # git auto complete
    source ./git-completion.bash

    # Matplotlibrc
    export MATPLOTLIBRC=/home/ezbc/.config/matplotlibrc/

    # Kerbel Space program
    alias kerbal='cd /home/ezbc/opt/KSP_linux/ && /home/ezbc/opt/KSP_linux/KSP.x86_64'
    
    # TOPCAT
    #alias topcat='java -jar /home/ezbc/opt/topcat-full.jar'
    alias topcat='/home/ezbc/opt/topcat'

    # PCGen, RPG character generators
    alias pcgen='/home/ezbc/opt/pcgen/pcgen.sh'
    
    # Set up aliases
    alias eclipse='/usr/bin/eclipse'
    alias fixinternet='sudo rm -rf /etc/resolv.conf && sudo ln -s /run/resolvconf/resolv.conf /etc/resolv.conf'
                      # && ' \
                      #'sudo service network-manager stop && '\
                      #'sudo ifconfig eth0 down && '\
                      #'sudo ifconfig eth0 up && '\
                      #'sudo service network-manager start'
    alias screenshot='gnome-screenshot -a'
    alias sysmon='gnome-system-monitor'
    alias setdisplay='kcmshell5 kcm_kscreen &'
    alias gvim='gvim -p'
    alias homedisplay='kquitapp plasmashell && kstart plasmashell && xrandr --auto --output HDMI2 --mode 1920x1080 --above eDP1 --primary'
    alias turnoffhdmi='xrandr --output HDMI2 --off && kquitapp plasmashell && kstart plasmashell'
    alias laptopdisplay=''
    alias gitremovebigfiles='java -jar ~/opt/bfg-1.12.8.jar --strip-blobs-bigger-than'

    # Prompt command
    # Tell bash to execute this function just before displaying its prompt.
    PROMPT_COMMAND=prompt_command_laptop

fi

if [ $HOSTNAME == "mac" ]; then

    # Node Version Manager
    export NVM_DIR=~/.nvm
    source $(brew --prefix nvm)/nvm.sh
fi

if [ $HOSTNAME == "elijah-ThinkPad-T480s" ]; then

    echo ""
    export SUBLIME_SETTINGS="/home/elijah/.config/sublime-text-3/Packages/User"

    # Node Version Manager
    export NVM_DIR=~/.nvm
    source "$NVM_DIR/nvm.sh"
fi

#===============================================================================
# Set up SSH environment
#===============================================================================

SSH_ENV=$HOME/.ssh/environment
   
# start the ssh-agent
function start_agent {
    echo "Initializing new SSH agent..."
    # spawn ssh-agent
    /usr/bin/ssh-agent | sed 's/^echo/#echo/' > "${SSH_ENV}"
    echo succeeded
    chmod 600 "${SSH_ENV}"
    . "${SSH_ENV}" > /dev/null
    /usr/bin/ssh-add
}
alias init_ssh='start_agent'

##########
# PYTHON #
##########
# Setting PATH for Python 3.6
# The original version is saved in .bash_profile.pysave
PATH="/Library/Frameworks/Python.framework/Versions/3.6/bin:${PATH}"
export PATH

# Make python3 the default
alias python='python3'
alias pip='pip3'


# added by travis gem
[ -f /Users/ezbc/.travis/travis.sh ] && source /Users/ezbc/.travis/travis.sh


# The next line updates PATH for the Google Cloud SDK.
if [ -f '/Users/Elijah/Downloads/google-cloud-sdk/path.bash.inc' ]; then source '/Users/Elijah/Downloads/google-cloud-sdk/path.bash.inc'; fi

# The next line enables shell command completion for gcloud.
if [ -f '/Users/Elijah/Downloads/google-cloud-sdk/completion.bash.inc' ]; then source '/Users/Elijah/Downloads/google-cloud-sdk/completion.bash.inc'; fi

export http_proxy=''
export https_proxy=''
export ftp_proxy=''
export socks_proxy=''
# added by Anaconda3 2018.12 installer
# >>> conda init >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$(CONDA_REPORT_ERRORS=false '/home/elijah/Downloads/.local/lib/anaconda3/bin/conda' shell.bash hook 2> /dev/null)"
if [ $? -eq 0 ]; then
    \eval "$__conda_setup"
else
    if [ -f "/home/elijah/Downloads/.local/lib/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/home/elijah/Downloads/.local/lib/anaconda3/etc/profile.d/conda.sh"
        CONDA_CHANGEPS1=false conda activate base
    else
        \export PATH="/home/elijah/Downloads/.local/lib/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda init <<<

[ -f ~/.fzf.bash ] && source ~/.fzf.bash

# added by travis gem
[ -f /home/elijah/.travis/travis.sh ] && source /home/elijah/.travis/travis.sh

export PATH="$HOME/.poetry/bin:/home/elijah/dot_files/bin:$PATH"
export PYENV_ROOT="$HOME/.pyenv"
if command -v pyenv 1>/dev/null 2>&1; then
  eval "$(pyenv init -)"
fi

