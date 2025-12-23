import pygame
from Entity import Entity


class Player(Entity):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load("resources/player.png").convert_alpha()
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.set_spawn()

    def set_spawn(self, x = 0, y = 0, speed = 2):
        self.x = x
        self.y = y
        self.speed = speed

    def update(self, delta_time):
        if self.up:
            self.y -= (60 * self.speed) * delta_time
        if self.down:
            self.y += (60 * self.speed) * delta_time
        if self.left:
            self.x -= (60 * self.speed) * delta_time
        if self.right:
            self.x += (60 * self.speed) * delta_time
        self.screen.blit(self.image, (self.x, self.y))