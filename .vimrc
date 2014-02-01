set nocompatible	" not compatible with the old-fashion vi mode
set encoding=utf-8
set backspace=2		" allow backspacing over everything in insert mode
set history=100		" keep 100 lines of command line history
set ruler			" show the cursor position all the time
set autoread		" auto read when file is changed from outside
set hidden			" hide the buffer instead of closing it
set title			" change the terminal title
imap <A-a> <Esc>
vmap <A-a> <Esc>
nmap <A-r> gwap         " reformat paragraph
imap <A-r> <Esc>gwapa
imap <A-v> <Esc>va
imap <C-s> <Esc>:w<Enter>
vmap <C-s> <Esc>:w<Enter>
nmap <C-s> <Esc>:w<Enter>
imap <C-e> <Esc>$a
nmap <C-a> <Esc>^i

set whichwrap+=<,>,h,l,[,] " allows for cursor wrapping
set wrap            " allow word wrapping
set linebreak       " 
set nolist          " list disables linebreak
set tabstop=4		" use # of chars to display a <TAB> 
set shiftwidth=4	" insert # of chars in autoindent
set softtabstop=4	" insert # of chars when pressing <TAB>
set autoindent		" auto indentation
set copyindent		" copy the previous indentation on autoindenting
set smartindent	" smart indentation for C-like language
"set cindent		" smart indentation especially for C language
set smarttab		" insert tabs on the start of a line according to 
                        " context
set incsearch		" incremental search
set ignorecase		" ignore case when searching
set smartcase		" ignore case if search pattern is all 
                        " lowercase,case-sensitive otherwise
set number              " shows line numbers
set expandtab 		" will convert tabs to spaces
set autoindent 		" will keep indentation level from previous line
set shiftwidth=4 	" will affect block indentation with >> and <<
set softtabstop=4 	" sets the length of soft tab in spaces
"set tabstop=8 		" sets the width of tab character
set hlsearch		" search highlighting
"set clipboard=unnamed	" yank to the system register (*) by default
"set clipboard=unnamedplus  " yank to the X11 system register (+) by default, 
                        " works only if '+xterm_clipboard' shows up in 
                        " 'vim --version'
set showmatch		" Cursor shows matching ) and }
set showmode		" Show current mode
set wildchar=<TAB>	" start wild expansion (auto-completioin of filename) 
                        " in the command line using <TAB>
set wildmenu		" wild char completion menu
setlocal spell spelllang=en_us   " Allows for spellchecking


" Color column settings
set colorcolumn=+1        " highlight column after 'textwidth'
set colorcolumn=+1,+2,+3  " highlight three columns after 'textwidth'
highlight ColorColumn ctermbg=lightgrey guibg=lightgrey
set colorcolumn=80
set numberwidth=3
set cpoptions+=n


" folding settings
autocmd FileType python set foldmethod=indent	" use indent for folding (python)
autocmd FileType python set foldnestmax=1	" maximal level of folding
autocmd FileType python set expandtab		" insert spaces instead of <Tab> 
autocmd FileType c,cpp set foldmethod=syntax
autocmd FileType c,cpp set foldnestmax=2

" copy and paste commands
vmap <C-c> "+yi
vmap <C-x> "+c
vmap <C-v> c<ESC>"+p
imap <C-v> <ESC>"+pa

set t_Co=256		" enable 256 colors
colorscheme torte
syntax on			" syntax highlight
"filetype off		" necessary to make ftdetect work on Linux
filetype on			" Enable filetype detection
filetype indent on	" Enable filetype-specific indenting
filetype plugin on	" Enable filetype-specific plugins

" ----------------------------------------------------------------------------
" plug-in settings
" ----------------------------------------------------------------------------

" ------------------ pathogen ----------------------
" Allows for easy plugin installation
" See pathogen vim install.
call pathogen#infect()

let python_highlight_all = 1	" hight all syntax, see 'syntax/python.vim'

" -------------------- vim-latex --------------------
let g:Tex_DefaultTargetFormat = 'pdf'
let g:Tex_ViewRule_pdf = 'evince'
let g:Tex_MultipleCompileFormats = 'pdf'
" OPTIONAL: Starting with Vim 7, the filetype of empty .tex files defaults to
" 'plaintex' instead of 'tex', which results in vim-latex not being loaded.
" The following changes the default filetype back to 'tex':
let g:tex_flavor='latex'

" ----------------- gvim ----------------------------
set guioptions-=m
set guioptions-=T
set guioptions-=r
set guioptions-=L





