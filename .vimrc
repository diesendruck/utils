"set nocompatible
filetype plugin indent on 
execute pathogen#infect()

syntax on
colorscheme codeschool 
set background=dark
set hlsearch
inoremap ;; <Esc>l
set visualbell

" Quick save mapping
noremap <silent> ;w :update<CR>

" Don't show numbers
set nonumber

" Commenting helpers
vmap <leader>cc :s/^/#/<cr>
vmap <leader>co :s/^#//<cr>

" Indentation changes
set smartindent
set tabstop=2
set shiftwidth=2
set expandtab

" Show column number in status bar
set ruler

" Show filename in status bar
set statusline+=%F

" Slimux config
"
let mapleader=" "
map <Leader>l :SlimuxREPLSendLine<CR>
vmap <Leader>l :SlimuxREPLSendSelection<CR>
map <Leader>a :SlimuxShellLast<CR>
map <leader>k :slimuxsendkeyslast<cr>

