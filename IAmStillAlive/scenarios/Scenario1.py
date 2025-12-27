# from IAmStillAlive.Player import Player
# from IAmStillAlive.Scenario import Scenario

''' -------- FOR REBUILD -------- '''

from Player import Player
from Scenario import Scenario
from Tile import Tile


class Scenario1(Scenario):
    def __init__(self, camera):
        super().__init__(camera)
        self.map_manager.load(0)
        player = Player(self.camera)
        self.entity_list.append(player)
        self.camera.set_target(player)