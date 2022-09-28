class Scene(object):

    def enter(self):
        pass


class Engine(object):

    def __init__(self,scene_map):
        pass
    
    def play(self):
        print("function play")

class Death(Scene):

    def enter(self):
        pass

class CentralCorridor(Scene):

    def enter(self):
        pass

class laserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass


class Map(object):

    def __init__(self, start_scene):
        #self.a = start_scene
        print(start_scene)

    def next_scene(self, Scene_name):
        print("this is next scene method")
        print(Scene_name)

    def opening_scene(self):
        pass


a_map = Map("cantral_corridor")
a_game = Engine(a_map)
a_game.play()
#a_game.next_scene("hero entery")