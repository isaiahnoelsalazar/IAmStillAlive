from Map import Map
from Tile import Tile


class MapManager:
    def __init__(self, camera):
        self.map_index = -1
        self.map_list = []
        with open("maps/map_list", "r") as m:
            for mt in m.readlines():
                map_array = []
                tilemap_list = []
                with open(f"maps/{mt.strip().split("+")[0]}", "r") as map_data:
                    for d in map_data.readlines():
                        map_array.append(d)
                with open(f"maps/{mt.strip().split("+")[1]}", "r") as tile_data:
                    for d in tile_data.readlines():
                        tilemap_list.append(d)
                full_map_data = Map()
                for a in range(len(map_array)):
                    for b in range(len(map_array[a].split(","))):
                        tile = Tile(
                            camera = camera,
                            image_path = f"resources/{tilemap_list[int(map_array[a].split(",")[b])]}.png"
                        )
                        tile.x = int(b) * tile.width
                        tile.y = int(a) * tile.height
                        full_map_data.tile_list.append(tile)
                self.map_list.append(full_map_data)

    def load(self, index):
        self.map_index = index

    def display(self):
        for tile in self.map_list[self.map_index].tile_list:
            tile.display()