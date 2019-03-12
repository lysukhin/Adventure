from sys import exit


class Engine(object):

    def __init__(self, map_):
        self.map = map_

    def start(self):
        current_scene = self.map.get_start_scene()
        while True:
            next_scene_name = current_scene.enter()
            current_scene = self.map.get_scene(next_scene_name)


class Scene(object):

    def enter(self):
        pass


class End(Scene):

    def enter(self):
        message = "GAME OVER"
        print(message)
        exit(1)


class Cockpit(Scene):

    def enter(self):
        title = """███████╗██████╗  █████╗  ██████╗███████╗    
██╔════╝██╔══██╗██╔══██╗██╔════╝██╔════╝    
███████╗██████╔╝███████║██║     █████╗      
╚════██║██╔═══╝ ██╔══██║██║     ██╔══╝      
███████║██║     ██║  ██║╚██████╗███████╗    
╚══════╝╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝    
                                            
 ██████╗ ██╗   ██╗███████╗███████╗████████╗ 
██╔═══██╗██║   ██║██╔════╝██╔════╝╚══██╔══╝ 
██║   ██║██║   ██║█████╗  ███████╗   ██║    
██║▄▄ ██║██║   ██║██╔══╝  ╚════██║   ██║    
╚██████╔╝╚██████╔╝███████╗███████║   ██║    
 ╚══▀▀═╝  ╚═════╝ ╚══════╝╚══════╝   ╚═╝    """
        print(title)
        message = "= " * 25 + '\n' + \
                  "You are the pilot of a spaceship. The big one." + '\n' + \
                  "Your ship is about to waste it\'s last gallon of fuel." + '\n' + \
                  "You see two planets ahead: one is blue, other is green." + '\n' + \
                  "Which one will you choose to land on?"
        print(message)

        action = input('Your action >: ')
        if action == 'blue':
            message = "You choose to land on a blue planet." + '\n' + \
                      "The surface seems to be inhabitable at first glance." + '\n' + \
                      "However, after leaving the ship you get caught in the trap by blue-skinned aliens." + '\n' + \
                      "You are raped to death."
            print(message)
            return "end"
        elif action == 'green':
            message = "You choose to land on a green planet." + '\n' + \
                      "The surface seems to be inhabitable at first glance." + '\n' + \
                      "However, after leaving the ship you get caught in the trap by green-skinned aliens." + '\n' + \
                      "You are raped to death."
            print(message)
            return "end"
        else:
            message = "Your action is unacceptable! Try again."
            print(message)
            return "cockpit"


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
