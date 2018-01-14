from talon.voice import Word, Context, Key, Rep, Str, press
from talon import ctrl
import string

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

pythonmap = {}
pythonmap.update({
    'google <dgndictation> [over]' : text,

    'def'                          : 'def ',
    'class'                          : 'class ',
    "import"                       : Key("import "),
    "if"                           : Key("if "),
    "else"                           : Key("else"),
    "elif"                           : Key("elif "),
    "try"                           : Key("try "),
    "except"                           : Key("except "),
    "raise"                           : Key("raise "),
    "true"                         : Key("True"),
    "false"                        : Key("False"),
    'none'                         : Key("None"),
    'print line'                        : Key("print() left"),
    "sum"                          : Key("sum("),
    "(len|length)"                 : Key("len("),
    "tuple"                        : Key("tuple("),
    "is instance"                  : Key("isinstance("),
    "init"                         : Key("__init__("),
    "self"                         : Key("self"),
    "iter items"                   : Key(".iteritems("),
    "dunder"                       : Key("__"),
    "dunder main"                  : Key("__main__"),
})

