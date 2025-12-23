import asyncio
import pygame
from Player import Player

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
delta_time = 0.1


async def main():
    global delta_time
    player = Player(screen)
    running = True
    while running:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.up = True
                if event.key == pygame.K_a:
                    player.left = True
                if event.key == pygame.K_s:
                    player.down = True
                if event.key == pygame.K_d:
                    player.right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player.up = False
                if event.key == pygame.K_a:
                    player.left = False
                if event.key == pygame.K_s:
                    player.down = False
                if event.key == pygame.K_d:
                    player.right = False
            if event.type == pygame.QUIT:
                running = False
        player.update(delta_time)
        pygame.display.flip()
        delta_time = clock.tick(60) / 1000
        delta_time = max(0.001, min(0.1, delta_time))
        await asyncio.sleep(0)


asyncio.run(main())