#!/bin/bash

if [ -z "$DOTFILES" ]
then
    echo "\$DOTFILES must be set"
    exit 1
else
    echo "\$DOTFILES env: $DOTFILES"
fi

# Configs
ln -s $DOTFILES/.new_vim ~/.new_vim
ln -s $DOTFILES/.vimrc ~/.vimrc
ln -s $DOTFILES/.bashrc ~/.bashrc
ln -s $DOTFILES/.hgrc ~/.hgrc
ln -s $DOTFILES/.bash_profile ~/.bash_profile
ln -s $DOTFILES/.zshrc ~/.zshrc
ln -s $DOTFILES/.i3config ~/.config/i3/config

# bin
FILEPATHS="$DOTFILES/bin/*"
for filepath in $FILEPATHS
do
    filename=$(basename $filepath)
    echo "adding $filename to path"
    ln -s "$filepath" "$HOME/.local/bin/$filename"
done

