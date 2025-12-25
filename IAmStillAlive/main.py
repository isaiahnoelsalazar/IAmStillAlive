import asyncio
import pygame
from Camera import Camera
import Globals
import ScenarioManager

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
delta_time = 0.1
camera = Camera(screen)


async def main():
    global delta_time

    ''' -------- INITIALIZATION -------- '''

    ScenarioManager.start(camera)
    running = True

    ''' -------- MAIN LOOP -------- '''

    while running:
        screen.fill((255, 255, 255))

        ''' -------- EVENTS -------- '''

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    Globals.KEY_W = True
                if event.key == pygame.K_a:
                    Globals.KEY_A = True
                if event.key == pygame.K_s:
                    Globals.KEY_S = True
                if event.key == pygame.K_d:
                    Globals.KEY_D = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    Globals.KEY_W = False
                if event.key == pygame.K_a:
                    Globals.KEY_A = False
                if event.key == pygame.K_s:
                    Globals.KEY_S = False
                if event.key == pygame.K_d:
                    Globals.KEY_D = False
            if event.type == pygame.QUIT:
                running = False

        ''' -------- UPDATE -------- '''

        ScenarioManager.update()
        camera.update(delta_time)

        ''' -------- DISPLAY -------- '''

        ScenarioManager.display()
        camera.display()
        pygame.display.flip()
        delta_time = clock.tick(60) / 1000
        delta_time = max(0.001, min(0.1, delta_time))
        await asyncio.sleep(0)


asyncio.run(main())