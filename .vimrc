if $HOSTNAME == "latitude-laptop"
  set runtimepath+=~/.vim_runtime
  
  source ~/.vim_runtime/vimrcs/basic.vim
  source ~/.vim_runtime/vimrcs/filetypes.vim
  source ~/.vim_runtime/vimrcs/plugins_config.vim
  source ~/.vim_runtime/vimrcs/extended.vim
  
  "try
  source ~/.vim_runtime/my_configs.vim
  "catch
  "endtry
else
  "set runtimepath=/d/cosmos/ezbc/opt/vim74/runtime
  "set runtimepath=/d/cosmos/ezbc/dot_files/.vim_runtime/vim74_runtime
  "set runtimepath=/d/cosmos/ezbc/dot_files/.vim_runtime/current
  "set runtimepath+=/d/cosmos/ezbc/dot_files/.vim_runtime
  "set runtimepath=/d/cosmos/ezbc/dot_files/.vim_runtime
  "set runtimepath+=/d/cosmos/ezbc/dot_files/.vim_runtime/runtime
  "
  set runtimepath=/d/cosmos/ezbc/dot_files/.new_vim/vim74_runtime
  
  source /d/cosmos/ezbc/dot_files/.new_vim/vimrcs/basic.vim
  source /d/cosmos/ezbc/dot_files/.new_vim/vimrcs/filetypes.vim
  source /d/cosmos/ezbc/dot_files/.new_vim/vimrcs/plugins_config.vim
  source /d/cosmos/ezbc/dot_files/.new_vim/vimrcs/extended.vim
  
  "try
  source /d/cosmos/ezbc/dot_files/.new_vim/vimrcs/my_configs.vim
  "catch
  "endtry
endif

