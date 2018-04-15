from talon.voice import Word, Context, Key, Rep, Str, press
from .mouse import delayed_click
import time
ctx = Context('vim', bundle='com.googlecode.iterm2', func=lambda app, win: 'vim' in win.title)

vimmap = {}

LEADER = 'space'

# hacky ways for repeat commands that take numbers as variables (there is another one of these in std)
# this doesn't work with buff 
vimmap.update({'%d buff' % k: [Key('escape shift-right')]*k for k in range(1, 10)})
vimmap.update({'%d ruff' % k: [Key('escape shift-left')]*k for k in range(1, 10)})
vimmap.update({'%d box' % k: ['x']*k for k in range(2, 10)})
vimmap.update({'%d undo' % k: ['u']*k for k in range(2, 10)})
vimmap.update({'%d redo' % k: [Key('ctrl-r')]*k for k in range(2, 10)})

# share this with bash.py
common_to_bash = {
    # within line search
    "gif"       : "F",
    "til"       : "t",
    "lit"       : "T",
    "bane"      : "ge",
    "ship bane" : "gE",

    "die line"  : "dd",
}

cursor_movement = {
    # line search
    'flexy'                 : '0',

    # line movement
    'fly'                   : 'G',

    # variations of slap
    'slapper' : Key('escape shift-a enter'),
    'coder' : Key('escape shift-a : enter tab'),
    'slender' : Key('escape shift-a enter tab'),

}

viewport = {
    "more" : Key("shift-j"),
    "less" : Key("shift-k"),
    "lesser" : Key("shift-u"),
    "mortar" : Key("shift-d"),
}

window_handler = {
    'buff'                  : Key('escape shift-right'),
    'ruff'                  : Key('escape shift-left'),
    'north'                 : Key('ctrl-k'),
    'south'                 : Key('ctrl-j'),
    'east'                  : Key('ctrl-l'),
    'west'                  : Key('ctrl-h'),
    'close (buff | buffer)' : Key('%s c' % LEADER),
    # sometimes saving doesn't work on barhal so small sleep command is added
    'write it'              : [Key('escape'), lambda m: time.sleep(0.25), Key('%s w' % LEADER)],
    'run it'                : [Key('escape'), lambda m: time.sleep(0.25), Key('%s w cmd-l up enter' % LEADER)],

    'quit it'               : Key('%s q' % LEADER),
    'force quit split'      : [':q!', Key('enter')],
}

plugins = {
    # tagbar, nerdtree
   '(tack board | tag-bar)' :  [Key("escape %s" % LEADER), "t"],
   'nerd'                   :  [Key("escape %s" % LEADER), "o"],

    # Tabularize
    'tabularize'            :  [":Tab", Key("space"), "/"],

    # jedi
    'show me'               :  Key('ctrl-space'),
    'soy'                   :  Key('ctrl-y'),
    'go to'                 :  [Key('%s' % LEADER), "d"],

    # RltvNmbr
    'relnumb'               :  [':RN', Key('enter')],
}

primitive_commands = {
    'undo'                  :  [Key('escape'), "u"],
    'redo'                  :  Key('escape ctrl-r'),

    'oozey' : Key("ctrl-o"),

    'bar'         : 'V',
    'block'       : Key('ctrl-v'),

    # SmartInner
    'winner'      : 'in',
    'wander'      : 'an',
    'bender'      : 'il',
    'banter'      : 'al',

    'make upper' :  'gU',
    'make lower' :  'gu',
    'soldier'    :  'gq',

    # marker stuff
    'privvy'       : [Key("escape"), "''"],
    'last change'  : "'.",
    'belect'       : "'<",
    'alect'        : "'>",

    'edit'         : Key('%s e space' % LEADER),
    'source'       : [":so", Key('space')],
    'settings'     : [":set", Key('space')],
    'settings paste'     : [":set", Key("space"), "paste", Key("enter")],
    'settings no paste'     : [":set", Key("space"), "nopaste", Key("enter")],

    # search stuff
    'cancel hits' :  ["/asdf", Key("enter")],
    'nex'         :  Key("n"),
    'bex'         :  Key("N"),
    'sore'        :  [":s///g"] + [Key("left")]*3,
    'globsore'    :  [":%s///g"] + [Key("left")]*3,

    'para' : [Key("escape"), "o", Key("enter")],

    }

mouse_map = {
    "psych whale"      : [Key("escape"), "mt", delayed_click, "yiw'tpa"],
    "psych ship whale" : [Key("escape"), "mt", delayed_click, "yiW'tpa"],
    "psych doll"       : [Key("escape"), "mt", delayed_click, "y$'tpa"],
    "psych sit larry"  : [Key("escape"), "mt", delayed_click, "yi('tpa"],
    "psych sit lack"   : [Key("escape"), "mt", delayed_click, "yi['tpa"],
    "psych sit lace"   : [Key("escape"), "mt", delayed_click, "yi{'tpa"],
    "psych sit langle" : [Key("escape"), "mt", delayed_click, "yi<'tpa"],
    "psych sit sote"   : [Key("escape"), "mt", delayed_click, "yi''tpa"],
    "psych sit quote"  : [Key("escape"), "mt", delayed_click, """yi"'tpa"""],
    "psych air lack"   : [Key("escape"), "mt", delayed_click, "ya['tpa"],
    "psych air lace"   : [Key("escape"), "mt", delayed_click, "ya{'tpa"],
    "psych air langle" : [Key("escape"), "mt", delayed_click, "ya<'tpa"],
    "psych air sote"   : [Key("escape"), "mt", delayed_click, "ya''tpa"],
    "psych air quote"  : [Key("escape"), "mt", delayed_click, """ya"'tpa"""],

    "steal whale"      : [Key("escape"), "mt", delayed_click, "yiw't"],
    "steal ship whale" : [Key("escape"), "mt", delayed_click, "yiW't"],
    "steal doll"       : [Key("escape"), "mt", delayed_click, "y$'t"],
    "steal sit larry"  : [Key("escape"), "mt", delayed_click, "yi('t"],
    "steal sit lack"   : [Key("escape"), "mt", delayed_click, "yi['t"],
    "steal sit lace"   : [Key("escape"), "mt", delayed_click, "yi{'t"],
    "steal sit langle" : [Key("escape"), "mt", delayed_click, "yi<'t"],
    "steal sit sote"   : [Key("escape"), "mt", delayed_click, "yi''t"],
    "steal sit quote"  : [Key("escape"), "mt", delayed_click, """yi"'t"""],
    "steal air lack"   : [Key("escape"), "mt", delayed_click, "ya['t"],
    "steal air lace"   : [Key("escape"), "mt", delayed_click, "ya{'t"],
    "steal air langle" : [Key("escape"), "mt", delayed_click, "ya<'t"],
    "steal air sote"   : [Key("escape"), "mt", delayed_click, "ya''t"],
    "steal air quote"  : [Key("escape"), "mt", delayed_click, """ya"'t"""],
}

common_names = {
    "dido" : "d$",
    "leader" : Key("%s" % LEADER),
}

vimmap.update(primitive_commands)
vimmap.update(cursor_movement)
vimmap.update(window_handler)
vimmap.update(plugins)
vimmap.update(viewport)
vimmap.update(common_names)
vimmap.update(common_to_bash)
vimmap.update(mouse_map)

ctx.keymap(vimmap)

