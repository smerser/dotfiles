from talon.voice import Word, Context, Key, Rep, Str, press
from talon import ctrl
import string

alpha_alt = 'air bat cap die each fail gone harm sit jury crash look mad near odd pit quest red sun trap urge vest whale box yes zip'.split()
alnum = list(zip(alpha_alt, string.ascii_lowercase)) + [(str(i), str(i)) for i in range(0, 10)]

alpha = {}
alpha.update(dict(alnum))
alpha.update({'ship %s' % word: letter for word, letter in zip(alpha_alt, string.ascii_uppercase)})

alpha.update({'control %s' % k: Key('ctrl-%s' % v) for k, v in alnum})
alpha.update({'command %s' % k: Key('cmd-%s' % v) for k, v in alnum})
alpha.update({'command shift %s' % k: Key('ctrl-shift-%s' % v) for k, v in alnum})
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


keymap = {}
keymap.update(alpha)
keymap.update({
    'phrase <dgndictation> [over]': text,
    'word <dgnwords>': word,
    '(%s)+ <dgndictation>' % (' | '.join(formatters)): FormatText,

    'tab':   Key('tab'),
    'left':  Key('left'),
    'right': Key('right'),
    'up':    Key('up'),
    'down':  Key('down'),

    'chuck': Key('backspace'),

    'slap': Key('enter'),
    'slapper': [Key('cmd-right enter')],
    'skate': Key('esc'),
    'question [mark]': '?',
    '(minus | hyphen)': '-',
    'plus': '+',
    'tilde': '~',
    '(bang | exclamation mark)': '!',
    'doll': '$',
    'downscore': '_',
    '(semi | semicolon)': ';',
    'colon': ':',
    'lacket': '[',
    'bracket': ']',
    'larent': '(',
    'parent': ')',
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
    'triple backtick': "'''",
    '(dot | period)': '.',
    'conner': ',',
    'spamma': ', ',
    'space': ' ',
    'slash': '/',
    'backslash': '\\',

    # these are really for bash
    '(dot dot | dotdot)': '..',
    'cd': 'cd ',
    'our em': 'rm ',
    'run make durr': 'mkdir ',
    'run git': 'git ',
    'run git clone': 'git clone ',
    'run git diff': 'git diff ',
    'run git commit': 'git commit ',
    'run git push': 'git push ',
    'run git pull': 'git pull ',
    'run git status': 'git status ',
    'run git add': 'git add ',
    'run (them | vim)': 'vim ',
    'run ellis': 'ls\n',
    'dot pie': '.py',

    'args': ['()', Key('left')],
    'empty list': '[]',
    'empty dict': '{}',

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
    'call': '()',

    'new window': Key('cmd-n'),
    'next window': Key('cmd-`'),
    'last window': Key('cmd-shift-`'),
    'next app': Key('cmd-tab'),
    'last app': Key('cmd-shift-tab'),
    'next tab': Key('ctrl-tab'),
    'new tab': Key('cmd-t'),

    'click': lambda x: ctrl.mouse_click(),
})
