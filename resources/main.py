import asyncio
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
player = pygame.image.load("player.png").convert_alpha()
clock = pygame.time.Clock()


async def main():
    delta_time = 0.1
    x = 0
    running = True
    while running:
        screen.fill((255, 255, 255))
        screen.blit(player, (x, 30))
        x += 60 * delta_time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
        delta_time = clock.tick(60) / 1000
        delta_time = max(0.001, min(0.1, delta_time))
        await asyncio.sleep(0)


asyncio.run(main())