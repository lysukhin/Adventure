class Engine(object):

    def __init__(self, map_):
        self.map = map_

    def start(self):
        current_scene = self.map.get_start_scene()
        while True:
            next_scene_name = current_scene.enter()
            current_scene = self.map.get_scene(next_scene_name)


class Map(object):

    def __init__(self, scenes, initial):
        self.scenes = scenes
        self.initial = initial

    def get_scene(self, scene_name):
        if scene_name not in self.scenes:
            raise NotImplementedError('This scene ({}) does not exist'.format(scene_name))
        return self.scenes[scene_name]

    def get_start_scene(self):
        return self.get_scene(self.initial)
