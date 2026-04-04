import pygame
import random
import sys

# 1. INITIALIZE & CONSTANTS
pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 400, 400
ROWS, COLS = 4, 4
SQUARE_SIZE = WIDTH // COLS
FPS = 60

# COLORS (RGB)
GRAY = (150, 150, 150)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# YOUR 8-COLOR PALETTE
COLOR_MAP = {
    1: (255, 0, 0), # Red
    2: (0, 0, 255), # Blue
    3: (0, 255, 0), # Green
    4: (255, 255, 0), # Yellow
    5: (255, 165, 0), # Orange
    6: (139, 69, 19), # Brown
    7: (0, 0, 0), # Black
    8: (255, 255, 255) # White
}
font = pygame.font.SysFont("Arial",50,bold = True)
small_font = pygame.font.SysFont("Arial",20,bold = True)

def reset_game():
    global secret_grid,display_grid,first_card,second_card, waiting_for_timer     

    # 2. SET UP THE BRAINS
    # Create 8 pairs and shuffle them
    cards = list(range(1, 9)) * 2
    random.shuffle(cards)

    # Secret Brain (Answers)
    secret_grid = [cards[i:i+4] for i in range(0, 16, 4)]

    # Player's Brain (-1 means hidden/gray)
    display_grid = [[-1 for _ in range(COLS)] for _ in range(ROWS)]

    # 3. GAME STATE VARIABLES
    first_card = None # Stores (row, col)
    second_card = None # Stores (row, col)
    waiting_for_timer = False
    timer_start_time = 0
reset_game()    

# SET UP WINDOW
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Memory Match - MOHITHA")
clock = pygame.time.Clock()
pygame.font.init()
font=pygame.font.SysFont("Arial",50,bold=True)

# 4. THE MAIN GAME LOOP
while True:
    screen.fill(BLACK)
    current_time = pygame.time.get_ticks()
    
    # --- EVENT HANDLING ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_r:
                  reset_game()    
        if event.type == pygame.MOUSEBUTTONDOWN and not waiting_for_timer:
            pos = pygame.mouse.get_pos()
            col = pos[0] // SQUARE_SIZE
            row = pos[1] // SQUARE_SIZE
            
            # Check if square is already open
            if display_grid[row][col] == -1:
                display_grid[row][col] = secret_grid[row][col]
                if first_card is None:
                    first_card = (row, col)
                else:
                    second_card = (row, col)
                
                # Check for Match
                    r1, c1 = first_card
                    r2, c2 = second_card
                    
                    if secret_grid[r1][c1] == secret_grid[r2][c2]:
                        # MATCH! Reset tracking, keep cards open
                        first_card = None
                        second_card = None
                    else:# NO MATCH! Start the 1-second timer
                        waiting_for_timer = True
                        timer_start_time = current_time
                        
                        # --- TIMER LOGIC (Non-blocking) ---
    if waiting_for_timer:
        if current_time - timer_start_time > 1000: # 1000ms = 1 sec
            r1, c1 = first_card
            r2, c2 = second_card
            display_grid[r1][c1] = -1
            display_grid[r2][c2] = -1
            first_card = None
            second_card = None
            waiting_for_timer = False
                                
    # --- DRAWING ---
    hidden_count = 0
    for row in range(ROWS):
        for col in range(COLS):
            val = display_grid[row][col]
            if  val == -1:
                hidden_count += 1
            color = COLOR_MAP[val] if val != -1 else GRAY

                                # Draw the square with a small margin (padding)
            rect = (col * SQUARE_SIZE + 5, row * SQUARE_SIZE + 5,
                SQUARE_SIZE - 10, SQUARE_SIZE - 10)
                
                
            pygame.draw.rect(screen, color, rect)
    if hidden_count == 0:
                text_surface=font.render("YOU WIN !", True,WHITE)
                text_rect = text_surface.get_rect(center=(WIDTH//2,HEIGHT//2))
                reset_surf =small_font.render("Press 'R' to Restart",True,WHITE)
                reset_rect = reset_surf.get_rect(center= (WIDTH//2,HEIGHT// + 30))
                pygame.draw.rect(screen,BLACK,(text_rect.x-10,text_rect.y-10,
                                               text_rect.width + 20,
                                               text_rect.height + 20))
                
                screen.blit(text_surface,text_rect)
    pygame.display.flip()
    clock.tick(FPS)