
# Get the location for the dot_files repo
if [ $HOSTNAME == localhost.localdomain ] || [ $HOSTNAME == laptop ] ; then
    export DOTLOC=/home/ezbc/dot_files
fi
if [ $HOSTNAME == cosmos ] || [ $HOSTNAME == bip ] || [ $HOSTNAME == leffe ] || [ $HOSTNAME == uwast ]; then
    export DOTLOC=/d/cosmos/ezbc/dot_files
fi

ln -s $DOTLOC/.new_vim ~/.new_vim
ln -s $DOTLOC/.vimrc ~/.vimrc
ln -s $DOTLOC/.bashrc ~/.bashrc
ln -s $DOTLOC/.bash_profile ~/.bash_profile
ln -s $DOTLOC/.tcshrc ~/.tcshrc
ln -s $DOTLOC/matplotlibrc $HOME/.config/matplotlib/matplotlibrc
ln -s $DOTLOC/matplotlibrc $XDG_CONFIG_HOME/matplotlib/matplotlibrc
ln -s $DOTLOC/matplotlibrc $HOME/.matplotlib/matplotlibrc
ln -s $DOTLOC/matplotlibrc /etc/matplotlibrc
ln -s $DOTLOC/matplotlibrc /usr/lib64/python2.7/site-packages/matplotlib/mpl-data/matplotlibrc

