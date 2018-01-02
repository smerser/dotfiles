"test
set nowrap
set ai
set history=750
set undolevels=750
set iskeyword+=_,$,@,%,#,-
syntax on
set hlsearch
set number
filetype plugin on
set list
set mouse=v
"set foldmethod=indent

" my leader is space:
let mapleader = "\<Space>"
nnoremap <Leader>w :w<CR>
nnoremap <Leader>x :xa<CR>
nnoremap <leader>q :bp<cr>:bd #<cr>
nnoremap <Leader>qq :q<CR>
nnoremap <Leader>c :Bclose<CR>

nnoremap <Leader>l <C-W><C-L>
" moving around splits
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>

" When editing a file, always jump to the last cursor position
autocmd BufReadPost *
\ if ! exists("g:leave_my_cursor_position_alone") |
\ if line("'\"") > 0 && line ("'\"") <= line("$") |
\ exe "normal g'\"" |
\ endif |
\ endif

set tabstop=4
set softtabstop=4
set shiftwidth=4
set smarttab
set expandtab
set backspace=indent,eol,start

execute pathogen#infect()

set term=xterm-256color
set background=dark
colorscheme gruvbox

set nobackup
set nowritebackup
set noswapfile

let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0
let g:syntastic_python_checkers = ['python']
let g:syntastic_enable_highlighting = 0
map <leader>pp :let g:syntastic_python_checkers = ['pylint']<CR>

let g:jedi#show_call_signatures = "1"
let g:jedi#use_splits_not_buffers = ""
let g:jedi#popup_on_dot = 0
let g:jedi#documentation_command = "R"
let g:jedi#smart_auto_mappings = 0

" closes vim if only window is NERDTree
"autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif
" shows line numbers for NERDTree
let NERDTreeShowLineNumbers=1

" shows line numbers for Tagbar
let g:tagbar_show_linenumbers = 1

map <leader>o :NERDTreeToggle<CR>
map <leader>t :TagbarToggle<CR>
map <leader>e :copen<CR>
map <leader>ee :cc<CR>
map <leader>en :cnext<CR>
map <leader>mm :set mouse=a<CR>
map <leader>me :set mouse=v<CR>
hi SpellBad cterm=underline 
"ctermbg=red ctermfg=black
let g:tagbar_left = 1
let g:airline#extensions#tabline#enabled = 1

if !exists('g:airline_symbols')
    let g:airline_symbols = {}
endif

:let g:airline_theme='simple'

set noruler
set laststatus=2

set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*
set statusline+=%{fugitive#statusline()}

" no automatic word wrap, but `gq` wraps to 100
:set textwidth=100
:set fo-=t

" navigation (CRUCIAL FOR ME!)
no <down> ddp
no <up> ddkP
no <left> <Nop>
no <right> <Nop>

:nnoremap <S-j> jzz
:nnoremap <S-k> kzz

ino <down> <Nop>
ino <left> <Nop>
ino <right> <Nop>
ino <up> <Nop>

:set so=1

" buffer stuff
:map <left> :bp!<CR>
:map <right> :bn!<CR> 
:map <leader>c :bw!<CR>

:set hidden

inoremap <expr> <C-j>     pumvisible() ? "\<C-n>" : "\<C-j>"
inoremap <expr> <C-k>       pumvisible() ? "\<C-p>" : "\<C-k>"

" relative numbering (:RltvNmbr[!] enables/disables) `call RltvNmbr#RltvNmbrCtrl(1)` was added to ~/.vim//plugin/RltvNmbr.vim
hi default HL_RltvNmbr_Minus    gui=none,italic ctermfg=172   ctermbg=black guifg=yellow   guibg=black
hi default HL_RltvNmbr_Positive gui=none,italic ctermfg=172 ctermbg=black guifg=yellow guibg=black

" snakemake syntax highlighting
au BufNewFile,BufRead Snakefile set syntax=snakemake
au BufNewFile,BufRead *.smk set syntax=snakemake
au BufNewFile,BufRead *.fasta,*.fa  setf fasta
