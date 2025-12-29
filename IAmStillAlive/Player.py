import pygame
from Entity import Entity
import Globals
import ScenarioManager


class Player(Entity):
    def __init__(self, camera):
        super().__init__()
        self.camera = camera
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.image = pygame.image.load("resources/player.png").convert_alpha()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.set_spawn()

    def set_spawn(self, x = 0, y = 0, speed = 2):
        self.x = x
        self.y = y
        self.speed = speed

    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.up = Globals.KEY_W
        self.down = Globals.KEY_S
        self.left = Globals.KEY_A
        self.right = Globals.KEY_D
        movement = (60 * self.speed) * self.camera.delta_time
        left_rect_movement = pygame.Rect(self.x - movement, self.y, self.width, self.height)
        right_rect_movement = pygame.Rect(self.x + movement, self.y, self.width, self.height)
        up_rect_movement = pygame.Rect(self.x, self.y - movement, self.width, self.height)
        down_rect_movement = pygame.Rect(self.x, self.y + movement, self.width, self.height)
        for tile in ScenarioManager.scenario_list[ScenarioManager.scenario_index].map_manager.map_list[ScenarioManager.scenario_list[ScenarioManager.scenario_index].map_manager.map_index].tile_list:
            if tile.is_solid:
                if left_rect_movement.colliderect(tile.rect):
                    self.left = False
                if right_rect_movement.colliderect(tile.rect):
                    self.right = False
                if up_rect_movement.colliderect(tile.rect):
                    self.up = False
                if down_rect_movement.colliderect(tile.rect):
                    self.down = False
        for object_item in ScenarioManager.scenario_list[ScenarioManager.scenario_index].map_manager.map_list[ScenarioManager.scenario_list[ScenarioManager.scenario_index].map_manager.map_index].object_list:
            if object_item.is_solid:
                if left_rect_movement.colliderect(object_item.rect):
                    self.left = False
                if right_rect_movement.colliderect(object_item.rect):
                    self.right = False
                if up_rect_movement.colliderect(object_item.rect):
                    self.up = False
                if down_rect_movement.colliderect(object_item.rect):
                    self.down = False
        if self.up:
            self.y -= movement
        if self.down:
            self.y += movement
        if self.left:
            self.x -= movement
        if self.right:
            self.x += movement

    def display(self):
        self.camera.screen.blit(self.image, (self.x - self.camera.x, self.y - self.camera.y))