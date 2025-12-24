import pygame


class Tile:
    def __init__(self, camera, x = 0, y = 0, image_path = None, width = 0, height = 0, color = (0, 0, 0)):
        self.camera = camera
        self.x = x
        self.y = y
        try:
            self.image = pygame.image.load(image_path).convert_alpha()
        except:
            self.image = None
        self.width = width
        self.height = height
        if self.image is not None:
            self.width = self.image.get_width()
            self.height = self.image.get_height()
        self.color = pygame.color.Color(color)

    def update(self):
        if self.image is not None:
            self.camera.screen.blit(self.image, (self.x - self.camera.x, self.y - self.camera.y))
        else:
            surface = pygame.Surface((self.width, self.height))
            surface.fill(self.color)
            self.camera.screen.blit(surface, (self.x - self.camera.x, self.y - self.camera.y))