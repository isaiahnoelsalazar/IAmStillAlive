import pygame
from Entity import Entity
import Globals


class Player(Entity):
    def __init__(self, camera):
        super().__init__()
        self.camera = camera
        self.image = pygame.image.load("resources/player.png").convert_alpha()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.set_spawn()

    def set_spawn(self, x = 0, y = 0, speed = 2):
        self.x = x
        self.y = y
        self.speed = speed

    def update(self):
        if Globals.up:
            self.y -= (60 * self.speed) * self.camera.delta_time
        if Globals.down:
            self.y += (60 * self.speed) * self.camera.delta_time
        if Globals.left:
            self.x -= (60 * self.speed) * self.camera.delta_time
        if Globals.right:
            self.x += (60 * self.speed) * self.camera.delta_time

    def display(self):
        self.camera.screen.blit(self.image, (self.x - self.camera.x, self.y - self.camera.y))