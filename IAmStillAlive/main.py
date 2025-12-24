import asyncio
import pygame
from Player import Player
from Tile import Tile

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
delta_time = 0.1


async def main():
    global delta_time
    player = Player(screen)
    player.set_spawn(
        x = (screen.get_width() // 2) - (player.width // 2),
        y = (screen.get_height() // 2) - (player.height // 2)
    )
    tile = Tile(
        screen = screen,
        x = 96,
        y = 0,
        width = 48,
        height = 48
    )
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
        tile.update(delta_time)
        player.update(delta_time)
        pygame.display.flip()
        delta_time = clock.tick(60) / 1000
        delta_time = max(0.001, min(0.1, delta_time))
        await asyncio.sleep(0)


asyncio.run(main())