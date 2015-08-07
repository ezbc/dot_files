
setlocal spell spelllang=en_us   " Allows for spellchecking

" mappings
"imap jk <Esc>l
"vmap jk <Esc>
"imap kj <Esc>l
"vmap kj <Esc>
"imap kj <Esc>l

imap <A-a> <Esc>
vmap <A-a> <Esc>

" Tab switching
map <S-space> :tabn<Enter>
map <C-space> :tabp<Enter>

" Command mode autocomplete
set wildmode=longest:full,list:full

" reformat paragraph
nmap <A-r> gwap
imap <A-r> <Esc>gwapa
imap <A-v> <Esc>va
map <A-C-s> <Esc>:w<Enter>
vmap <A-C-s> <Esc>:w<Enter>
nmap <A-C-s> <Esc>:w<Enter>
imap <A-C-s> <Esc>:w<Enter>

" Indenting and wrapping
set textwidth=80
set whichwrap+=<,>,h,l,[,] " allows for cursor wrapping
set wrap            " allow word wrapping
set linebreak       " 
set nolist          " list disables linebreak
set tabstop=4		" use # of chars to display a <TAB> 
set shiftwidth=4	" insert # of chars in autoindent
set softtabstop=4	" insert # of chars when pressing <TAB>
set smarttab		" insert tabs on the start of a line according to 
                        " context
set expandtab 		" will convert tabs to spaces
set shiftwidth=4 	" will affect block indentation with >> and <<
set softtabstop=4 	" sets the length of soft tab in spaces
"set copyindent		" copy the previous indentation on autoindenting
"set smartindent	" smart indentation for C-like language
"set cindent		" smart indentation especially for C language
"set autoindent 		" will keep indentation level from previous line
set nosmartindent

" Clipboard options
set clipboard=unnamed	" yank to the system register (*) by default
"set clipboard=unnamedplus  " yank to the X11 system register (+) by default, 
                        " works only if '+xterm_clipboard' shows up in 
                        " 'vim --version'

" Searching and completion
set showmatch		" Cursor shows matching ) and }
set showmode		" Show current mode
set wildchar=<TAB>	" start wild expansion (auto-completioin of filename) 
                        " in the command line using <TAB>
set wildmenu		" wild char completion menu
set hlsearch		" search highlighting
set incsearch		" incremental search

set autoread		" auto read when file is changed from outside

" Color column
"set colorcolumn=+1        " highlight column after 'textwidth'
"set colorcolumn=+1,+2,+3  " highlight three columns after 'textwidth'
"highlight ColorColumn ctermbg=lightgrey guibg=lightgrey
"set colorcolumn=80
"set numberwidth=3
"set cpoptions+=n

" aesthetics
set number              " shows line numbers

" ----------------- gvim ----------------------------
if has("gui_running")
    set guioptions-=m
    set guioptions-=T
    set guioptions-=r
    set guioptions-=L
    set guifont=Monospace\ 9
endif

" folding
autocmd FileType c,cpp set foldmethod=syntax
autocmd FileType c,cpp set foldnestmax=2

" copy and paste commands
vmap <C-c> "+yi
vmap <C-x> "+c
vmap <C-v> c<ESC>"+p
imap <C-v> <ESC>"+pa
vmap n i

filetype on			" Enable filetype detection
"filetype indent on	" Enable filetype-specific indenting
filetype plugin on	" Enable filetype-specific plugins

" ----------------------------------------------------------------------------
" plug-in settings
" ----------------------------------------------------------------------------

" -------------------- vim-latex --------------------
let g:Tex_DefaultTargetFormat = 'pdf'
let g:Tex_ViewRule_pdf = 'evince'
let g:Tex_MultipleCompileFormats = 'pdf'
" OPTIONAL: Starting with Vim 7, the filetype of empty .tex files defaults to
" 'plaintex' instead of 'tex', which results in vim-latex not being loaded.
" The following changes the default filetype back to 'tex':
let g:tex_flavor='latex'
" The following toggles syntastic
let g:syntastic_mode_map = { 'mode': 'passive', 'active_filetypes': ['py'],'passive_filetypes': [] }
nnoremap <C-w>E :SyntasticCheck<CR> :SyntasticToggleMode<CR>


" ----------------------------------------------------------------------------
" Snippets
" ----------------------------------------------------------------------------

" Track the engine.
"Plugin 'SirVer/ultisnips'

" Snippets are separated from the engine. Add this if you want them:
"Plugin 'honza/vim-snippets'

" Trigger configuration. Do not use <tab> if you use https://github.com/Valloric/YouCompleteMe.
"let g:UltiSnipsExpandTrigger="<tab>"
"let g:UltiSnipsJumpForwardTrigger="<c-b>"
"let g:UltiSnipsJumpBackwardTrigger="<c-z>"

" If you want :UltiSnipsEdit to split your window.
"let g:UltiSnipsEditSplit="vertical"




