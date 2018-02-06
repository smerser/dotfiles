from talon.voice import Word, Context, Key, Rep, Str, press
ctx = Context('bash', bundle='com.googlecode.iterm2')

from .vim import common_to_bash

'''
notice that i update the bash dictionary with another dictionary from vim.py. the reason for
this is because i use vim-like editing in my bash, so i port over some of the basic vim commands
'''

bashmap = {

    "mbl" : "mbl",
    "bar hall" : "barhal",

    "ssh" : "ssh ",
    "ssh long" : "ssh -L 8091:localhost:8091 ",
    '(dock dock | dockdock)' : '..',
    'cd'                     : 'cd ',
    "(vim | fim)" : "vim ",
    'remove'                 : 'rm ',
    'show'                 : Key("tab tab"),
    'cat'                 : 'cat ',
    'ls'                 : 'ls ',
    "qstat" : "qstat ",
    "qdel" : "qdel ",
    "gzip" : "gzip ",
    "douche" : "du -sh ",
    'scp'                 : 'scp ',
    'move'                 : 'mv ',
    'python'                 : 'python ',
    'our mrf'                 : 'rm -rf ',
    'make durr'              : 'mkdir ',
    'run get'                : 'git ',
    'run get clone'          : 'git clone ',
    'run get diff'           : 'git diff ',
    'run get branch'         : 'git branch ',
    'run get commit'         : ['git commit -m ""', Key("left")],
    'run get push'           : 'git push ',
    'run get pull'           : 'git pull ',
    'run get status'         : 'git status ',
    'run get add'            : 'git add ',
    'run get reset'          : 'git reset --hard HEAD ',
    'run get checkout'          : 'git checkout ',
    'run ellis'              : 'ls\n',
    'run ellis LA'           : 'ls -la\n',

    'run snakemake'           : ["snakemake", Key("enter")],
    # Only works using vim mode insertion
    "sacramento" : [Key("esc"), "I#", Key("esc enter")],

    'zoom in' : Key('cmd-='),
    'zoom out' : Key('cmd+-'),

    # convenience variables
    'snap academics'  : Key("$academics/ tab tab tab"),
    'snap anvio'      : Key("$anvio/ tab tab tab"),
    'snap desktop'    : Key("$desktop/ tab tab tab"),
    'snap disco'      : Key("$disco/ tab tab tab"),
    'snap DESMAN'     : Key("$DESMAN/ tab tab tab"),
    'snap documents'  : Key("$documents/ tab tab tab"),
    'snap illumina'   : Key("$illumina/ tab tab tab"),
    'snap meren'      : Key("$meren/ tab tab tab"),
    'snap shop'       : Key("$shop/ tab tab tab"),
    'snap soft where' : Key("$software/ tab tab tab"),
    'snap talon'      : Key("$talon/ tab tab tab"),
    'snap talon scripts'      : Key("$talonscripts/ tab tab tab"),
    'snap temp'       : Key("$temp/ tab tab tab"),
    'snap vim bundle'       : Key("$vimbundle/ tab tab tab"),

}

bashmap.update(common_to_bash)

ctx.keymap(bashmap)

def unload():
    ctx.disable()

