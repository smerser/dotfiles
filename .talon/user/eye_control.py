import eye
from user import eye2
from talon.voice import Word, Context, Key, Rep, Str, press

ctx = Context('eye_control')
ctx.keymap({
    'debug overlay':   lambda m: eye2.on_menu('User Eye Mouse >> Show Debug Overlay'),
    'mouser':          lambda m: eye2.on_menu('User Eye Mouse >> Control Mouse'),
    'camera overlay':  lambda m: eye.on_menu('Eye Tracking >> Show Camera Overlay'),
    'run calibration': lambda m: eye.on_menu('Eye Tracking >> Calibrate'),
})
