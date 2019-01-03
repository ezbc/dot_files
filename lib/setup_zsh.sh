#!/bin/bash

apt install zsh wget git

# instal oh my zsh
wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh

chsh -s $(which zsh) $(whoami)

