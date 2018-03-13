#!/bin/bash
# example:
# $ replace-text.sh ./ s/apple/orange/g

# find and replace strings in files with sed regex
# avoid directories

find $1 -type f -exec sed -i -e "$2" {} \;

