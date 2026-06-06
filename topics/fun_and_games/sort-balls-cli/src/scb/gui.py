import sys

import pygame

from . import colors, size


def draw_ball(surface, color, center, radius):
    """Draw a ball."""
    # TODO: Given a grid or stack, draw it
    pygame.draw.circle(surface, colors.BALL_OUTLINE, center, radius)
    pygame.draw.circle(surface, color, center, radius - size.BALL_OUTLINE_THICKNESS)


def draw_grid(surface):
    top = 100
    for x in range(100, (size.COLUMNS_COUNT + 2) * 100, 100):
        pygame.draw.line(
            surface,
            colors.LINE,
            (x, top),
            (x, 900),
            size.LINE_THICKNESS,
        )
    # for i in range(size.COLUMNS_COUNT + 2):
    #     x = (size.COLUMN_WIDTH // 2) + i * size.COLUMN_WIDTH

    #     pygame.draw.line(
    #         surface,
    #         colors.LINE,
    #         (x, size.VERTICAL_MARGIN),
    #         (x, size.VERTICAL_MARGIN + size.COLUMN_HEIGHT),
    #         size.LINE_THICKNESS,
    #     )


def draw_guide(surface):
    thin = 1
    thick = 2

    for x in range(0, size.SCREEN_WIDTH, 20):
        pygame.draw.line(
            surface,
            colors.GUIDE_MAJOR if x % 100 == 0 else colors.GUIDE_MINOR,
            (x, 0),
            (x, size.SCREEN_HEIGHT),
            thick if x % 100 == 0 else thin,
        )

    for y in range(0, size.SCREEN_HEIGHT, 20):
        pygame.draw.line(
            surface,
            colors.GUIDE_MAJOR if y % 100 == 0 else colors.GUIDE_MINOR,
            start_pos=(0, y),
            end_pos=(size.SCREEN_WIDTH, y),
            width=thick if y % 100 == 0 else thin,
        )


def main():
    # Initialize Pygame
    pygame.init()

    screen = pygame.display.set_mode((size.SCREEN_WIDTH, size.SCREEN_HEIGHT))
    pygame.display.set_caption("7 Color Balls - Game Assets")

    # Main game loop
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear screen with a neutral dark background so colors pop
        screen.fill(colors.BACKGROUND)
        draw_guide(screen)
        draw_grid(screen)

        # Calculate spacing to evenly distribute 7 balls across the screen
        spacing = size.SCREEN_WIDTH // 8
        y_position = size.SCREEN_HEIGHT // 2

        # Draw all 7 balls
        for i, color in enumerate(colors.BALLS):
            x_position = (i + 1) * spacing
            draw_ball(screen, color, (x_position, y_position), size.BALL_RADIUS)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()
