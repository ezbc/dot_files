Vim�UnDo� ��1O�c�Zd��`�bFhVBeL�֍�X���6H   �   imap <A-a> <Esc>            M       M   M   M    T�x    _�                     F        ����                                                                                                                                                                                                                                                                                                                                                             S�l     �   E   I   �       5�_�                    F        ����                                                                                                                                                                                                                                                                                                                                                             S�n     �   D   F   �      set guioptions-=L    �   E   G   �       5�_�                    F        ����                                                                                                                                                                                                                                                                                                                                                             S�o    �   E   G   �       5�_�                    F       ����                                                                                                                                                                                                                                                                                                                                                             S瘘    �   E   G   �      set guifont=Monospace 105�_�                    F       ����                                                                                                                                                                                                                                                                                                                                                             S瘰    �   E   G   �      set guifont=Monospace\ 105�_�                    d        ����                                                                                                                                                                                                                                                                                                                                                             S�~     �   c   d           5�_�                    d        ����                                                                                                                                                                                                                                                                                                                                                             S�~     �   c   d           5�_�      	              d        ����                                                                                                                                                                                                                                                                                                                                                             S�     �   c   d           5�_�      
           	   c        ����                                                                                                                                                                                                                                                                                                                                                             S療     �   b   c           5�_�   	              
   c        ����                                                                                                                                                                                                                                                                                                                                                             S療     �   b   c           5�_�   
                 Q        ����                                                                                                                                                                                                                                                                                                                                                             S癇     �   P   Q           5�_�                    A       ����                                                                                                                                                                                                                                                                                                                                                             S癡     �   A   H   �    �   A   B   �    5�_�                    C        ����                                                                                                                                                                                                                                                                                                                            C           F           V        S癣     �   B   C              set guioptions-=T       set guioptions-=e       set t_Co=256       set guitablabel=%M\ %t5�_�                    D        ����                                                                                                                                                                                                                                                                                                                            D           H           V        S癥     �   C   D          set guioptions-=m   set guioptions-=T   set guioptions-=r   set guioptions-=L   set guifont=Monospace\ 85�_�                    B        ����                                                                                                                                                                                                                                                                                                                            D           D           V        S癦     �   B   H   �    �   B   C   �    5�_�                    C        ����                                                                                                                                                                                                                                                                                                                            C           G           V        S癧    �   B   H   �      set guioptions-=m   set guioptions-=T   set guioptions-=r   set guioptions-=L   set guifont=Monospace\ 85�_�                    G       ����                                                                                                                                                                                                                                                                                                                            C           G           V        S�B    �   F   H   �          set guifont=Monospace\ 85�_�                    G       ����                                                                                                                                                                                                                                                                                                                            C           G           V        S皕    �   F   H   �          set guifont=Monospace:h85�_�                    G       ����                                                                                                                                                                                                                                                                                                                            C           G           V        S��     �   F   H   �          set guifont=Monospace\ 85�_�                    G       ����                                                                                                                                                                                                                                                                                                                            C           G           V        S��     �   F   H   �          set guifont=Monospace 85�_�                    G       ����                                                                                                                                                                                                                                                                                                                            C           G           V        S��    �   F   H   �          set guifont=Monospace85�_�                    G       ����                                                                                                                                                                                                                                                                                                                            C           G           V        S�=     �   F   H   �          set guifont=Monospace:h85�_�                    G       ����                                                                                                                                                                                                                                                                                                                            C           G           V        S�?     �   F   H   �          set guifont=Monospace\ 85�_�                    G       ����                                                                                                                                                                                                                                                                                                                            C           G           V        S�@   	 �   F   H   �          set guifont=Monospace\ 5�_�                    R       ����                                                                                                                                                                                                                                                                                                                            C           G           V        S�T   
 �   Q   T   �      imap <C-v> <ESC>"+pa5�_�                    7        ����                                                                                                                                                                                                                                                                                                                            7           <                   S盭    �   6   8   �      >set colorcolumn=+1        " highlight column after 'textwidth'�   6   =   �      ?#set colorcolumn=+1        " highlight column after 'textwidth'   F#set colorcolumn=+1,+2,+3  " highlight three columns after 'textwidth'   8#highlight ColorColumn ctermbg=lightgrey guibg=lightgrey   #set colorcolumn=80   #set numberwidth=3   #set cpoptions+=n5�_�                    f        ����                                                                                                                                                                                                                                                                                                                            �           f           v        S�     �   e   g   �   0   N" ----------------------------------------------------------------------------   " Vundle   N" ----------------------------------------------------------------------------       5set nocompatible              " be iMproved, required   (filetype off                  " required       7" set the runtime path to include Vundle and initialize   !set rtp+=~/.vim/bundle/Vundle.vim   call vundle#begin()   @" alternatively, pass a path where Vundle should install plugins   &"call vundle#begin('~/some/path/here')       $" let Vundle manage Vundle, required   Plugin 'gmarik/Vundle.vim'       <" The following are examples of different formats supported.   0" Keep Plugin commands between vundle#begin/end.   " plugin on GitHub repo   Plugin 'tpope/vim-fugitive'   5" plugin from http://vim-scripts.org/vim/scripts.html   Plugin 'L9'   !" Git plugin not hosted on GitHub   ,Plugin 'git://git.wincent.com/command-t.git'   H" git repos on your local machine (i.e. when working on your own plugin)   +Plugin 'file:///home/gmarik/path/to/plugin'   F" The sparkup vim script is in a subdirectory of this repo called vim.   0" Pass the path to set the runtimepath properly.   *Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}   " Avoid a name conflict with L9   #Plugin 'user/L9', {'name': 'newL9'}       =" All of your Plugins must be added before the following line   'call vundle#end()            " required   'filetype plugin indent on    " required   /" To ignore plugin indent changes, instead use:   "filetype plugin on   "   " Brief help   0" :PluginList          - list configured plugins   1" :PluginInstall(!)    - install (update) plugins   @" :PluginSearch(!) foo - search (or refresh cache first) for foo   L" :PluginClean(!)      - confirm (or auto-approve) removal of unused plugins   "   0" see :h vundle for more details or wiki for FAQ   +" Put your non-Plugin stuff after this line        5�_�                    e        ����                                                                                                                                                                                                                                                                                                                            f           f           v        S�    �   d   e           5�_�                    k        ����                                                                                                                                                                                                                                                                                                                            e           e           v        S�+     �   j   l   z      Plugin 'SirVer/ultisnips'5�_�                    k        ����                                                                                                                                                                                                                                                                                                                            e           e           v        S�,    �   j   l   z      "Plugin 'SirVer/ultisnips'5�_�                     k        ����                                                                                                                                                                                                                                                                                                                            e           e           v        S�1     �   j   l   z      Plugin 'SirVer/ultisnips'5�_�      !               n        ����                                                                                                                                                                                                                                                                                                                            e           e           v        S�3    �   m   o   z      Plugin 'honza/vim-snippets'5�_�       "           !      
    ����                                                                                                                                                                                                                                                                                                                                                             T�     �         z      vmap <A-a> <Esc>5�_�   !   #           "      	    ����                                                                                                                                                                                                                                                                                                                                                             T�*     �         z      vmap <j-k> <Esc>5�_�   "   $           #          ����                                                                                                                                                                                                                                                                                                                                                             T�*     �         z      vmap <j-k <Esc>5�_�   #   %           $          ����                                                                                                                                                                                                                                                                                                                                                             T�+     �         z      vmap <jk <Esc>5�_�   $   &           %          ����                                                                                                                                                                                                                                                                                                                                                             T�,     �         z      imap <A-a> <Esc>5�_�   %   '           &          ����                                                                                                                                                                                                                                                                                                                                                             T�0     �         z      imap A-a> <Esc>5�_�   &   (           '          ����                                                                                                                                                                                                                                                                                                                                                             T�0     �         z      imap -a> <Esc>5�_�   '   )           (          ����                                                                                                                                                                                                                                                                                                                                                             T�0     �         z      imap a> <Esc>5�_�   (   *           )          ����                                                                                                                                                                                                                                                                                                                                                             T�1     �         z      imap > <Esc>5�_�   )   +           *          ����                                                                                                                                                                                                                                                                                                                                                             T�2    �         z      imap  <Esc>5�_�   *   ,           +          ����                                                                                                                                                                                                                                                                                                                                                V       T�v     �      
   z    �         z    5�_�   +   -           ,           ����                                                                                                                                                                                                                                                                                                                                       	           V        T�y     �                imap jk <Esc>   vmap jk <Esc>5�_�   ,   .           -           ����                                                                                                                                                                                                                                                                                                                                                  V        T�z     �         z      vmap jk <Esc>5�_�   -   /           .           ����                                                                                                                                                                                                                                                                                                                                                  V        T�{     �         z      imap jk <Esc>5�_�   .   0           /           ����                                                                                                                                                                                                                                                                                                                                                  V        T�|     �      
   z      " reformat paragraph5�_�   /   1           0   	        ����                                                                                                                                                                                                                                                                                                                                                  V        T�     �      
   {      á" reformat paragraph5�_�   0   2           1          ����                                                                                                                                                                                                                                                                                                                                                  V        T��     �         {      map jk <Esc>5�_�   1   3           2          ����                                                                                                                                                                                                                                                                                                                                                  V        T��    �         {      map k <Esc>5�_�   2   4           3           ����                                                                                                                                                                                                                                                                                                                                                             T��     �         {      map jk <Esc>5�_�   3   5           4           ����                                                                                                                                                                                                                                                                                                                                                             T��     �         {      map kj <Esc>5�_�   4   6           5           ����                                                                                                                                                                                                                                                                                                                                                  V        T��     �      
   {    �         {    5�_�   5   7           6          ����                                                                                                                                                                                                                                                                                                                                                  V        T��     �      	   }      imap jk <Esc>5�_�   6   8           7          ����                                                                                                                                                                                                                                                                                                                                                  V        T��     �      	   }      imap k <Esc>5�_�   7   9           8          ����                                                                                                                                                                                                                                                                                                                                                  V        T��     �      	   }      imap  <Esc>5�_�   8   :           9   	       ����                                                                                                                                                                                                                                                                                                                                                  V        T��     �      
   }      vmap kj <Esc>5�_�   9   ;           :   	       ����                                                                                                                                                                                                                                                                                                                	                                V        T��     �   	   
   ~      vmap jk <Esc>�      	   }    5�_�   :   <           ;          ����                                                                                                                                                                                                                                                                                                                                                V        T��     �      	   ~      vmap jk <Esc>�         }    5�_�   ;   =           <          ����                                                                                                                                                                                                                                                                                                                                                V        T��    �         ~      vmap kj <Esc>�   	      }    5�_�   <   >           =   	       ����                                                                                                                                                                                                                                                                                                                	                                           T��     �      
   }      vmap kj <Esc>5�_�   =   ?           >   	       ����                                                                                                                                                                                                                                                                                                                	                                           T��     �      
   }      vmap kj <Esc>5�_�   >   @           ?   	       ����                                                                                                                                                                                                                                                                                                                	                                           T��     �      
   }      vmap kj <Esc>ká5�_�   ?   A           @   	       ����                                                                                                                                                                                                                                                                                                                	                                           T��     �      
   }      vmap kj <Esc>k5�_�   @   B           A          ����                                                                                                                                                                                                                                                                                                                	                                           T��     �      	   }      imap kj <Esc>5�_�   A   C           B          ����                                                                                                                                                                                                                                                                                                                	                                           T��    �         }      imap jk <Esc>5�_�   B   D           C          ����                                                                                                                                                                                                                                                                                                                	                                           T�     �      	   }      imap kj <Esc>k5�_�   C   E           D          ����                                                                                                                                                                                                                                                                                                                	                                           T�    �         }      imap jk <Esc>j5�_�   D   F           E          ����                                                                                                                                                                                                                                                                                                                	                                           T�    �         }      imap jk <Esc>h5�_�   E   G           F          ����                                                                                                                                                                                                                                                                                                                	                                           T�     �         }      imap jk <Esc>5�_�   F   H           G   	       ����                                                                                                                                                                                                                                                                                                                	                                           T�z     �   	      ~       �   	      }    5�_�   G   I           H          ����                                                                                                                                                                                                                                                                                                                	                                           TĆ     �   
            
imap <Esc>5�_�   H   J           I           ����                                                                                                                                                                                                                                                                                                                	                                V        TĠ     �             �             5�_�   I   K           J           ����                                                                                                                                                                                                                                                                                                                	                                V        Tġ     �         �      imap <A-a> <Esc>5�_�   J   L           K           ����                                                                                                                                                                                                                                                                                                                	                                V        Tġ    �         �      map <A-a> <Esc>5�_�   K   M           L          ����                                                                                                                                                                                                                                                                                                                	                                V        T��    �   
      �      imap <A-a> <Esc>5�_�   L               M          ����                                                                                                                                                                                                                                                                                                                	                                           T�w    �   
      �      imap <A-a> <Esc>l5��