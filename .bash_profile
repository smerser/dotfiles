# hello
# welcome message
cat ~/.bash_welcome

#Define your own aliases here ...
if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

# convenience variables
export academics="/Users/evan/Academics"
export anvio="/Users/evan/Software/anvio"
export desktop="/Users/evan/Desktop"
export disco="/Users/evan/Software/stunning-disco"
export DESMAN="/Users/evan/Software/DESMAN"
export documents="/Users/evan/Documents"
export dotfiles="/Users/evan/Software/dotfiles"
export illumina="/Users/evan/Software/illumina-utils"
export meren="/Users/evan/Academics/Research/Meren"
export popvar="/Users/evan/Software/popvar"
export shop="/Users/evan/Documents/Personal/Recipes/IngredientShopping"
export software="/Users/evan/Software"
export saav="/Users/evan/Software/SAAV-structural-mapping"
export table2md="csvtomd"
export talon="/Applications/Talon.app/Contents/Resources/pypy/site-packages/talon"
export talonscripts="/Users/evan/.talon/user"
export temp="/Users/evan/Academics/Research/Meren/MATS_NSERC/Synechococcus_DAVEWARD"
export vimbundle="/Users/evan/.vim/bundle"

# bash prompt
STARTFGCOLOR='\e[0;30m';
STARTBGCOLOR="\e[43m"
ENDCOLOR="\e[0m"
export PS1="\[$STARTFGCOLOR\]\[$STARTBGCOLOR\]\h:[\W]\[$ENDCOLOR\] "

# ls coloring
export CLICOLOR=1
export LSCOLORS=gxhxCxDxBxegedabagaced

# python paths
export PYTHONPATH="${PYTHONPATH}:/Users/evan/Software/pymol-v1.8.6.0-Darwin-x86_64/modules"
export PYTHONPATH="${PYTHONPATH}:/Users/evan/software/stunning-disco"
export PYTHONPATH="${PYTHONPATH}:/Users/evan/Software/SAAV-structural-mapping/saav_structure"
export PYTHONPATH="${PYTHONPATH}:/Users/evan/Documents/Personal/Recipes/IngredientShopping"

# iterm
test -e "${HOME}/.iterm2_shell_integration.bash" && source "${HOME}/.iterm2_shell_integration.bash"

# pyenv 
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

# embedded matplotlib images
#export MPLBACKEND="module://itermplot"
#export ITERMPLOT=rv

# centrifuge
export CENTRIFUGE_BASE="/Users/evan/Software/CENTRIFUGE"
export PATH=$PATH:$CENTRIFUGE_BASE/centrifuge

# DESMAN
export PATH=$HOME/Users/evan/Software/DESMAN/scripts:$PATH

# copies dotfolder contents into $software/dotfiles. If you get permission denied spam, change
# permission settings here. I copy some dotfiles as well incase some of the symlinks are broken
rm -rf $software/dotfiles/.ipython && mkdir -p $software/dotfiles/.ipython && cp -r ~/.ipython/* $software/dotfiles/.ipython
rm -rf $software/dotfiles/.vim && mkdir -p $software/dotfiles/.vim && cp -r ~/.vim/* $software/dotfiles/.vim
rm -rf $software/dotfiles/.jupyter && mkdir -p $software/dotfiles/.jupyter && cp -r ~/.jupyter/* $software/dotfiles/.jupyter
rm -rf $software/dotfiles/.talon && mkdir -p $software/dotfiles/.talon && cp -r ~/.talon/* $software/dotfiles/.talon
cp ~/.vimrc $software/dotfiles/.vimrc
cp ~/.bash_profile $software/dotfiles/.bash_profile
cp ~/.bash_aliases $software/dotfiles/.bash_aliases
rm -rf $software/dotfiles/.vim/bundle/*/.git/

