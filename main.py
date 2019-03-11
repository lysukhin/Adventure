from modules import *


def run():
    scenes = {'cockpit': Cockpit(), 'end': End()}
    map_ = Map(scenes, initial='cockpit')
    engine = Engine(map_)
    engine.start()


if __name__ == '__main__':
    run()
