
" mappings
"imap jk <Esc>l
"vmap jk <Esc>
"imap kj <Esc>l
"vmap kj <Esc>
"imap kj <Esc>l

" prevent tab completion
imap <Tab> <Tab>

" escape to normal mode with Alt+a
imap <A-a> <Esc>
vmap <A-a> <Esc>

" Resync syntax highlighting when fold interferes
map <A-s> :syntax sync fromstart<Enter>

" line switching
":nnoremap <silent> gw "_yiw:s/\(\%#\w\+\)\(\_W\+\)\(\w\+\)/\3\2\1/<CR><c-o><c-l>
":nnoremap <silent> gr "_yiw:s/\(\%#\w\+\)\(\_W\+\)\(\w\+\)/\3\2\1/<CR><c-o>/\w\+\_W\+<CR><c-l>

" Tab switching
map <C-space> :tabn<Enter>
map <S-space> :tabp<Enter>

" Line switching
map <A-k> ddkkp " move down
map <A-j> ddp " move up

"set wildchar=<TAB>	" start wild expansion (auto-completioin of filename) 
                        " in the command line using <TAB>
"set wildmenu		" wild char completion menu
" Command mode autocomplete
if has("wildmenu")
    set wildignore+=*.h,*.mod
    set wildignore+=*.a,*.o
    set wildignore+=*.bmp,*.gif,*.ico,*.jpg,*.png
    set wildignore+=.DS_Store,.git,.hg,.svn
    set wildignore+=*~,*.swp,*.tmp
    set wildignore+=/usr/include/*,/usr/local/*
    set wildmenu
    set wildmode=longest,list
endif

" reformat paragraph
nmap <A-r> gwap
imap <A-r> <Esc>gwapa
imap <A-v> <Esc>va
map <A-C-s> <Esc>:w<Enter>
vmap <A-C-s> <Esc>:w<Enter>
nmap <A-C-s> <Esc>:w<Enter>
imap <A-C-s> <Esc>:w<Enter>

" Indenting and wrapping
set whichwrap+=<,>,h,l,[,] " allows for cursor wrapping
set wrap            " allow word wrapping
set linebreak       " 
set nolist          " list disables linebreak
"set tabstop=4		" use # of chars to display a <TAB> 
"set shiftwidth=4	" insert # of chars in autoindent
"set softtabstop=4	" insert # of chars when pressing <TAB>
"set smarttab		" insert tabs on the start of a line according to context
"set noexpandtab     " will convert tabs to spaces
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


" ----------------------------- aesthetics -----------------------------------
" ------------------------------------------------------------------------------
set number              " shows line numbers

" cursor line
set cursorline
" hi CursorLine cterm=NONE ctermbg=darkred guibg=purple4
hi Cursor guibg=white guifg=black
hi CursorLine guibg=gray20
set number

" Visual mode highlighting
hi Visual guibg=white guifg=black 

" Tab line colors
"hi TabLine guibg=green
hi TabLineSel guibg=white guifg=black
hi TabLineFill guibg=gray10

" -------------------------------- gvim --------------------------------------
" ------------------------------------------------------------------------------
if has("gui_running")
    set guioptions-=m
    set guioptions-=T
    set guioptions-=r
    set guioptions-=L
    set guifont=Monospace\ 9

    " Window size
    set textwidth=80
    set lines=50

    au BufReadPre,TabEnter * let &numberwidth = float2nr(log10(line("$"))) + 3
          \| let &columns = &numberwidth + 82
    au BufRead * let &numberwidth = float2nr(log10(line("$"))) + 3
          \| let &columns = &numberwidth + 82

    "autocmd BufWinEnter * call matchadd('ErrorMsg', '\%>'.&l:textwidth.'v.\+', -1)

endif


" folding
autocmd FileType c,cpp set foldmethod=syntax
autocmd FileType c,cpp set foldnestmax=2

" Tab definitions for different filetypes
autocmd BufRead,BufNewFile *.py set tabstop=4 shiftwidth=4 softtabstop=4 smarttab expandtab 		
autocmd BufRead,BufNewFile *.html,*.md,*.tex,*.scss,*.css set tabstop=2 shiftwidth=2 softtabstop=2 smarttab expandtab

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



syn region markdownItalic start="[^* ]\@<=\*\*\@!\|\*\@<!\*[^* ]\@=" end="[^* ]\@<=\*\|\*\@<!\*[^* ]\@=" keepend contains=markdownLineStart
syn region markdownItalic start="[^_ ]\@<=__\@!\|_\@<!_[^_]\@=" end="[^_ ]\@<=_\|_\@<!_[^_]\@=" keepend contains=markdownLineStart

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


" ----------------------------
" Vimdiff syntax highlighting
" ---------------------------
" hi DiffAdd      gui=none    guifg=NONE          guibg=#bada9f
" hi DiffChange   gui=none    guifg=NONE          guibg=#e5d5ac
" hi DiffDelete   gui=bold    guifg=#ff8080       guibg=#ffb0b0
" hi DiffText     gui=none    guifg=NONE          guibg=#8cbee2


" ----------------------------------
"  Spell Highlighting
" ----------------------------------
setlocal spelllang=en_us   " Allows for spellchecking
set spelllang=en_us   " Allows for spellchecking

hi clear SpellBad SpellCap
hi SpellBad ctermfg=015 ctermbg=000 cterm=none guifg=red guibg=#000000 gui=none
hi SpellCap ctermfg=013 ctermbg=000 cterm=none guifg=lightred guibg=#000000 gui=none

