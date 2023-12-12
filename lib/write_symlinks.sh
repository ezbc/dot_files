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
#ln -s $DOTFILES/.i3config ~/.config/i3/config
#ln -s $DOTFILES/.i3status ~/.config/i3status/config
#ln -s $DOTFILES/.i3regolith_config ~/.config/regolith/i3/config
#ln -s $DOTFILES/.i3regolith2_config ~/.config/regolith2/i3/config

# bin
FILEPATHS="$DOTFILES/bin/*"
for filepath in $FILEPATHS
do
    filename=$(basename $filepath)
    echo "adding $filename to path"
    ln -s "$filepath" "$HOME/.local/bin/$filename"
done


# profile.d
FILEPATHS="$DOTFILES/profile.d/*"
for filepath in $FILEPATHS
do
    filename=$(basename $filepath)
    echo "adding $filename to path"
    sudo ln -s "$filepath" "/etc/profile.d/$filename"
done

