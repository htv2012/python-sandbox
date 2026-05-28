
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
coord = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("gray")
    pygame.draw.circle(screen, "red", coord, 50)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_h]:
        coord.x -= 300 * dt
    elif keys[pygame.K_l]:
        coord.x += 300 * dt
    elif keys[pygame.K_j]:
        coord.y += 300 * dt
    elif keys[pygame.K_k]:
        coord.y -= 300 * dt

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
