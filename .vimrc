if $HOSTNAME == "latitude-laptop"
  set runtimepath+=~/.new_vim
  
  source ~/.new_vim/vimrcs/basic.vim
  source ~/.new_vim/vimrcs/filetypes.vim
  source ~/.new_vim/vimrcs/plugins_config.vim
  source ~/.new_vim/vimrcs/extended.vim
  
  "try
  source ~/.new_vim/vimrcs/my_configs.vim
  "catch
  "endtry
else
  "set runtimepath=/d/cosmos/ezbc/opt/vim74/runtime
  "set runtimepath=~/.new_vim/vim74_runtime
  "set runtimepath=~/.new_vim/current
  "set runtimepath+=~/.new_vim
  "set runtimepath=~/.new_vim
  "set runtimepath+=~/.new_vim/runtime
  "
  set runtimepath=~/.new_vim/vim74_runtime
  set runtimepath+=~/.new_vim/
  
  source ~/.new_vim/vimrcs/basic.vim
  source ~/.new_vim/vimrcs/filetypes.vim
  source ~/.new_vim/vimrcs/plugins_config.vim
  source ~/.new_vim/vimrcs/extended.vim
  
  "try
  source ~/.new_vim/vimrcs/my_configs.vim
  "catch
  "endtry
endif

