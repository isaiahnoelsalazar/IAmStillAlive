from Player import Player
from Scenario import Scenario
from Tile import Tile


class Scenario2(Scenario):
    def __init__(self, camera):
        super().__init__(camera)
        self.map_manager.load(1)
        player = Player(self.camera)
        player.set_spawn(
            x = 144,
            y = 144
        )
        self.entity_list.append(player)
        self.camera.set_target(player)