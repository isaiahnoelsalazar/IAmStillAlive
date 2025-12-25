from IAmStillAlive.Player import Player
from IAmStillAlive.Tile import Tile

entity_list = []
tile_list = []


def start(camera):
    player = Player(camera)
    entity_list.append(player)
    tile_list.append(
        Tile(
            camera=camera,
            x=96,
            y=0,
            width=48,
            height=48,
            is_solid=True
        )
    )
    camera.set_target(player)


def update():
    for entity in entity_list:
        entity.update()


def display():
    for tile in tile_list:
        tile.display()
    for entity in entity_list:
        entity.display()