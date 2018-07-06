from talon.voice import Word, Context, Key, Rep, Str, press
ctx = Context('bash', bundle='com.googlecode.iterm2')

from .vim import common_to_bash
from .std import lower_upper_digits
from .mouse import initial_pos_dubclick

bashmap = {}

mouse_map = {
    "passit" : [initial_pos_dubclick, Key("cmd-v")],
    "passirk" : [initial_pos_dubclick, Key("cmd-v enter")],
    "cd here" : [initial_pos_dubclick, "cd ", Key("cmd-v"), "; ls", Key("enter")],
}; bashmap.update(mouse_map)

binary_map = {
    "ssh"          : "ssh ",
    "barhally"     : ["barhali", Key("enter")],
    'cd'           : 'cd ',
    "(vim | fim)"  : "vim ",
    'remove'       : 'rm ',
    'grep'         : 'grep ',
    'cat'          : 'cat ',
    'ls'           : 'ls ',
    "qstat"        : ['qstat', Key("enter")],
    "qstat me"     : ['qstat -u ekiefl', Key("enter")],
    "screen"       : "screen ",
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
    'talon log'    : ['tail -f ~/.talon/talon.log', Key("enter")],
    'tailff'       : 'tail -f ',
    'column'       : 'column -t ',
    'bartsch'      : 'bash ',
    'fg'           : ['fg', Key("enter")],
    'ground'       : [Key("ctrl-z")],
}; bashmap.update(binary_map)

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
}; bashmap.update(git_map)

names_map = {
    "mbl"                    :  "mbl",
    "bar hall"               :  "barhal",

    '(dock dock | dockdock)' :  '../',
    'show'                   :  Key("tab tab"),
    'run snakemake'          :  ["snakemake", Key("enter")],
    "sacramento"             :  [Key("esc"), "I#", Key("esc enter")],

    # convenience variables
    'snap academics'     : ["$academics/", Key("tab tab")],
    'snap anvio'         : ["$anvio/", Key("tab tab")],
    'snap codebase'      : ["$codebase/", Key("tab tab")],
    'snap desktop'       : ["$desktop/", Key("tab tab")],
    'snap disco'         : ["$disco/", Key("tab tab")],
    'snap DESMAN'        : ["$DESMAN/", Key("tab tab")],
    'snap documents'     : ["$documents/", Key("tab tab")],
    'snap dot files'     : ["$dotfiles/", Key("tab tab")],
    'snap illumina'      : ["$illumina/", Key("tab tab")],
    'snap meren'         : ["$meren/", Key("tab tab")],
    'snap shop'          : ["$shop/", Key("tab tab")],
    'snap software'      : ["$software/", Key("tab tab")],
    'snap talon'         : ["$talon/", Key("tab tab")],
    'snap talon scripts' : ["$talonscripts/", Key("tab tab")],
    'snap temp'          : ["$temp/", Key("tab tab")],
    'snap vim bundle'    : ["$vimbundle/", Key("tab tab")],
}; bashmap.update(names_map)

directory_marking = {}
directory_marking.update({("sticky %s" % x, "export %s=`pwd`" % y) for x, y in lower_upper_digits.items()})
directory_marking.update({("telly %s" % x,  "cd $%s; pwd; ls" % y) for x, y in lower_upper_digits.items()})
for key, value in directory_marking.items():
    directory_marking[key] = [value, Key("enter")]
bashmap.update(directory_marking)

#air arch = " -a "; ship air arch = " -A "
flags_map = {("%s arch" % x, " -%s " % y) for x, y in lower_upper_digits.items()}
bashmap.update(flags_map)

bashmap.update(common_to_bash)
ctx.keymap(bashmap)

