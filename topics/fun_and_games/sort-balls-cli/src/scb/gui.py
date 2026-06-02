import sys

import pygame


class Sizing:
    BALLS_PER_COLUMN = 8
    BALL_RADIUS = 40
    BALL_GAP = 20

    SCREEN_WIDTH = 1400
    SCREEN_HEIGHT = 800

    COLUMNS_COUNT = 8
    COLUMN_HEIGHT = (BALL_RADIUS + BALL_GAP) * BALLS_PER_COLUMN
    COLUMN_WIDTH = SCREEN_WIDTH // (COLUMNS_COUNT + 1)

    LINE_THICKNESS = 5
    BALL_OUTLINE_THICKNESS = 5


class Color:
    BACKGROUND = (30, 30, 36)
    LINE = (150, 150, 150)  # Light gray for the dividers
    BALL_OUTLINE = (255, 255, 255)

    @staticmethod
    def balls():
        return [
            (235, 77, 75),  # red ball
            (48, 144, 255),  # blue ball
            (39, 174, 96),  # green ball
            (241, 196, 15),  # yellow ball
            (230, 126, 34),  # orange ball
            (155, 89, 182),  # purple ball
            (243, 104, 224),  # pink ball
        ]


def draw_ball(surface, color, center, radius):
    """Draw a ball."""
    pygame.draw.circle(surface, Color.BALL_OUTLINE, center, radius)
    pygame.draw.circle(surface, color, center, radius - Sizing.BALL_OUTLINE_THICKNESS)


def draw_grid(surface):
    for i in range(Sizing.COLUMNS_COUNT + 2):
        x = (Sizing.COLUMN_WIDTH // 2) + i * Sizing.COLUMN_WIDTH

        vertical_margin = Sizing.BALL_GAP * 2 + Sizing.BALL_RADIUS

        pygame.draw.line(
            surface,
            Color.LINE,
            (x, vertical_margin),
            (x, Sizing.COLUMN_HEIGHT + (Sizing.COLUMN_HEIGHT // 2)),
            Sizing.LINE_THICKNESS,
        )


#


def main():
    # Initialize Pygame
    pygame.init()

    screen = pygame.display.set_mode((Sizing.SCREEN_WIDTH, Sizing.SCREEN_HEIGHT))
    pygame.display.set_caption("7 Color Balls - Game Assets")

    # Main game loop
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear screen with a neutral dark background so colors pop
        screen.fill(Color.BACKGROUND)
        draw_grid(screen)

        # Calculate spacing to evenly distribute 7 balls across the screen
        spacing = Sizing.SCREEN_WIDTH // 8
        y_position = Sizing.SCREEN_HEIGHT // 2

        # Draw all 7 balls
        for i, color in enumerate(Color.balls()):
            x_position = (i + 1) * spacing
            draw_ball(screen, color, (x_position, y_position), Sizing.BALL_RADIUS)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()
