from modules import *
from scenes import *


def run():
    scenes = {'start': Start(),
              'cockpit': Cockpit(),
              'end': End()}
    map_ = Map(scenes, initial='start')
    engine = Engine(map_)
    engine.start()


if __name__ == '__main__':
    run()
