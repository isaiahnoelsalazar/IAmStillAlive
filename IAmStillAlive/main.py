import asyncio
import pygame
from Camera import Camera
import Globals
from Scenario1 import Scenario1

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
delta_time = 0.1
camera = Camera(screen)


async def main():
    global delta_time

    ''' -------- INITIALIZATION -------- '''

    scenario1 = Scenario1(camera)
    running = True

    ''' -------- MAIN LOOP -------- '''

    while running:
        screen.fill((255, 255, 255))

        ''' -------- EVENTS -------- '''

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    Globals.up = True
                if event.key == pygame.K_a:
                    Globals.left = True
                if event.key == pygame.K_s:
                    Globals.down = True
                if event.key == pygame.K_d:
                    Globals.right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    Globals.up = False
                if event.key == pygame.K_a:
                    Globals.left = False
                if event.key == pygame.K_s:
                    Globals.down = False
                if event.key == pygame.K_d:
                    Globals.right = False
            if event.type == pygame.QUIT:
                running = False

        ''' -------- UPDATE -------- '''

        scenario1.update()
        camera.update(delta_time)

        ''' -------- DISPLAY -------- '''

        scenario1.display()
        camera.display()
        pygame.display.flip()
        delta_time = clock.tick(60) / 1000
        delta_time = max(0.001, min(0.1, delta_time))
        await asyncio.sleep(0)


asyncio.run(main())