#!/usr/bin/env python3
import pathlib
import pygame


BG = (100, 149, 237)
FPS = 60
WIDTH, HEIGHT = 900, 500
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
VELOCITY = 3
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game")

ASSETS_DIR = pathlib.Path(__file__).with_name("Assets")
assert ASSETS_DIR.exists()

def _make_spaceship(asset, angle):
    path = ASSETS_DIR / asset
    image = pygame.image.load(path)
    spaceship = pygame.transform.scale(image, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
    spaceship = pygame.transform.rotate(spaceship, angle)
    return spaceship


YELLOW_SPACESHIP = _make_spaceship("spaceship_yellow.png", 90)
RED_SPACESHIP = _make_spaceship("spaceship_red.png", 270)


def draw_window(red, yellow):
    WIN.fill(BG)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()


def move_ship(rect, key_pressed, left, right, up, down):
    if key_pressed[left]:
        rect.x = max(0, rect.x - VELOCITY)
    elif key_pressed[right]:
        rect.x = min(WIDTH - rect.width, rect.x + VELOCITY)
    elif key_pressed[up]:
        rect.y = max(0, rect.y - VELOCITY)
    elif key_pressed[down]:
        rect.y = min(HEIGHT - rect.height, rect.y + VELOCITY)


# def _calculate_new_position(rect, direction):
#     if direction

def main():
    """ Entry """
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys_pressed = pygame.key.get_pressed()
        move_ship(red, keys_pressed, left=pygame.K_h, right=pygame.K_l, up=pygame.K_k, down=pygame.K_j)
        move_ship(yellow, keys_pressed, left=pygame.K_s, right=pygame.K_f, up=pygame.K_e, down=pygame.K_d)
        draw_window(red, yellow)
    pygame.quit()


if __name__ == '__main__':
    main()
