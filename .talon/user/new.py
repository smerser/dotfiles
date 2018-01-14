from talon.voice import Word, Context, Key, Rep, Str, press

LEADER = 'space'

python_mappings = {
    "this is just a test" : Key("F"),
}

ctx.keymap(python_mappings)

def unload():
    ctx.disable()
