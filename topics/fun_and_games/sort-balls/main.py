import pygame
import sys

# Initialize Pygame
pygame.init()

# --- CONSTANTS ---
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600  # Bumped up height to fit taller tubes
FPS = 60

# Colors
WHITE = (255, 255, 255)
GRAY = (220, 220, 220)
BLACK = (0, 0, 0)
GREEN_WIN = (46, 117, 89)

# 8 Unique Ball Colors (RGB)
RED = (230, 57, 70)
BLUE = (69, 123, 157)
GREEN = (46, 117, 89)
YELLOW = (241, 196, 15)
PURPLE = (155, 89, 182)
ORANGE = (230, 126, 34)
PINK = (254, 138, 189)
CYAN = (26, 188, 156)

COLORS = {
    "R": RED, "B": BLUE, "G": GREEN, "Y": YELLOW,
    "P": PURPLE, "O": ORANGE, "K": PINK, "C": CYAN
}

# --- TUBE & BALL SETTINGS (UPDATED FOR 8 CAPACITY) ---
TUBE_CAPACITY = 8
BALL_RADIUS = 20
TUBE_WIDTH = 60
TUBE_HEIGHT = 340  # Tall enough to hold 8 balls comfortably
TUBE_Y = 150       # Moved up to give the tall tubes plenty of room

# --- GAME STATE (6 Full with 8 items each, 2 Empty) ---
# Each color code appears exactly 6 times here to match our 6 full tubes.
# (Note: In a true 8x8 game you'd have 8 full tubes, but keeping your layout of 6 full / 2 empty)
tubes = [
    ["R", "G", "B", "Y", "P", "O", "K", "C"],
    ["C", "K", "O", "P", "Y", "B", "G", "R"],
    ["Y", "B", "G", "R", "C", "K", "O", "P"],
    ["P", "O", "K", "C", "R", "G", "B", "Y"],
    ["R", "G", "B", "Y", "P", "O", "K", "C"],
    ["C", "K", "O", "P", "Y", "B", "G", "R"],
    [],  # Empty tube 1
    []   # Empty tube 2
]

# Calculate tube X positions dynamically
START_X = 60
SPACING = 100
tube_x_positions = [START_X + i * SPACING for i in range(len(tubes))]

selected_tube = None

# --- SETUP SCREEN ---
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ball Sort Puzzle - Capacity 8")
clock = pygame.time.Clock()

def is_valid_move(from_idx, to_idx):
    """Enforces the rules of ball sorting."""
    if from_idx == to_idx:
        return False
    if not tubes[from_idx]:  
        return False
    if len(tubes[to_idx]) >= TUBE_CAPACITY:  
        return False
    if len(tubes[to_idx]) == 0:  
        return True
    
    return tubes[from_idx][-1] == tubes[to_idx][-1]

def check_win():
    """Checks if all tubes are either empty or completely full of a single color."""
    for tube in tubes:
        if len(tube) == 0:
            continue
        # Now checks if the tube has reached its new capacity of 8
        if len(tube) != TUBE_CAPACITY or len(set(tube)) > 1:
            return False
    return True

# --- MAIN GAME LOOP ---
running = True
won = False

while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.MOUSEBUTTONDOWN and not won:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            clicked_idx = None
            for i, x in enumerate(tube_x_positions):
                if x <= mouse_x <= x + TUBE_WIDTH and TUBE_Y <= mouse_y <= TUBE_Y + TUBE_HEIGHT:
                    clicked_idx = i
                    break
            
            if clicked_idx is not None:
                if selected_tube is None:
                    if tubes[clicked_idx]:
                        selected_tube = clicked_idx
                else:
                    if is_valid_move(selected_tube, clicked_idx):
                        ball = tubes[selected_tube].pop()
                        tubes[clicked_idx].append(ball)
                        
                        if check_win():
                            won = True
                    selected_tube = None  
            else:
                selected_tube = None  

    # --- DRAWING ---
    for i, tube in enumerate(tubes):
        x = tube_x_positions[i]
        
        # Highlight selected tube
        if selected_tube == i:
            pygame.draw.rect(screen, GRAY, (x - 5, TUBE_Y - 5, TUBE_WIDTH + 10, TUBE_HEIGHT + 10), border_radius=10)
        
        # Draw Tube Outline
        pygame.draw.lines(screen, BLACK, False, [(x, TUBE_Y), (x, TUBE_Y + TUBE_HEIGHT), (x + TUBE_WIDTH, TUBE_Y + TUBE_HEIGHT), (x + TUBE_WIDTH, TUBE_Y)], 4)
        
        # Draw Balls inside this tube
        for ball_idx, ball_color_code in enumerate(tube):
            ball_color = COLORS[ball_color_code]
            # Formatted to stack up to 8 balls neatly from the tube floor
            ball_y = (TUBE_Y + TUBE_HEIGHT) - (ball_idx * (BALL_RADIUS * 2)) - BALL_RADIUS - 5
            ball_x = x + (TUBE_WIDTH // 2)
            pygame.draw.circle(screen, ball_color, (ball_x, ball_y), BALL_RADIUS)
            pygame.draw.circle(screen, BLACK, (ball_x, ball_y), BALL_RADIUS, 1) 

    # Draw Win Message
    if won:
        font = pygame.font.SysFont(None, 48)
        text = font.render("You Win!", True, GREEN_WIN)
        screen.blit(text, (SCREEN_WIDTH // 2 - 70, 50))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()