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
    #git_status="$(git status 2> /dev/null)"

    # Set color based on clean/staged/dirty.
    #if [[ ${git_status} =~ "working directory clean" ]]; then
    #    state="${GREEN}"
    #elif [[ ${git_status} =~ "Changes to be committed" ]]; then
    #    state="${YELLOW}"
    #else
    #    state="${RED}"
    #fi

    #export PS1="\n\[$YELLOW\] <\#> \[$LIGHTGREEN\]$PWD\n      \[$LIGHTRED\]\d \t \[$LIGHTPURPLE\]\u\[$NC\]@\[$LIGHTCYAN\]\h\[$NC\] ${state}$__git_branch$__prompt_tail$__last_color\n $ERRPROMPT"
    export PS1="\n\[$YELLOW\] <\#> \[$LIGHTGREEN\]$PWD\n      \[$LIGHTRED\]\d \t \[$LIGHTPURPLE\]\u\[$NC\]@\[$LIGHTCYAN\]\h\[$NC\] $__git_branch$__prompt_tail$__last_color\n $ERRPROMPT"
}

# Tell bash to execute this function just before displaying its prompt.
PROMPT_COMMAND=prompt_command

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

# ========================== Set bashrc for elijah ============================
if [ $HOSTNAME == latitude ]; then
    PATH=/usr/bin/:/bin/

    # Read in astro library for gdl
    export GDL_STARTUP=~/.gdl_startup
    export thunderbird=/usr/local/thunderbird
    export vnc=/usr/local/bin/.VNC-Viewer-5.0.5-Linux-x86
    export PATH=$PATH:/usr/local/bin/casa
    export PATH=$PATH:'/home/elijah/applications/miriad/bin/linux/miriad'
    export PATH=$PATH:/usr/local/bin/miriad
    export PATH=$PATH:/usr/local/bin
    export PATH=$PATH:/sbin/
    export PATH=$PATH:/usr/games/
    export PATH=$PATH:/home/ezbc/opt/hdf5-1.8.13/hdf5/bin
    export PYTHONPATH=$PYTHONPATH:/home/ezbc/research/python_modules/
    export PYTHONPATH=$PYTHONPATH:/home/ezbc/brewing/modules/
    export GAUSSPY=/home/ezbc/classes/machine_learning/project/gausspy_module/gausspy/
    export PYTHONPATH=$PYTHONPATH:/home/ezbc/classes/machine_learning/project/gausspy_module/gausspy
    export PYTHONPATH=$PYTHONPATH:/home/ezbc/python/galactus


    # Parellel programming
    export MADSDK_ROOT=~/opt/madsdk

    # KARMA package
    source /usr/local/karma/.karmarc

    # Set up for Star-link
    #export STARLINK_DIR="/home/ezbc/opt/star-hawaiki"
    #source $STARLINK_DIR/etc/profile

    # Set up for cloudy
    alias cloudy='/home/ezbc/opt/c13.03/source/sys_gcc/cloudy.exe'

    # Kerbel Space program
    alias kerbal='cd /home/ezbc/opt/KSP_linux/ && /home/ezbc/opt/KSP_linux/KSP.x86_64'

    # Switch iraf login command
    alias iraf='cl'
    
    # TOPCAT
    alias topcat='java -jar /home/ezbc/opt/topcat-lite.jar'

    # Bbarolo
    alias bbarolo='/home/ezbc/opt/Bbarolo_Linux_x64/Bbarolo'
    
    # Set up aliases
    alias eclipse='/usr/bin/eclipse'
    alias fixinternet='sudo rm -rf /etc/resolv.conf && sudo ln -s /run/resolvconf/resolv.conf /etc/resolv.conf'
                      # && ' \
                      #'sudo service network-manager stop && '\
                      #'sudo ifconfig eth0 down && '\
                      #'sudo ifconfig eth0 up && '\
                      #'sudo service network-manager start'
    alias sshbip='ssh -XY ezbc@bip.astro.wisc.edu'
    alias screenshot='gnome-screenshot -a'
    alias sysmon='gnome-system-monitor'
    alias testinternet='/home/ezbc/opt/speedtest-cli'

    cosmos='ezbc@cosmos.astro.wisc.edu:'
    bip='ezbc@bip.astro.wisc.edu:'
    LOGIN_ARCH=linux
    

fi

# ========================== Set bashrc for ezbc ============================
if [ $HOSTNAME == cosmos ] || [ $HOSTNAME == bip ] || [ $HOSTNAME == leffe ] || [ $HOSTNAME == uwast ]; then
    # IDL
    export IDL_STARTUP=~/.idlstartup
    export IDL_PATH=$IDL_PATH:+/usr/users/ezbc/idl/
    export IDL_PATH=$IDL_PATH:+/usr/local/rsi/idl/idl82/lib/

    # KARMA, Miriad, GIPSY, and CASA
    alias miriad='tcsh | miriad'
    
    # Python
    export PYTHONPATH=$PYTHONPATH:/usr/users/ezbc/python/
    export PYTHONPATH=$PYTHONPATH:/usr/users/ezbc/research/python_modules
    export PYTHONPATH=$PYTHONPATH:/usr/users/ezbc/research/python_modules/miriad
    export \
        PYTHONPATH=$PYTHONPATH:/usr/users/ezbc/research/python_modules/planckpy
    #export PYTHONPATH=$PYTHONPATH:/.local/lib/python2.7/site-packages/scipy
    #export PYTHONPATH=$PYTHONPATH:/.local/lib/python2.7/site-packages/
    export PATH=/usr/users/ezbc/python:$PATH # anaconda
    
    # Texlive
	export PATH=/usr/users/ezbc/.local/lib/texlive/bin/x86_64-linux:$PATH

    # Google-chrome
    export PATH=/usr/users/ezbc/opt/usr/bin:$PATH

    # Local bin
    export PATH=/usr/users/ezbc/.local/bin:$PATH

    # Nodejs
    export PATH=/usr/users/ezbc/opt/node-v0.12.0/~/.local/lib/bin:$PATH

    # Ruby
    export PATH=/usr/users/ezbc/.gem/ruby/2.0.0/bin:$PATH

    # Aliases
    alias taurus='cd /d/bip3/ezbc/taurus'
    alias perseus='cd /d/bip3/ezbc/perseus'
    alias please='sudo'
    alias engels='cd /d/engels2/ezbc/'
    alias bip='ssh -XY bip'
    alias latitude='ezbc@144.92.179.191'
    alias sshlatitude='ssh -XY ezbc@144.92.179.191'
    alias miriad='tcsh -c miriad'
    alias kvis='tcsh -c kvis'
    alias kpvslice='tcsh -c kpvslice'
    alias gipsy='tcsh -c gipsy'
    alias sl='ls --color=auto'
    alias clean='rm -rf #* .*.swp .*.swn .*.swo'
    alias mac='ssh -XY research@141.140.86.26'
    alias screenshot='gnome-screenshot -a'
    alias ipython='/usr/users/ezbc/.local/bin/ipython'
    alias screen='~/apps/screen/bin/screen'
    alias sysmon='gnome-system-monitor'
    alias view='eog'
    alias xflux='/usr/users/ezbc/apps/xflux -z 53703'
    alias dropbox='/usr/users/ezbc/apps/dropbox.py start -i'
    alias mendeley='/usr/users/ezbc/opt/mendeleydesktop-1.12.4-linux-x86_64/bin/mendeleydesktop'
    alias bundle='bundle2.0'

    #/usr/users/ezbc/apps/dropbox.py autostart y'
    # Deine user variables 
    downloads='/d/bip3/ezbc/Downloads/'
    mac='research@141.140.86.26:'
    elijah='elijah@144.92.179.225:'
    home='elijah@192.168.1.124:'
    cosmos='/d/cosmos/ezbc/'
    classes='/d/cosmos/ezbc/classes/'
    bip3='/d/bip3/ezbc/'
    engels='/d/engels2/ezbc/'

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
   
#if [ -f "${SSH_ENV}" ]; then
#     . "${SSH_ENV}" > /dev/null
#     ps -ef | grep ${SSH_AGENT_PID} | grep ssh-agent$ > /dev/null || {
#        start_agent;
#    }
#else
#    start_agent;
#fi

alias init_ssh='start_agent'

# Add iraf setup commands
#if [ -e /home/ezbc/.iraf/setup.sh ]; then
#    source /home/ezbc/.iraf/setup.sh
#fi

export PATH="$PATH:$HOME/.rvm/bin" # Add RVM to PATH for scripting
