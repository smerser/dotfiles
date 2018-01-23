from talon.engine import engine

def listener(topic, m):
    print(topic, m)

engine.register('', listener)
def unload(): engine.unregister('', listener)
