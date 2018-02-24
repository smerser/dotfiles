from talon.voice import Word, Context, Key, Rep, Str, press
ctx = Context('chrome', bundle='com.google.Chrome')

from .vim import common_to_bash

chromemap = {}

chromemap.update(common_to_bash)

chromemap.update({'%d ruff' % k: [Key('J')]*k for k in range(1, 10)})
chromemap.update({'%d buff' % k: [Key('K')]*k for k in range(1, 10)})


chromemap.update({
    "go to amazon" : [Key("escape escape cmd-l"), "amazon.com", Key("enter")],
    "go to wikipedia" : [Key("escape escape cmd-l"), "wikipedia.com", Key("enter")],
    "go to github" : [Key("escape escape cmd-l"), "github.com", Key("enter")],
    "go to facebook" : [Key("escape escape cmd-l"), "facebook.com", Key("enter")],
    "go to gmail" : [Key("escape escape cmd-l"), "gmail.com", Key("enter")],
    "go to google" : [Key("escape escape cmd-l"), "google.com", Key("enter")],
    "go to read it" : [Key("escape escape cmd-l"), "reddit.com", Key("enter")],
    "go to drive" : [Key("escape escape cmd-l"), "drive.google.com", Key("enter")],
    "go to netflix" : [Key("escape escape cmd-l"), "netflix.com", Key("enter")],
    "go to lab fiesta" : [Key("escape escape cmd-l"), "https://github.com/merenlab/lab-fiesta", Key("enter")],
    })

chromemap.update({
    'more' : 'd',
    'less' : 'u',
    'lesser' : Key('alt-up'),
    'mortar' : Key('alt-down'),
    'out' : [Key('tab')]*25,
    'dark mode' : Key('alt-shift-d'),
    'zoom in' : Key('cmd-='),
    'zoom out' : Key('cmd+-'),
    'pan left' : 'h'*4,
    'pan right' : 'l'*4,
    'nex' : 'n',
    'bex' : 'N',
    'tab search' : 'T',
    'ruff' : Key("escape J"),
    'buff' : Key("escape K"),
    'back' : 'H',
    'forward' : 'L',
    'refresh' : 'cmd-r',
    })

ctx.keymap(chromemap)

def unload():
    ctx.disable()

