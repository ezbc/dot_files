prompt_command () {
    # Capture the output of the "git status" command.
    git_status="$(git status 2> /dev/null)"

    local __git_branch='`git branch 2> /dev/null | grep -e ^* | sed -E  s/^\\\\\*\ \(.+\)$/\(\\\\\1\)\ /`'
    local __prompt_tail="\[\033[35m\]$"
    local __last_color="\[\033[00m\]"

    # Set color based on clean/staged/dirty.
    if [[ ${git_status} =~ "working directory clean" ]]; then
        state="${GREEN}"
    elif [[ ${git_status} =~ "Changes to be committed" ]]; then
        state="${YELLOW}"
    else
        state="${RED}"
    fi

    export PS1="${state}$__git_branch$__prompt_tail$__last_color "
}

# Tell bash to execute this function just before displaying its prompt.
PROMPT_COMMAND=prompt_command

