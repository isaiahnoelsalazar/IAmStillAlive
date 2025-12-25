from IAmStillAlive.Player import Player
from IAmStillAlive.Scenario import Scenario
from IAmStillAlive.Tile import Tile


class Scenario1(Scenario):
    def __init__(self, camera):
        super().__init__(camera)
        self.tile_list.append(
            Tile(
                camera=self.camera,
                x=96,
                y=0,
                width=48,
                height=48,
                is_solid=True
            )
        )
        self.tile_list.append(
            Tile(
                camera=self.camera,
                x=-96,
                y=0,
                width=48,
                height=48,
                is_solid=True
            )
        )
        player = Player(self.camera)
        self.entity_list.append(player)
        self.camera.set_target(player)