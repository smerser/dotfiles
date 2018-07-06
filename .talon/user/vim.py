from talon.voice import Word, Context, Key, Rep, Str, press
from .mouse import initial_pos_click
from .mouse import final_pos_click
from .mouse import advanced_click
from .std import punctuation
from .std import lower_upper_digits
import time
ctx = Context('vim', bundle='com.googlecode.iterm2', func=lambda app, win: 'vim' in win.title)

vimmap = {}

LEADER = 'space'

# hacky ways for repeat commands that take numbers as variables (there is another one of these in std)
vimmap.update({'%d buff' % k: [Key('escape')] + [Key('shift-right'), lambda m: time.sleep(0.1)]*k for k in range(2, 10)})
vimmap.update({'%d ruff' % k: [Key('escape')] + [Key('shift-left'), lambda m: time.sleep(0.1)]*k for k in range(2, 10)})
vimmap.update({'%d box' % k: ['x']*k for k in range(2, 10)})
vimmap.update({'%d undo' % k: ['u']*k for k in range(2, 10)})
vimmap.update({'%d redo' % k: [Key('ctrl-r')]*k for k in range(2, 10)})

# I share this with bash.py (I have vim-style bash -- see ~/.inputrc)
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
    'flexy' : '0',

    # line movement
    'fly' : 'G',

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
    'show me'               :  lambda m: press('ctrl-space', wait=16000), # does not work in iterm :(
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
    'cancel hits' :  ["/asde", Key("enter")],
    'nex'         :  Key("n"),
    'bex'         :  Key("N"),
    'sore'        :  [":s///g"] + [Key("left")]*3,
    'globsore'    :  [":%s///g"] + [Key("left")]*3,

    'para' : [Key("escape"), "o", Key("enter")],
}; vimmap.update(primitive_commands)

# Key("left"), Key("right") used to maintain column position when escaping immediately after `o` or `O`
make_marker = lambda marker_key, *args: [Key("left"), Key("right"), Key("escape"), Str("m%s" % marker_key)]

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
}

target_required_text_selectors = {
    "fail"       : "f",
    "til"        : "t",
    "gif"        : "F",
    "lit"        : "T",
}

teleport_commands = [
    'psych',
    'steal',
    'slice',
    'kill',
    'kip',
    'phipps',
    'nothing',
]

here_to_here_commands = [
    'phipps',
    'bar',
    'kill',
    'steal',
    'psych',
]

movement_targets = lower_upper_digits.copy()
movement_targets.update(punctuation)

def TeleportCommand(m):
    '''Teleport commands are a group of commands that carry out keystrokes both at the mouse\'s position
       AND the cursor's position at the time of first utterance. It is called teleport because the cursor
       'teleports' between these two positions. The general flow of this function is:

            1. make a marker at the cursor's position
            2. click where the mouse was at the start of the utterance
            3. carry out keystrokes for the command (e.g. select text, etc)
            4. optionally return to the marker and carry out more keystrokes (e.g. paste text, etc)

       The concept of these commands was seeded by the command `psych`, which is demonstrated in this
       video: https://www.youtube.com/watch?v=F2KEnQl7d2s
    '''
    utterance = []
    for w in m._words:
        utterance.append(w.word)

    marker_key = 't' # marks original cursor position

    if utterance[0] == "psych":
        preprend = 'y' # yank
        append = "'{}pa".format(marker_key) # return to marker, paste, re-enter insert mode

    elif utterance[0] == "steal":
        preprend = 'y' # yank
        append = "'{}".format(marker_key) # return to marker

    elif utterance[0] == "slice":
        preprend = 'd' # delete
        append = "'{}pa".format(marker_key) # return to marker, paste, re-enter insert mode

    elif utterance[0] == "kill":
        preprend = 'd' # delete
        append = "'{}".format(marker_key) # return to marker

    elif utterance[0] == "kip":
        preprend = 'c' # change
        append = ""

    elif utterance[0] == "phipps":
        preprend = 'v' # select
        append = ""

    else:
        raise Exception("`{}` is not a keyword understood by TeleportCommand".format(utterance[0]))

    marker_operations = make_marker(marker_key, m)
    for action in marker_operations:
        action(m)
    time.sleep(0.1)
    initial_pos_click(m)
    del utterance[0] # remove teleport operator from utterance

    movement_strokes = text_selectors.get(' '.join(utterance), False)
    if not movement_strokes:
        # movement key was also uttered. fish it out (assumes no more than 2 words, e.g. "ship air")
        if movement_targets.get(' '.join(utterance[-2:]), False):
            movement_strokes = target_required_text_selectors[' '.join(utterance[:-2])] + movement_targets[' '.join(utterance[-2:])]
        else:
            movement_strokes = target_required_text_selectors[' '.join(utterance[:-1])] + movement_targets[utterance[-1]]
    movement_strokes = preprend + movement_strokes + append
    Str(movement_strokes)(None)


def HereToHereCommand(m):
    '''`Here-to-here` commands select and sometimes operate on a text selection defined by where the
       mouse is at the start and end of the utterance. In this sense the user sweeps with their eyes
       the text selection as they utter `<command_prefix> here to here`. They can also use
       `<command_prefix> to here` to use the starting cursor position as the first text selection
       point, or `<command_prefix> here` to select either a single character or line.'''
    utterance = []
    for w in m._words:
        utterance.append(w.word)

    marker1 = 't' # original cursor pos
    marker2 = 'y' # position of first click
    marker3 = 'u' # position of second click

    if utterance[0] == 'phipps':
        selection_type = "v"
        movements = "'{}".format(marker3)
        strokes = ""
        append = ""

    elif utterance[0] == 'bar':
        selection_type = "V"
        movements = "'{}".format(marker3)
        strokes = ""
        append = ""

    elif utterance[0] == 'kill':
        selection_type = "V"
        movements = "'{}".format(marker3)
        strokes = "d"
        append = "'{}".format(marker1)

    elif utterance[0] == 'steal':
        selection_type = "V"
        movements = "'{}".format(marker3)
        strokes = "y"
        append = "'{}".format(marker1)

    elif utterance[0] == 'psych':
        selection_type = "V"
        movements = "'{}".format(marker3)
        strokes = "y"
        append = "'{}p".format(marker1)

    elif utterance[0] == 'psych':
        selection_type = "V"
        movements = "'{}".format(marker3)
        strokes = "y"
        append = "'{}p".format(marker1)

    else:
        raise Exception("`{}` is not a keyword understood by HereToHereCommand".format(utterance[0]))

    # here-to-here command
    if len(utterance) > 2 and utterance[-3] == 'here':
        marker_operations = make_marker(marker1, m)
        for action in marker_operations:
            action(m)
        time.sleep(0.05)

        final_pos_click(m)
        marker_operations = make_marker(marker3, m)
        for action in marker_operations:
            action(m)
        time.sleep(0.05)

        initial_pos_click(m)
        Str(selection_type + movements + strokes + append)(None)

    # to-here command
    elif utterance[-2] == 'to':
        marker_operations = make_marker(marker1, m)
        for action in marker_operations:
            action(m)
        time.sleep(0.05)

        final_pos_click(m)
        marker_operations = make_marker(marker3, m)
        for action in marker_operations:
            action(m)
        time.sleep(0.05)

        return_to_cursor = "'{}".format(marker1)
        Str(return_to_cursor + selection_type + movements + strokes + append)(None)

    # here command
    elif utterance[-1] == 'here':
        marker_operations = make_marker(marker1, m)
        for action in marker_operations:
            action(m)
        time.sleep(0.05)

        initial_pos_click(m)
        Str(selection_type + strokes + append)(None)


# everything mouse-related
mouse_map = {
    '(%s) ((%s) | (%s) [(%s)])' % (' | '.join(teleport_commands),
                                   ' | '.join(list(text_selectors.keys())),
                                   ' | '.join(list(target_required_text_selectors.keys())),
                                   ' | '.join(list(movement_targets.keys()))): TeleportCommand,
    '(%s) (here to here | to here | here)' % (' | '.join(here_to_here_commands)): HereToHereCommand,
}; vimmap.update(mouse_map)


common_names = {
    "dido" : "d$",
    "leader" : Key("%s" % LEADER),
}; vimmap.update(common_names)


ctx.keymap(vimmap)

