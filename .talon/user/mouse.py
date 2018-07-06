#import eye
from user import eye2 as eye
import time
from talon import ctrl, tap
from talon.voice import Context, Key
ctx = Context('mouse')

x, y = ctrl.mouse_pos()
mouse_history = [(x, y, time.time())]
force_move = None

def on_move(typ, e):
    mouse_history.append((e.x, e.y, time.time()))
    if force_move:
        e.x, e.y = force_move
        return True
tap.register(tap.MMOVE, on_move)

def get_initial_mouse_pos(m):
    word = m._words[0] # first word in utterance
    start = (word.start + min((word.end - word.start) / 2, 0.100)) / 1000.0 # add a little time
    diff, pos = min([(abs(start - pos[2]), pos) for pos in mouse_history])
    return pos[:2]

def get_final_mouse_pos(m):
    word = m._words[-1] # last word in utterance
    #start = (word.start + (word.end - word.start)/2) / 1000.0 # add a little time
    start = word.start / 1000.0 # feels more natural to timestamp the start of last word
    diff, pos = min([(abs(start - pos[2]), pos) for pos in mouse_history])
    return pos[:2]

def initial_pos_click(m, button=0, times=1, down=None, up=None):
    old = eye.config.control_mouse
    eye.config.control_mouse = False
    x, y = get_initial_mouse_pos(m)
    ctrl.mouse(x, y)
    ctrl.mouse_click(x, y, button=button, down=down, up=up, times=times, wait=16000)
    time.sleep(0.032)
    eye.config.control_mouse = old

def final_pos_click(m, button=0, times=1, down=None, up=None):
    old = eye.config.control_mouse
    eye.config.control_mouse = False
    x, y = get_final_mouse_pos(m)
    ctrl.mouse(x, y)
    ctrl.mouse_click(x, y, button=button, down=down, up=up, times=times, wait=16000)
    time.sleep(0.032)
    eye.config.control_mouse = old

def initial_pos_right_click(m):
    initial_pos_click(m, button=1)

def initial_pos_dubclick(m):
    initial_pos_click(m, button=0, times=2)

def initial_pos_tripclick(m):
    initial_pos_click(m, button=0, times=3)

def initial_pos_mouse_drag(m):
    initial_pos_click(m, button=0, times=1, down=True)

def initial_pos_dubmouse_drag(m):
    initial_pos_click(m, button=0)
    initial_pos_click(m, button=0, times=1, down=True)

def initial_pos_mouse_release(m):
    initial_pos_click(m, button=0, times=1, up=True)

def mouse_drag(m):
    x, y = get_initial_mouse_pos(m)
    ctrl.mouse_click(x, y, down=True)

def mouse_release(m):
    x, y = get_initial_mouse_pos(m)
    ctrl.mouse_click(x, y, up=True)

def advanced_click(button, click_func, *mods, **kwargs):

    def click(e):
        for key in mods:
            ctrl.key_press(key, down=True)
        click_func(e)
        for key in mods[::-1]:
            ctrl.key_press(key, up=True)

    return click

keymap = {
    'righty'     : initial_pos_right_click,
    'click'      : initial_pos_click,
    'rick'       : advanced_click(0, initial_pos_click, 'ctrl'),
    'drip'       : initial_pos_dubclick,
    'trick'      : initial_pos_tripclick,
    'press'      : initial_pos_mouse_drag,
    'dress'      : initial_pos_dubmouse_drag,
    'lease'      : initial_pos_mouse_release,
    'leach'      : [initial_pos_mouse_release, Key("backspace")],
    'lickop'     : [initial_pos_mouse_release, Key("cmd-c")],

    "drickop"    : [initial_pos_dubclick, Key("cmd-c")],
    "trickop"    : [initial_pos_tripclick, Key("cmd-c")],

    'screencop'  : [Key('cmd-shift-ctrl-4'), initial_pos_mouse_drag],
    'screenshot' : [Key('cmd-shift-4'), initial_pos_mouse_drag],
}

ctx.keymap(keymap)
