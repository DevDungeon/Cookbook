set number
syntax on

"" show existing tab with 4 spaces width
set tabstop=4
"" when indenting with '>', use 4 spaces width
set shiftwidth=4
"" On pressing tab, insert 4 spaces
set expandtab

set showcmd     "" Show (partial) command in status line.
set showmatch       "" Show matching brackets.
set ignorecase      "" Do case insensitive matching
""set smartcase      "" Do smart case matching
set incsearch       "" Incremental search
""set hlsearch
""set autowrite      "" Automatically save before commands like :next and :make
""set hidden     "" Hide buffers when they are abandoned
""set mouse=a        "" Enable mouse usage (all modes)

if filereadable("${HOME}/.vimrc.local")
  source ${HOME}/.vimrc.local
endif

"" Show whitespace
set listchars=tab:>~,nbsp:_,trail:.
set list

"" Make semicolon act as colon
nnoremap ; :

"" Highlight lines that reach the limit
highlight ColorColumn ctermbg=magenta
call matchadd('ColorColumn', '\%80v', 100)

"" Show row/column in status bar
set ruler
