import pygame


class Camera:
    def __init__(self, screen):
        self.screen = screen
        self.delta_time = 0
        self.x = 0
        self.y = 0
        self.target = None

    def set_target(self, target):
        self.target = target

    def update(self, delta_time):
        self.delta_time = delta_time
        self.x = self.target.x - (self.screen.get_width() // 2) + (self.target.width // 2)
        self.y = self.target.y - (self.screen.get_height() // 2) + (self.target.height // 2)

    def display(self):
        self.screen.blit(pygame.Surface((0, 0)), (self.x, self.y))