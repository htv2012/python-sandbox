import sys

import pygame

from . import colors, size


def draw_ball(surface, color, center, radius):
    """Draw a ball."""
    # TODO: Given a grid or stack, draw it
    pygame.draw.circle(surface, colors.BALL_OUTLINE, center, radius)
    pygame.draw.circle(surface, color, center, radius - size.BALL_OUTLINE_THICKNESS)


def draw_grid(surface):
    for i in range(size.COLUMNS_COUNT + 1):
        x = size.GRID_LEFT + (i * size.COLUMN_WIDTH)
        pygame.draw.line(
            surface,
            colors.LINE,
            (x, size.GRID_TOP),
            (x, size.GRID_BOTTOM),
            size.LINE_THICKNESS,
        )
    pygame.draw.line(
        surface,
        colors.LINE,
        (size.GRID_LEFT, size.GRID_BOTTOM),
        (size.GRID_RIGHT, size.GRID_BOTTOM),
        size.LINE_THICKNESS,
    )


def draw_guide(surface):
    for x in range(0, max(size.SCREEN_WIDTH, size.SCREEN_HEIGHT), 50):
        pygame.draw.line(
            surface,
            colors.GUIDE,
            (x, 0),
            (x, size.SCREEN_HEIGHT),
        )
        pygame.draw.line(
            surface,
            colors.GUIDE,
            start_pos=(0, x),
            end_pos=(size.SCREEN_WIDTH, x),
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
