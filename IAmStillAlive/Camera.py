import math
import pygame


class Camera:
    def __init__(self, screen):
        self.screen = screen
        self.delta_time = 0
        self.x = 0
        self.y = 0
        self.camera_aim_arrow_image = pygame.image.load("resources/blue_arrow.png").convert_alpha()
        self.new_camera_aim_arrow_image = pygame.transform.rotate(self.camera_aim_arrow_image, 0)
        self.camera_aim_arrow_image_rect = self.new_camera_aim_arrow_image.get_rect(center = ((self.screen.get_width() / 2), (self.screen.get_height() / 2)))
        self.target = None

    def set_target(self, target):
        self.target = target

    def update(self, delta_time):
        self.delta_time = delta_time
        self.x = self.target.x - (self.screen.get_width() // 2) + (self.target.width // 2)
        self.y = self.target.y - (self.screen.get_height() // 2) + (self.target.height // 2)

        mouse_x, mouse_y = pygame.mouse.get_pos()
        dx = mouse_x - (self.screen.get_width() / 2)
        dy = mouse_y - (self.screen.get_height() / 2)
        angle_radians = math.atan2(dy, dx)
        angle_degrees = -math.degrees(angle_radians)
        self.new_camera_aim_arrow_image = pygame.transform.rotate(self.camera_aim_arrow_image, angle_degrees - 90)
        self.camera_aim_arrow_image_rect = self.new_camera_aim_arrow_image.get_rect(center = ((self.screen.get_width() / 2), (self.screen.get_height() / 2)))

    def display(self):
        self.screen.blit(self.new_camera_aim_arrow_image, self.camera_aim_arrow_image_rect)
        self.screen.blit(pygame.Surface((0, 0)), (self.x, self.y))