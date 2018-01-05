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
nnoremap <Leader>q :q<CR>
" disable default write and quit (for muscle memory)
nnoremap :w<CR> <nop>
nnoremap :q<CR> <nop>
nnoremap <Leader>x :xa<CR>

" easily edit and source vimrc
:nnoremap <leader>ev :split ~/.vimrc<cr>
:nnoremap <leader>sv :source ~/.vimrc<cr>

" moving around splits
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>

" ' is so much easier to type than ` for markers, that I switch them here
nnoremap ' `
nnoremap ` '

" >> indents in command mode. >M idents to level defined by line aboveAENEA
" command not written yet
" << back-indents in command mode <M back-idents to 0AENEA
nnoremap <M ^d0
" related: some times you just want to move a line up (mnemonic: Move Up)AENEA
nnoremap MU ^d0i<bs><esc>

" when exiting insert mode, the marker r is made
inoremap <esc> <esc>mr

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

" source abbreviations
:so ~/.vim/abbreviations.vim
:so ~/.vim/myscripts.vim

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

map <leader>t :TagbarToggle<CR>
map <leader>o :NERDTree<CR>
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

" check SmoothScroll AENEA

ino <down> <Nop>
ino <left> <Nop>
ino <right> <Nop>
ino <up> <Nop>

" how far away from max cursor position is from window
:set so=1

" buffer stuff
:map <left> :bp!<CR>
:map <right> :bn!<CR> 
:map <leader>c :bw!<CR>

" quickly insert space above and below current line
:nnoremap <C-u> :call ReturnToOriginalPosition("O")<CR>
:nnoremap <C-d> :call ReturnToOriginalPosition("o")<CR>

:set hidden

" jedi autocomplete window navigation
inoremap <expr> <C-j>     pumvisible() ? "\<C-n>" : "\<C-j>"
inoremap <expr> <C-k>     pumvisible() ? "\<C-p>" : "\<C-k>"

" relative numbering (:RltvNmbr enables/disables) `call RltvNmbr#RltvNmbrCtrl(1)` was added to ~/.vim/plugin/RltvNmbr.vim
hi default HL_RltvNmbr_Minus    gui=none,italic ctermfg=172   ctermbg=black guifg=yellow   guibg=black
hi default HL_RltvNmbr_Positive gui=none,italic ctermfg=172 ctermbg=black guifg=yellow guibg=black

" snakemake syntax highlighting
au BufNewFile,BufRead Snakefile set syntax=snakemake
au BufNewFile,BufRead *.smk set syntax=snakemake
au BufNewFile,BufRead *.fasta,*.fa  setf fasta

" operate inside or outside delimiters when cursor is not between
onoremap in( :<C-U>call SmartInner(v:count, 0, "(", "i")<CR>
onoremap in[ :<C-U>call SmartInner(v:count, 0, "[", "i")<CR>
onoremap in< :<C-U>call SmartInner(v:count, 0, "<", "i")<CR>
onoremap in{ :<C-U>call SmartInner(v:count, 0, "{", "i")<CR>
onoremap in" :<C-U>call SmartInner(v:count, 0, '"', "i")<CR>
onoremap in' :<C-U>call SmartInner(v:count, 0, "'", "i")<CR>

onoremap an( :<C-U>call SmartInner(v:count, 0, "(", "a")<CR>
onoremap an[ :<C-U>call SmartInner(v:count, 0, "[", "a")<CR>
onoremap an< :<C-U>call SmartInner(v:count, 0, "<", "a")<CR>
onoremap an{ :<C-U>call SmartInner(v:count, 0, "{", "a")<CR>
onoremap an" :<C-U>call SmartInner(v:count, 0, "'", "a")<CR>
onoremap an' :<C-U>call SmartInner(v:count, 0, '"', "a")<CR>

onoremap il( :<C-U>call SmartInner(v:count, 1, "(", "i")<CR>
onoremap il[ :<C-U>call SmartInner(v:count, 1, "[", "i")<CR>
onoremap il< :<C-U>call SmartInner(v:count, 1, "<", "i")<CR>
onoremap il{ :<C-U>call SmartInner(v:count, 1, "{", "i")<CR>
onoremap il" :<C-U>call SmartInner(v:count, 1, '"', "i")<CR>
onoremap il' :<C-U>call SmartInner(v:count, 1, "'", "i")<CR>

onoremap al( :<C-U>call SmartInner(v:count, 1, "(", "a")<CR>
onoremap al[ :<C-U>call SmartInner(v:count, 1, "[", "a")<CR>
onoremap al< :<C-U>call SmartInner(v:count, 1, "<", "a")<CR>
onoremap al{ :<C-U>call SmartInner(v:count, 1, "{", "a")<CR>
onoremap al" :<C-U>call SmartInner(v:count, 1, '"', "a")<CR>
onoremap al' :<C-U>call SmartInner(v:count, 1, "'", "a")<CR>

" select inside or outside delimiters when cursor is not between
nnoremap vin( :<C-U>call SmartInner(v:count, 0, "(", "i")<CR>
nnoremap vin[ :<C-U>call SmartInner(v:count, 0, "[", "i")<CR>
nnoremap vin< :<C-U>call SmartInner(v:count, 0, "<", "i")<CR>
nnoremap vin{ :<C-U>call SmartInner(v:count, 0, "{", "i")<CR>
nnoremap vin" :<C-U>call SmartInner(v:count, 0, '"', "i")<CR>
nnoremap vin' :<C-U>call SmartInner(v:count, 0, "'", "i")<CR>

nnoremap van( :<C-U>call SmartInner(v:count, 0, "(", "a")<CR>
nnoremap van[ :<C-U>call SmartInner(v:count, 0, "[", "a")<CR>
nnoremap van< :<C-U>call SmartInner(v:count, 0, "<", "a")<CR>
nnoremap van{ :<C-U>call SmartInner(v:count, 0, "{", "a")<CR>
nnoremap van" :<C-U>call SmartInner(v:count, 0, '"', "a")<CR>
nnoremap van' :<C-U>call SmartInner(v:count, 0, "'", "a")<CR>

nnoremap vil( :<C-U>call SmartInner(v:count, 1, "(", "i")<CR>
nnoremap vil[ :<C-U>call SmartInner(v:count, 1, "[", "i")<CR>
nnoremap vil< :<C-U>call SmartInner(v:count, 1, "<", "i")<CR>
nnoremap vil{ :<C-U>call SmartInner(v:count, 1, "{", "i")<CR>
nnoremap vil" :<C-U>call SmartInner(v:count, 1, '"', "i")<CR>
nnoremap vil' :<C-U>call SmartInner(v:count, 1, "'", "i")<CR>

nnoremap val( :<C-U>call SmartInner(v:count, 1, "(", "a")<CR>
nnoremap val[ :<C-U>call SmartInner(v:count, 1, "[", "a")<CR>
nnoremap val< :<C-U>call SmartInner(v:count, 1, "<", "a")<CR>
nnoremap val{ :<C-U>call SmartInner(v:count, 1, "{", "a")<CR>
nnoremap val" :<C-U>call SmartInner(v:count, 1, '"', "a")<CR>
nnoremap val' :<C-U>call SmartInner(v:count, 1, "'", "a")<CR>

