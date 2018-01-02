# dotfiles

dotfiles are symlinked, but dotfolders are updated "manually" by adding this to my bash_profile:

    # copies dotfolder contents into $software/dotfiles. If you get permission denied spam, change
    # permission settings here
    chmod -R 777 $software/dotfiles/.vim/bundle/
    mkdir -p $software/dotfiles/.ipython && cp -r ~/.ipython/* $software/dotfiles/.ipython
    mkdir -p $software/dotfiles/.vim && cp -r ~/.vim/* $software/dotfiles/.vim
