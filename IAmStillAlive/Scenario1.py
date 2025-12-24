from Scenario import Scenario
from Player import Player
from Tile import Tile

class Scenario1(Scenario):
    def __init__(self, camera):
        super().__init__(camera)
        self.player = Player(camera)
        self.tile_list.append(
            Tile(
                camera=camera,
                x=96,
                y=0,
                width=48,
                height=48,
                is_solid=True
            )
        )
        self.camera.set_target(self.player)

    def update(self):
        super().update()
        self.player.update()

    def display(self):
        super().display()
        self.player.display()