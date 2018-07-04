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

ctx = Context('python', bundle='com.googlecode.iterm2', func=lambda app, win: any(s in win.title for s in ('.py', 'IPython', 'Snakefile')))

pythonmap = {}

basicpython  = {
    'def'          : 'def ',
    'loop'         : 'for ',
    'class'        : 'class ',
    'return'       : 'return ',
    "from"         : "from ",
    "lint"         : " in ",
    "andy"         : " and ",
    "sass"         : " as ",
    "range"        : ["range()", Key("left")],
    "import"       : "import ",
    "sift"         : "if ",
    "sift not"     : "if not ",
    "andy not"     : " and not ",
    "else"         : "else",
    "elif"         : "elif ",
    "try"          : ["try: ", Key("enter"), Key("tab")],
    "except"       : "except",
    "finally"      : ["finally: ", Key("enter"), Key("tab")],
    "raise"        : "raise ",
    "true"         : "True",
    "false"        : "False",
    'none'         : "None",
    'print'        : ["print()", Key("left")],
    'open'         : ["open()", Key("left")],
    'sum'          : ["sum()", Key("left")],
    'len'          : ["len()", Key("left")],
    "tupple"       : ["tuple()", Key("left")],
    "is instance"  : ["isinstance()", Key("left")],
    "init"         : ["__init__()", Key("left")],
    "upend"        : ["append()", Key("left")],
    "vars"         : ["vars()", Key("left")],
    "dir"          : ["dir()", Key("left")],
    "self"         : "self",
    "iter"         : "iter",
    "dunder"       : "__",
    "dunder in it" : "__init__",
    "dunder main"  : "__main__",

    "integer"      : "int",
    "float"        : "float",
    "string"       : "str",

    "os"           : "os",
}

pandasmap = {

    "loke" : ["loc[]", Key("left")],
    "iloke" : ["iloc[]", Key("left")],

}


pythonmap.update(basicpython)
pythonmap.update(pandasmap)


ctx.keymap(pythonmap)
