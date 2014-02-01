

" --------- Window size settings --------
if has("gui_running")
  " GUI is running or is about to start.
  " Maximize gvim window.
  set lines=40 columns=85
  set numberwidth=4
  "set cpoptions+=n
else
  " This is console Vim.
  if exists("+lines")
    set lines=50
  endif
  if exists("+columns")
    set columns=85
  endif
endif




