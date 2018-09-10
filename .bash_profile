# .bash_profile

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
	. ~/.bashrc
fi

# User specific environment and startup programs

PATH=$PATH:$HOME/.local/bin:$HOME/bin

export PATH

# Git autocomplete
if [ -f ~/.git-completion.bash ]; then
  . ~/.git-completion.bash
fi


# The next line updates PATH for the Google Cloud SDK.
if [ -f '/Users/ezbc/Downloads/google-cloud-sdk/path.bash.inc' ]; then source '/Users/ezbc/Downloads/google-cloud-sdk/path.bash.inc'; fi

# The next line enables shell command completion for gcloud.
if [ -f '/Users/ezbc/Downloads/google-cloud-sdk/completion.bash.inc' ]; then source '/Users/ezbc/Downloads/google-cloud-sdk/completion.bash.inc'; fi
