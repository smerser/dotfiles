from talon.voice import Word, Context, Key, Rep, Str, press
ctx = Context('vim')

from .std import keymap
from .python import pythonmap

vimmap = {}
vimmap.update(keymap)
vimmap.update(pythonmap)

LEADER = 'space'

# hacky ways for repeat commands that take numbers as variables (there is another one of these in std)
# this doesn't work with buff 
vimmap.update({'%d buff' % k: [Key('escape shift-right')]*k for k in range(1, 10)})
vimmap.update({'%d ruff' % k: [Key('escape shift-left')]*k for k in range(1, 10)})

cursor_movement = {
    # within line search
    "gif"                   : Key("F"),
    "til"                   : Key("t"),
    "lit"                   : Key("T"),
    "bane"                  : Key("ge"),
    "ship bane"             : Key("gE"),

    # line search
    'flexy'                 : Key('0'),

    # line movement
    'fly'                   : Key('G'),

    # variations of slap
    'slapper' : Key('escape shift-a enter'),
    'coder' : Key('escape shift-a : enter tab'),
    'slender' : Key('escape shift-a enter tab'),

}

viewport = {
    "more" : Key("shift-j"),
    "less" : Key("shift-k"),
    "ellie" : Key("shift-u"),
    "vader" : Key("shift-d"),
}

window_handler = {
    'buff'                  : Key('escape shift-right'),
    'ruff'                  : Key('escape shift-left'),
    'north'                 : Key('ctrl-k'),
    'south'                 : Key('ctrl-j'),
    'east'                  : Key('ctrl-l'),
    'west'                  : Key('ctrl-h'),
    'close (buff | buffer)' : Key('%s c' % LEADER),
    'quit (split | window)' : Key('%s q' % LEADER),
    'force quit split'      : Key(':q! enter'),
}

plugins = {
    # surround plugin
    'flurry'                :  Key("cs"),
    'you surrey'            :  Key("ysiw"),

    # tagbar, nerdtree
    'tag-bar'               :  Key("escape %s t" % LEADER),

    # Tabularize
    'tabularize'            :  Key(":Tab space /"),

    # jedi
    'show me'               :  Key('ctrl-space'),
    'soy'                   :  Key('ctrl-y'),
    'go to'                 :  Key('%s d' % LEADER),
    'jedi'                  :  Key('ctrl-j'),
    'kitty'                 :  Key('ctrl-k'),

    # RltvNmbr
    'relnumb'               :  Key(':RN enter'),
}

primitive_commands = {
    'undo'                  :  Key('escape u'),
    'redo'                  :  Key('escape ctrl-r'),

    'bar'         : Key('V'),
    'block'       : Key('ctrl-v'),
    'yank'        : Key('y'),
    'paste'       : Key('p'),
    'post'        : Key('P'),

    # SmartInner
    'winner'      : Key('in'),
    'wander'      : Key('an'),
    'bender'      : Key('il'),
    'banter'      : Key('al'),

    'make upper' :  Key('gU'),
    'make lower' :  Key('gu'),
    'soldier'    :  Key('gq'),

    # marker stuff
    'privvy'       : Key("escape ''"),
    'last change'  : Key("'."),
    'belect'       : Key("'<"),
    'alect'        : Key("'>"),
    'retter'       : Key("'"),

    'save'         : Key('%s w' % LEADER),
    'edit'         : Key('%s e space' % LEADER),
    'source'       : Key(':so space'),
    'settings'     : Key(':set space'),

    # search stuff
    'cancel hits'  : Key("/asdf enter"),
    'nex'          : Key("n"),
    'bex'          : Key("N"),

    'para' : Key("escape o enter"),
    'line' : Key("escape o"),

    'run it' : Key("escape %s w cmd-l up enter" % LEADER),

    }

common_names = {
    "vim our see" : Key("~/.vimrc"),
    "vim" : Key("vim"),
    "dido" : Key("d$"),
    "leader" : Key("%s" % LEADER),
}

vimmap.update(primitive_commands)
vimmap.update(cursor_movement)
vimmap.update(window_handler)
vimmap.update(plugins)
vimmap.update(viewport)
vimmap.update(common_names)

ctx.keymap(vimmap)

def unload():
    ctx.disable()

