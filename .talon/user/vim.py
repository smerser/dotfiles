from talon.voice import Word, Context, Key, Rep, Str, press
from .mouse import initial_pos_click
from .std import punctuation
from .std import lower_upper_digits
import time
ctx = Context('vim', bundle='com.googlecode.iterm2', func=lambda app, win: 'vim' in win.title)

vimmap = {}

LEADER = 'space'

# hacky ways for repeat commands that take numbers as variables (there is another one of these in std)
vimmap.update({'%d buff' % k: [Key('escape shift-right'), lambda m: time.time(0.1)]*k for k in range(1, 10)})
vimmap.update({'%d ruff' % k: [Key('escape shift-left'), lambda m: time.time(0.1)]*k for k in range(1, 10)})
vimmap.update({'%d box' % k: ['x']*k for k in range(2, 10)})
vimmap.update({'%d undo' % k: ['u']*k for k in range(2, 10)})
vimmap.update({'%d redo' % k: [Key('ctrl-r')]*k for k in range(2, 10)})

# share this with bash.py (I have vim-style bash -- see ~/.inputrc)
common_to_bash = {
    "gif"       : "F",
    "til"       : "t",
    "lit"       : "T",
    "bane"      : "ge",
    "ship bane" : "gE",
    "die line"  : "dd",
}; vimmap.update(common_to_bash)

cursor_movement = {
    # line search
    'flexy'                 : '0',

    # line movement
    'fly'                   : 'G',

    # variations of slap
    'slapper' : Key('escape shift-a enter'),
    'coder' : Key('escape shift-a : enter tab'),
    'slender' : Key('escape shift-a enter tab'),
}; vimmap.update(cursor_movement)

viewport = {
    "more" : Key("shift-j"),
    "less" : Key("shift-k"),
    "lesser" : Key("shift-u"),
    "mortar" : Key("shift-d"),
}; vimmap.update(viewport)

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

    'quit it'               : [Key('%s ' % LEADER), "q"],
    'force quit it'         : [Key('%s ' % LEADER), "fq"],
}; vimmap.update(window_handler)

plugins = {
    # tagbar, nerdtree
   '(tack board | tag-bar)' :  [Key("escape %s" % LEADER), "t"],
   'nerd'                   :  [Key("escape %s" % LEADER), "o"],

    # Tabularize
    'tabularize'            :  [":Tab", Key("space"), "/"],

    # jedi
    'show me'               :  lambda m: press('ctrl-space', wait=16000),
    'soy'                   :  Key('ctrl-y'),
    'go to'                 :  [Key('%s' % LEADER), "d"],

    # RltvNmbr
    'relnumb'               :  [':RN', Key('enter')],
}

plugins.update({'%d jedi' % k: [Key('ctrl-j')]*k for k in range(2, 10)})
plugins.update({'%d kitty' % k: [Key('ctrl-k')]*k for k in range(2, 10)})
vimmap.update(plugins)

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
}; vimmap.update(primitive_commands)

# Key("left"), Key("right") used to maintain column position when escaping immediately after `o` or `O`
make_marker = lambda *args: [Key("left"), Key("right"), Key("escape"), Str("mt")]

text_selectors = {
    "whale"      : "iw",
    "ship whale" : "iW",
    "each"       : "e",
    "ship each"  : "E",
    "bat"        : "b",
    "ship bat"   : "B",
    "doll"       : "$",
    "sit larry"  : "i(",
    "sit lack"   : "i[",
    "sit lace"   : "i{",
    "sit langle" : "i<",
    "sit sote"   : "i'",
    "sit quote"  : "i\"",
    "air lack"   : "a[",
    "air lace"   : "a{",
    "air langle" : "a<",
    "air sote"   : "a'",
    "air quote"  : "a\"",
    "fail"       : "f",
    "til"        : "t",
    "gif"        : "F",
    "lit"        : "T",
}

single_click_commands = [
    'psych',
    'steal',
    'slice',
    'kill',
    'kip',
    'phipps',
]

movement_targets = lower_upper_digits.copy()
movement_targets.update(punctuation)

def SingleClickCommand(m):

    utterance = []
    for w in m._words:
        utterance.append(w.word)

    if utterance[0] == "psych":
        preprend = 'y' # yank
        append = "'tpa" # return to marker, paste, re-enter insert mode

    elif utterance[0] == "steal":
        preprend = 'y' # yank
        append = "'t" # return to marker

    elif utterance[0] == "slice":
        preprend = 'd' # delete
        append = "'tpa" # return to marker, paste, re-enter insert mode

    elif utterance[0] == "kill":
        preprend = 'd' # delete
        append = "'t" # return to marker, paste, re-enter insert mode

    elif utterance[0] == "kip":
        preprend = 'c' # change
        append = ""

    elif utterance[0] == "phipps":
        preprend = 'v' # select
        append = ""

    marker_operations = make_marker(m)
    for action in marker_operations:
        action(m)
    time.sleep(0.001)
    initial_pos_click(m)
    del utterance[0] # remove teleport operator from utterance

    movement_strokes = text_selectors.get(' '.join(utterance), False)
    if not movement_strokes:
        # movement key was also uttered. fish it out.
        if movement_targets.get(' '.join(utterance[-2:]), False):
            movement_strokes = text_selectors[' '.join(utterance[:-2])] + movement_targets[' '.join(utterance[-2:])]
        else:
            movement_strokes = text_selectors[' '.join(utterance[:-1])] + movement_targets[utterance[-1]]

    movement_strokes = preprend + movement_strokes + append
    Str(movement_strokes)(None)

mouse_map = {
    '(%s) (%s) [(%s)]' % (' | '.join(single_click_commands),
                          ' | '.join(list(text_selectors.keys())),
                          ' | '.join(list(movement_targets.keys()))): SingleClickCommand,
}; vimmap.update(mouse_map)

common_names = {
    "dido" : "d$",
    "leader" : Key("%s" % LEADER),
}; vimmap.update(common_names)


ctx.keymap(vimmap)

