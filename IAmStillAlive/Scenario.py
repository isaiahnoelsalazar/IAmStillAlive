from MapManager import MapManager


class Scenario:
    def __init__(self, camera):
        self.camera = camera
        self.map_manager = MapManager(camera)
        self.entity_list = []

    def update(self):
        for entity in self.entity_list:
            entity.update()

    def display(self):
        self.map_manager.display()
        for entity in self.entity_list:
            entity.display()