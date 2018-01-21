from talon.voice import Word, Context, Key, Rep, Str, press
from talon import ctrl
import string

alpha_alt = 'air bat cap die each fail gone harm sit jury crash look mad near odd pit quest red sun trap urge vest whale box yes zip'.split()
alnum = list(zip(alpha_alt, string.ascii_lowercase)) + [(str(i), str(i)) for i in range(0, 10)]

alpha = {}
alpha.update(dict(alnum))
alpha.update({'ship %s' % word: letter for word, letter in zip(alpha_alt, string.ascii_uppercase)})

alpha.update({'corey %s' % k: Key('ctrl-%s' % v) for k, v in alnum})
alpha.update({'commy %s' % k: Key('cmd-%s' % v) for k, v in alnum})
alpha.update({'commy ship %s' % k: Key('ctrl-shift-%s' % v) for k, v in alnum})
alpha.update({'alt %s' % k: Key('alt-%s' % v) for k, v in alnum})

mapping = {
    'semicolon': ';',
    r'new-line': '\n',
    r'new-paragraph': '\n\n',
}

def parse_word(word):
    word = word.lstrip('\\').split('\\', 1)[0]
    word = mapping.get(word, word)
    return word

def text(m):
    tmp = [str(s).lower() for s in m.dgndictation[0]._words]
    words = [parse_word(word) for word in tmp]
    Str(' '.join(words))(None)

def word(m):
    tmp = [str(s).lower() for s in m.dgnwords[0]._words]
    words = [parse_word(word) for word in tmp]
    Str(' '.join(words))(None)

def surround(by):
    def func(i, word, last):
        if i == 0: word = by + word
        if last: word += by
        return word
    return func

def rot13(i, word, _):
    out = ''
    for c in word.lower():
        if c in string.ascii_lowercase:
            c = chr((((ord(c) - ord('a')) + 13) % 26) + ord('a'))
        out += c
    return out

formatters = {
    'dunder':       (True,  lambda i, word, _: '__%s__' % word if i == 0 else word),
    'camel':        (True,  lambda i, word, _: word if i == 0 else word.capitalize()),
    'snake':        (True,  lambda i, word, _: word if i == 0 else '_'+word),
    'kebab':        (True,  lambda i, word, _: word if i == 0 else '-'+word),
    'dotword':      (True,  lambda i, word, _: word if i == 0 else '.'+word),
    'smash':        (True,  lambda i, word, _: word),
    'proper':       (True, lambda i, word, _: word.capitalize()),
    'title':        (False, lambda i, word, _: word.capitalize()),
    'allcaps':      (False, lambda i, word, _: word.upper()),
    'string':       (False, surround('"')),
    'soul string':  (False, surround("'")),
    'padded':       (False, surround(" ")),
    'rot thirteen': (False, rot13),
}

def FormatText(m):
    fmt = []
    for w in m._words:
        if isinstance(w, Word):
            fmt.append(w.word)
    words = [str(s).lower() for s in m.dgndictation[0]._words]

    tmp = []
    spaces = True
    for i, word in enumerate(words):
        word = parse_word(word)
        for name in reversed(fmt):
            smash, func = formatters[name]
            word = func(i, word, i == len(words)-1)
            spaces = spaces and not smash
        tmp.append(word)
    words = tmp

    sep = ' '
    if not spaces:
        sep = ''
    Str(sep.join(words))(None)

ctx = Context('input')

keymap = {}

# hacky ways for repeat commands that take numbers as variables
keymap.update({'%d work' % k: [Key('alt-backspace')]*k for k in range(1, 10)})
keymap.update({'%d chuck' % k: [Key('backspace')]*k for k in range(1, 10)})
keymap.update({'%d left' % k: [Key('left')]*k for k in range(1, 10)})
keymap.update({'%d right' % k: [Key('right')]*k for k in range(1, 10)})
keymap.update({'%d box' % k: ['x']*k for k in range(1, 10)})

keymap.update(alpha)
keymap.update({
    'say <dgndictation> [over]': text,
    'word <dgnwords>': word,
    '(%s)+ <dgndictation>' % (' | '.join(formatters)): FormatText,

    'tab':   Key('tab'),
    'left':  Key('left'),
    'right': Key('right'),
    'up':    Key('up'),
    'down':  Key('down'),

    'chuck': Key('backspace'),
    'work' : Key('alt-backspace'),

    'slap': Key('enter'),
    'slapper': [Key('cmd-right enter')],
    'skate': Key('esc'),
    'question': '?',
    'dash': '-',
    'plus': '+',
    'tilde': '~',
    '(bang | exclamation mark)': '!',
    'doll': '$',
    'downscore': '_',
    '(semi | semicolon)': ';',
    'colon': ':',
    'lacket': '[',
    'bracket': ']',
    'larry': '(',
    'perry': ')',
    'lace': '{',
    'brace': '}',
    'langle': '<',
    'rangle': '>',

    'star': '*',
    'hash': '#',
    'percent [sign]': '%',
    'flex': '^',
    'ash': '@',
    'ampersand': '&',
    'pipe': '|',

    'dubquote': '"',
    'quote': "'",
    'triple quote': "'''",
    'triple backtick': "```",
    '(dock | period)': '.',
    'conner': ',',
    'spamma': ', ',
    'space': ' ',
    'slash': '/',
    'backslash': '\\',

    'anvio' : Key('anvio'),
    'quake' : Key(' = '),

    'dot pie': '.py',

    'args': Key("() left"),
    'square' : Key("[] left"),
    'dish': Key('{} left'),
    'call' : Key("()"),
    'empty list': '[]',
    'empty dish': '{}',

    'state deaf': 'def ', 
    'state else if': 'elif ',
    'state if': 'if ',
    'state while': ['while ()', Key('left')],
    'state for': 'for ',
    'state import': 'import ',

    'comment py': '# ',

    'dunder in it': '__init__',

    'is equal to': ' == ',
    'equals': '=',

    'next window': Key('cmd-`'),
    'last window': Key('cmd-shift-`'),
    'next app': Key('cmd-tab'),
    'last app': Key('cmd-shift-tab'),

    'click': lambda x: ctrl.mouse_click(),

    # a bunch of common names that i use
    "vim our see" : Key("~/.vimrc"),
    "bash profile" : Key("~/.bash_profile"),
    "vim" : Key("vim"),
})

ctx.keymap(keymap)
