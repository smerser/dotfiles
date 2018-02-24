import eye
import time
from talon import ctrl, tap
from talon.voice import Context, Key
ctx = Context('mouse')

x, y = ctrl.mouse_pos()
mouse_history = [(x, y, time.time())]
force_move = None

def on_move(_, e):
    mouse_history.append((e.x, e.y, time.time()))
    if force_move:
        e.x, e.y = force_move
        return True
tap.register(tap.MMOVE, on_move)

def click_pos(m):
    word = m._words[0]
    start = (word.start + min((word.end - word.start) / 2, 0.100)) / 1000.0
    diff, pos = min([(abs(start - pos[2]), pos) for pos in mouse_history])
    return pos[:2]

def delayed_click(m, button=0, times=1, down=None, up=None):
    old = eye.config.control_mouse
    eye.config.control_mouse = False
    x, y = click_pos(m)
    ctrl.mouse(x, y)
    ctrl.mouse_click(x, y, button=button, down=down, up=up, times=times, wait=16000)
    time.sleep(0.032)
    eye.config.control_mouse = old

def delayed_right_click(m):
    delayed_click(m, button=1)

def delayed_dubclick(m):
    delayed_click(m, button=0, times=2)

def delayed_tripclick(m):
    delayed_click(m, button=0, times=3)

def delayed_mouse_drag(m):
    delayed_click(m, button=0, times=1, down=True)

def delayed_mouse_release(m):
    delayed_click(m, button=0, times=1, up=True)

keymap = {
    'righty': delayed_right_click,
    'click': delayed_click,
    'drip': delayed_dubclick,
    'trick': delayed_tripclick,
    'press': delayed_mouse_drag,
    'lease': delayed_mouse_release,
    'cheese': [delayed_mouse_release, Key("backspace")],

    # combinations of mouse and keypresses
    "drickop" : [delayed_dubclick, Key("cmd-c")],
    "trickop" : [delayed_tripclick, Key("cmd-c")],

    'screencop' : [Key('cmd-shift-ctrl-4'), delayed_mouse_drag],
    'screenshot' : [Key('cmd-shift-4'), delayed_mouse_drag],

}
ctx.keymap(keymap)

#def unload():
#    global mouse_history
#    ctx.unload()
#    tap.unregister(tap.MMOVE, on_move)
#    mouse_history = []
