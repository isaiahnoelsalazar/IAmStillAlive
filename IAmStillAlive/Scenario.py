class Scenario:
    def __init__(self, camera):
        self.camera = camera
        self.tile_list = []
        self.entity_list = []

    def update(self):
        for entity in self.entity_list:
            entity.update()

    def display(self):
        for tile in self.tile_list:
            tile.display()
        for entity in self.entity_list:
            entity.display()