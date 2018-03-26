shopt -s expand_aliases

# shortcuts
alias anvio="source ~/virtual-envs/anvio-master/bin/activate"
alias illumina="source ~/virtual-envs/illumina-utils-master/bin/activate"
alias mbl="ssh ekiefl@evol5.mbl.edu"
alias midway1="ssh ekiefl@midway-login1.rcc.uchicago.edu"
alias midway2="ssh ekiefl@midway-login2.rcc.uchicago.edu"
alias pymol="/Applications/MacPyMOL.app/Contents/MacOS/MacPyMOL"
alias vim="vi"
alias run_dragon="/Applications/Talon.app/Contents/Resources/run_dragon"
alias desman2="source ~/virtual-envs/desman/bin/activate" # DESMAN 2 (is a virtual env)
alias desman3="source ~/virtual-envs/desman3/bin/activate" # DESMAN 3 (is a virtual env)

alias ..="cd .."
alias ...="cd ../.."
alias ....="cd ../../../"
alias .....="cd ../../../.."

# abbreviations
alias tlf="tail -f"
alias rmrf="rm -rf"
alias tarp="tar -zcvf"
alias untarp="tar -zxvf"
alias dush="du -sh"
alias rl="readlink -f"
alias mkdirp="mkdir -p"
alias lsla="ls -la"
alias head="head -n"
alias tail="tail -n"
alias col="column -t"
alias eb="vim ~/.bash_profile"
alias ev="vim ~/.vimrc"
alias sb="source ~/.bash_profile"

# changes title of the window from `old` to `new (old)` via `title new`
function title {
    echo -ne "\033]0;"$*"\007"
}
