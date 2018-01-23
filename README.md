# dotfiles

dotfiles are symlinked, but dotfolders are updated "manually" by adding this to my bash_profile:

    # copies dotfolder contents into $software/dotfiles. If you get permission denied spam, change
    # permission settings here. notice that this is only 4 dotfolder contents, dotfiles are symlinked
    rm -rf $software/dotfiles/.ipython && mkdir -p $software/dotfiles/.ipython && cp -r ~/.ipython/* $software/dotfiles/.ipython
    rm -rf $software/dotfiles/.vim && mkdir -p $software/dotfiles/.vim && cp -r ~/.vim/* $software/dotfiles/.vim
    rm -rf $software/dotfiles/.jupyter && mkdir -p $software/dotfiles/.jupyter && cp -r ~/.jupyter/* $software/dotfiles/.jupyter
    rm -rf $software/dotfiles/.talon && mkdir -p $software/dotfiles/.talon && cp -r ~/.talon/* $software/dotfiles/.talon
    rm -rf $software/dotfiles/.vim/bundle/*/.git/

