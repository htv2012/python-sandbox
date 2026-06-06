import sys

import pygame

from scb.grid import Grid

from . import colors, size
from .generate import create_grid


def draw_ball(surface, color, center, radius):
    """Draw a ball."""
    # TODO: Given a grid or stack, draw it
    pygame.draw.circle(surface, colors.BALL_OUTLINE, center, radius)
    pygame.draw.circle(surface, color, center, radius - size.BALL_OUTLINE_THICKNESS)


def draw_columns(surface):
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


def draw_grid(surface, grid: Grid):
    for col, stack in enumerate(grid):
        left = size.GRID_LEFT + size.GRID_LEFT * col
        bottom = size.GRID_BOTTOM - size.BALL_GAP
        for i in stack:
            color = colors.BALLS[i]
            draw_ball(
                surface,
                color,
                (
                    (left + left + size.COLUMN_WIDTH) / 2,
                    bottom - (size.BALL_RADIUS + size.BALL_GAP) / 2,
                ),
                size.BALL_RADIUS,
            )
            bottom -= 2 * (size.BALL_RADIUS) + size.BALL_GAP


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
    pygame.init()
    screen = pygame.display.set_mode((size.SCREEN_WIDTH, size.SCREEN_HEIGHT))
    pygame.display.set_caption("7 Color Balls - Game Assets")
    grid = create_grid()

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear screen with a neutral dark background so colors pop
        screen.fill(colors.BACKGROUND)
        draw_guide(screen)
        draw_columns(screen)
        draw_grid(screen, grid)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()
