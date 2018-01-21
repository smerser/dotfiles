from talon.voice import Word, Context, Key, Rep, Str, press
from talon import ctrl
import string

def parse_word(word):
    word = word.lstrip('\\').split('\\', 1)[0]
    word = mapping.get(word, word)
    return word

def text(m):
    tmp = [str(s).lower() for s in m.dgndictation[0]._words]
    words = [parse_word(word) for word in tmp]
    Str(' '.join(words))(None)

ctx = Context('python', bundle='com.googlecode.iterm2', func=lambda app, win: '.py' in win.title)

pythonmap = {}
pythonmap.update({
    'def'          :  'def ',
    'loop'         :  'for ',
    'class'        :  'class ',
    "from"         :  Key("from "),
    "lint"           :  Key("in "),
    "import"       :  Key("import "),
    "sift"           :  Key("if "),
    "else"         :  Key("else"),
    "elif"         :  Key("elif "),
    "try"          :  Key("try "),
    "except"       :  Key("except "),
    "raise"        :  Key("raise "),
    "true"         :  Key("True"),
    "false"        :  Key("False"),
    'none'         :  Key("None"),
    'print'        :  Key("print() left"),
    "sum"          :  Key("sum("),
    "(len|length)" :  Key("len("),
    "tuple"        :  Key("tuple("),
    "is instance"  :  Key("isinstance("),
    "init"         :  Key("__init__("),
    "self"         :  Key("self"),
    "iter"         :  Key("iter"),
    "dunder"       :  Key("__"),
    "dunder main"  :  Key("__main__"),

    "upend" : Key("append"),

    "scipy" : Key("scipy"),
    "numpy" : Key("numpy"),

})

ctx.keymap(pythonmap)

def unload():
    ctx.disable()

