class Engine(object):

    def __init__(self, map_):
        self.map = map_

    def start(self):
        current_scene = self.map.get_start_scene()
        while True:
            next_scene_name = current_scene.enter()
            current_scene = self.map.get_scene(next_scene_name)


class Map(object):

    def __init__(self, scenes, start):
        self.scenes = scenes
        self.start = start

    def get_scene(self, scene_name):
        if scene_name not in self.scenes:
            raise NotImplementedError('This scene ({}) does not exist'.format(scene_name))
        return self.scenes[scene_name]

    def get_start_scene(self):
        return self.get_scene(self.start)


class Scene(object):

    def enter(self):
        pass


class State(object):

    def __init__(self):
        pass


class Item(object):

    def __init__(self):
        pass
