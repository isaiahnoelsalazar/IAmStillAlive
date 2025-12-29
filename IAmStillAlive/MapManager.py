import pygame
from Map import Map
from Tile import Tile
from GameObject import GameObject


class MapManager:
    def __init__(self, camera):
        self.map_index = -1
        self.map_list = []
        with open("maps/map_list", "r") as m:
            for mt in m.readlines():
                tilemap_array = []
                new_tile_list = []
                objectmap_array = []
                new_object_list = []
                with open(f"maps/{mt.strip().split("+")[0]}", "r") as map_data:
                    for d in map_data.readlines():
                        tilemap_array.append(d)
                with open(f"maps/{mt.strip().split("+")[1]}", "r") as tile_data:
                    for d in tile_data.readlines():
                        new_tile_list.append(d)
                with open(f"maps/{mt.strip().split("+")[2]}", "r") as objectmap_data:
                    for d in objectmap_data.readlines():
                        objectmap_array.append(d)
                with open(f"maps/{mt.strip().split("+")[3]}", "r") as object_list_data:
                    for d in object_list_data.readlines():
                        new_object_list.append(d)
                full_map_data = Map()
                for a in range(len(tilemap_array)):
                    for b in range(len(tilemap_array[a].split(","))):
                        tile = Tile(
                            camera = camera,
                            image_path = f"resources/{new_tile_list[int(tilemap_array[a].split(",")[b])].replace(".", "")}.png"
                        )
                        if new_tile_list[int(tilemap_array[a].split(",")[b])].endswith("."):
                            tile.is_solid = True
                        tile.x = int(b) * tile.width
                        tile.y = int(a) * tile.height
                        tile.rect = pygame.Rect(tile.x, tile.y, tile.width, tile.height)
                        full_map_data.tile_list.append(tile)
                for a in range(len(objectmap_array)):
                    for b in range(len(objectmap_array[a].split(","))):
                        object_check = int(objectmap_array[a].split(",")[b]) - 1
                        if object_check >= 0:
                            game_object = GameObject(
                                camera = camera,
                                image_path = f"resources/{new_object_list[int(objectmap_array[a].split(",")[b]) - 1].replace(".", "")}.png"
                            )
                            if new_object_list[int(objectmap_array[a].split(",")[b]) - 1].endswith("."):
                                game_object.is_solid = True
                            game_object.x = int(b) * game_object.width
                            game_object.y = int(a) * game_object.height
                            game_object.rect = pygame.Rect(game_object.x, game_object.y, game_object.width, game_object.height)
                            full_map_data.object_list.append(game_object)
                self.map_list.append(full_map_data)

    def load(self, index):
        self.map_index = index

    def display(self):
        for tile in self.map_list[self.map_index].tile_list:
            tile.display()
        for object_item in self.map_list[self.map_index].object_list:
            object_item.display()