import asyncio
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
player = pygame.image.load("player.png").convert_alpha()
clock = pygame.time.Clock()


async def main():
    delta_time = 0.1
    x = 0
    y = 0
    up = False
    down = False
    left = False
    right = False
    running = True
    while running:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    up = True
                if event.key == pygame.K_a:
                    left = True
                if event.key == pygame.K_s:
                    down = True
                if event.key == pygame.K_d:
                    right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    up = False
                if event.key == pygame.K_a:
                    left = False
                if event.key == pygame.K_s:
                    down = False
                if event.key == pygame.K_d:
                    right = False
            if event.type == pygame.QUIT:
                running = False
        if up:
            y -= 60 * delta_time
        if down:
            y += 60 * delta_time
        if left:
            x -= 60 * delta_time
        if right:
            x += 60 * delta_time
        screen.blit(player, (x, y))
        pygame.display.flip()
        delta_time = clock.tick(60) / 1000
        delta_time = max(0.001, min(0.1, delta_time))
        await asyncio.sleep(0)


asyncio.run(main())