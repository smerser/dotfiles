from talon.voice import Word, Context, Key, Rep, Str, press
ctx = Context('bash', bundle='com.googlecode.iterm2')

from .vim import common_to_bash
from .std import lower_upper_digits
from .mouse import delayed_dubclick

'''
notice that i update the bash dictionary with another dictionary from vim.py. the reason for
this is because i use vim-like editing in my bash, so i port over some of the basic vim commands
'''

bashmap = {}

mouse_map = {
    "passit" : [delayed_dubclick, Key("cmd-v")],
    "passirk" : [delayed_dubclick, Key("cmd-v enter")],
    "cd here" : [delayed_dubclick, "cd ", Key("cmd-v"), "; ls", Key("enter")],
    }

binary_map = {

    "ssh"          : "ssh ",
    "barhally"     : "barhali",
    'cd'           : 'cd ',
    "(vim | fim)"  : "vim ",
    'remove'       : 'rm ',
    'cat'          : 'cat ',
    'ls'           : 'ls ',
    "qstat"        : "qstat ",
    "qdel"         : "qdel ",
    "gzip"         : "gzip ",
    "untar"        : "tar -zxvf ",
    "tar"          : "tar -zcvf ",
    "douche"       : "du -sh ",
    'scp'          : 'scp ',
    'jupiter'      : ['jupyter notebook', Key("enter")],
    'read link'    : "readlink -f ",
    'move'         : 'mv ',
    'virtual env'  : 'virtualenv ',
    'pie env'      : 'pyenv ',
    'python'       : 'python ',
    'ipython'      : 'ipython ',
    'our mrf'      : 'rm -rf ',
    'make durp'    : 'mkdir -p ',
    'run ellis'    : ['ls', Key('enter')],
    'run ellis LA' : ['ls -la', Key('enter')],
    'cluster rise' : 'clusterize -n ',
    'head'         : 'head -n ',
    'tail'         : 'tail -n ',
    'tailff'       : 'tail -f ',
    'column'       : 'column -t ',
    'bartsch'      : 'bash ',
}

git_map = {

    'run get'                :  'git ',
    'run get clone'          :  'git clone ',
   'run get diff'            :  'git diff ',
    'run get branch'         :  'git branch ',
    'run get commit'         :  ['git commit -m ""', Key("left")],
    'run get push'           :  'git push ',
    'run get pull'           :  'git pull ',
    'run get status'         :  ['git status', Key("enter")],
    'run get add'            :  'git add ',
    'run get reset'          :  'git reset --hard HEAD ',
    'run get checkout'       :  'git checkout ',

}

names_map = {

    "mbl"                    :  "mbl",
    "bar hall"               :  "barhal",

    '(dock dock | dockdock)' :  '..',
    'show'                   :  Key("tab tab"),
    'run snakemake'          :  ["snakemake", Key("enter")],
    "sacramento"             :  [Key("esc"), "I#", Key("esc enter")],

    # convenience variables
    'snap academics'     : ["$academics/", Key("tab tab tab")],
    'snap anvio'         : ["$anvio/", Key("tab tab tab")],
    'snap desktop'       : ["$desktop/", Key("tab tab tab")],
    'snap disco'         : ["$disco/", Key("tab tab tab")],
    'snap DESMAN'        : ["$DESMAN/", Key("tab tab tab")],
    'snap documents'     : ["$documents/", Key("tab tab tab")],
    'snap dot files'     : ["$dotfiles/", Key("tab tab tab")],
    'snap illumina'      : ["$illumina/", Key("tab tab tab")],
    'snap meren'         : ["$meren/", Key("tab tab tab")],
    'snap shop'          : ["$shop/", Key("tab tab tab")],
    'snap software'    : ["$software/", Key("tab tab tab")],
    'snap talon'         : ["$talon/", Key("tab tab tab")],
    'snap talon scripts' : ["$talonscripts/", Key("tab tab tab")],
    'snap temp'          : ["$temp/", Key("tab tab tab")],
    'snap vim bundle'    : ["$vimbundle/", Key("tab tab tab")],

}

directory_marking = {}
directory_marking.update({("sticky %s" % x, "export %s=`pwd`" % y) for x, y in lower_upper_digits.items()})
directory_marking.update({("telly %s" % x,  "cd $%s; pwd; ls" % y) for x, y in lower_upper_digits.items()})
for key, value in directory_marking.items():
    directory_marking[key] = [value, Key("enter")]

#air arch = " -a "; ship air arch = " -A "
flags_map = {("%s arch" % x, " -%s " % y) for x, y in lower_upper_digits.items()}

bashmap.update(common_to_bash)
bashmap.update(binary_map)
bashmap.update(git_map)
bashmap.update(names_map)
bashmap.update(flags_map)
bashmap.update(directory_marking)
bashmap.update(mouse_map)

ctx.keymap(bashmap)

