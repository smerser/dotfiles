shopt -s expand_aliases
alias anvio="source ~/virtual-envs/anvio-master/bin/activate"
alias aenea="source ~/virtual-envs/aenea/bin/activate"
alias illumina="source ~/virtual-envs/illumina-utils-master/bin/activate"
alias budget="ipython /Users/Evan/Documents/Personal/Budgeter/Budget_DateFrame.py"
alias mbl="ssh ekiefl@evol5.mbl.edu"
alias midway1="ssh ekiefl@midway-login1.rcc.uchicago.edu"
alias midway2="ssh ekiefl@midway-login2.rcc.uchicago.edu"
alias pymol="/Applications/MacPyMOL.app/Contents/MacOS/MacPyMOL"
alias vim="vi"
alias crypto="~/.crypto"
alias listen="python /Users/evan/Software/aenea/server/osx/server_osx.py"
alias run_dragon="/Applications/Talon.app/Contents/Resources/run_dragon"

# changes title of the window from `old` to `new (old)` via `title new`
function title {
    echo -ne "\033]0;"$*"\007"
}
