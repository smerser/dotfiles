" makes a new line above the current line, then returns to previous cursor position
function! MakeSpaceUp()
    execute "normal! mqO\<esc>`q"
endfunction

" makes a new line above the current line, then returns to previous cursor position
function! MakeSpaceDown()
    execute "normal! mqo\<esc>`q"
endfunction

" 
function! Foo(count)
    echo 'FOO: ' . a:count
    endfunction

nmap ,a :<C-U>call Foo(v:count)<C-R>

" command! -nargs=1 FooCmd call Foo(<args>)
" map ,a :<C-U>FooCmd(v:count)<CR>
