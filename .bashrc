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
shopt -s globstar

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

alias ls='ls --color=auto'

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
eval "`dircolors -b $DIR_COLORS`"

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
prompt_command () {
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
    if [[ ${git_status} =~ "working directory clean" ]]; then
        state="${GREEN}"
    elif [[ ${git_status} =~ "Changes to be committed" ]]; then
        state="${YELLOW}"
    else
        state="${RED}"
    fi

    export PS1="\n\[$YELLOW\] <\#> \[$LIGHTGREEN\]$PWD\n      \[$LIGHTRED\]\d \t \[$LIGHTPURPLE\]\u\[$NC\]@\[$LIGHTCYAN\]\h\[$NC\] ${state}$__git_branch$__prompt_tail$__last_color\n $ERRPROMPT"
}

# Tell bash to execute this function just before displaying its prompt.
PROMPT_COMMAND=prompt_command

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if [ -f /etc/bash_completion ] && ! shopt -oq posix; then
    . /etc/bash_completion
fi

# ========================== Set bashrc for elijah ============================
if [ $USER == elijah ]; then
    # Defines path to CASA start-up
    PATH='/home/elijah/applications/casapy-40.0.22208-001':$PATH
    gip_root=/home/elijah/applications/gipsy/;export gip_root

    # Read in astro library for gdl
    export GDL_STARTUP=~/.gdl_startup
    export thunderbird=/usr/local/thunderbird
    export vnc=/usr/local/bin/.VNC-Viewer-5.0.5-Linux-x86
    export PATH=$PATH:/usr/local/bin/casa
    PATH='/home/elijah/applications/miriad/bin/linux/miriad':$PATH
    export PATH=$PATH:/usr/local/bin/miriad
    source /usr/local/karma/.karmarc
    export PYTHONPATH=$PYTHONPATH:/home/elijah/python/myModules/

    # Set up aliases
    alias eclipse='/usr/bin/eclipse'
    #alias eclipse='/home/elijah/applications/eclipse/eclipse'
    alias fixinternet='please rm -rf /etc/resolv.conf'
    alias uw='ssh -XY ezbc@uwast.astro.wisc.edu'
    alias screenshot='gnome-screenshot -a'
    cosmos='ezbc@uwast.astro.wisc.edu:'
    uw='ezbc@uwast.astro.wisc.edu:'
    paper5='/home/elijah/Dropbox/research/manuscripts/leop/paper5/'\
        'post_circulation/'
    LOGIN_ARCH=linux
fi

# ========================== Set bashrc for ezbc ============================
if [ $USER == ezbc ]; then
    # IDL
    export IDL_STARTUP=~/.idlstartup
    export IDL_PATH=$IDL_PATH:+/usr/users/ezbc/idl/
    export IDL_PATH=$IDL_PATH:+/usr/local/rsi/idl/idl82/lib/

    # KARMA, Miriad, GIPSY, and CASA
    alias miriad='tcsh | miriad'
    
    # Python
    #export PYTHONPATH=$PYTHONPATH:/usr/users/ezbc/python/myModules
    export PYTHONPATH=$PYTHONPATH:/usr/users/ezbc/research/python_modules
    export PYTHONPATH=$PYTHONPATH:/usr/users/ezbc/research/python_modules/miriad
    export PATH=/usr/users/ezbc/python:$PATH # anaconda

    # Aliases
    alias taurus='cd /d/bip3/ezbc/taurus'
    alias perseus='cd /d/bip3/ezbc/perseus'
    alias please='sudo'
    alias bip='ssh -XY bip'
    alias miriad='tcsh -c miriad'
    alias casa='tcsh -c casa'
    #alias 'casanologger'='tcsh -c casa --nologger'
    alias kvis='tcsh -c kvis'
    alias kpvslice='tcsh -c kpvslice'
    alias gipsy='tcsh -c gipsy'
    alias sl='ls --color=auto'
    alias clean='rm -rf #* .*.swp .*.swn .*.swo'
    alias mac='ssh -XY research@141.140.86.26'
    alias screenshot='gnome-screenshot -a'
    alias mendeley='/usr/users/ezbc/apps/'\
        'mendeleydesktop-1.10.1-linux-x86_64/bin/mendeleydesktop'
    alias ipython='/usr/users/ezbc/.local/bin/ipython'
    alias screen='~/apps/screen/bin/screen'
    alias sysmon='gnome-system-monitor'
    alias view='eog'
    alias xflux='/usr/users/ezbc/apps/xflux -z 53703'
    alias dropbox='/usr/users/ezbc/apps/dropbox.py start -i'

    #/usr/users/ezbc/apps/dropbox.py autostart y'
    # Deine user variables 
    downloads='/d/bip3/ezbc/Downloads/'
    mac='research@141.140.86.26:'
    elijah='elijah@144.92.179.225:'
    home='elijah@192.168.1.124:'
    cosmos='/d/cosmos/ezbc/'
    classes='/d/cosmos/ezbc/classes/'
    bip3='/d/bip3/ezbc/'

    # Go to home directory
    cd ~
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
   
if [ -f "${SSH_ENV}" ]; then
     . "${SSH_ENV}" > /dev/null
     ps -ef | grep ${SSH_AGENT_PID} | grep ssh-agent$ > /dev/null || {
        start_agent;
    }
else
    start_agent;
fi

