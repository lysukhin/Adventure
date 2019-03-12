from sys import exit

from utils import *


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


class Start(object):

    def enter(self):
        message = ["""
        ███████╗██████╗  █████╗  ██████╗███████╗    
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
         ╚══▀▀═╝  ╚═════╝ ╚══════╝╚══════╝   ╚═╝
         """]
        print_message(message, cls=True)
        return "cockpit"


class End(Scene):

    def enter(self):
        message = ["GAME OVER"]
        print_message(message, cls=False)
        exit(1)


class Cockpit(Scene):

    def enter(self):
        message = ["You are the pilot of a spaceship. The big one.",
                   "Your ship is about to waste it\'s last gallon of fuel.",
                   "You see two planets ahead: one is blue, other is green.",
                   "Which one will you choose to land on?"]
        print_message(message)

        action = input('Your action >: ')
        if action == 'blue':
            message = ["You choose to land on a blue planet.",
                       "The surface seems to be inhabitable at first glance.",
                       "However, after leaving the ship you get caught in the ",
                       "trap by blue-skinned aliens.",
                       "You are raped to death."]
            print_message(message)
            return "end"
        elif action == 'green':
            message = ["You choose to land on a green planet.",
                       "The surface seems to be inhabitable at first glance.",
                       "However, after leaving the ship you get caught in the ",
                       "trap by green-skinned aliens.",
                       "You are raped to death."]
            print_message(message)
            return "end"
        else:
            message = ["Your action is unacceptable! Try again."]
            print_message(message)
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
