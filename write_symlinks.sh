
# Get the location for the dot_files repo
if [ $HOSTNAME == localhost.localdomain ] || [ $HOSTNAME == latitude-laptop ] ; then
    export DOTLOC=/home/ezbc/dot_files
fi
if [ $HOSTNAME == cosmos ] || [ $HOSTNAME == bip ] || [ $HOSTNAME == leffe ] || [ $HOSTNAME == uwast ]; then
    export DOTLOC=/d/cosmos/ezbc/dot_files
fi

ln -s $DOTLOC/.new_vim ~/.new_vim
ln -s $DOTLOC/.vimrc ~/.vimrc
ln -s $DOTLOC/.bashrc ~/.bashrc
ln -s $DOTLOC/.tcshrc ~/.tcshrc

