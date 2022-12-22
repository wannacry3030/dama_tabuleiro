import pygame

# Constants for window size and board size
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640
BOARD_SIZE = 8
SQUARE_SIZE = WINDOW_WIDTH // BOARD_SIZE

# Colors for the board and pieces
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Initialize Pygame
pygame.init()

# Set up the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Checkers")

# Create a 2D list to represent the checkers board
board = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Fill the board with pieces
for i in range(BOARD_SIZE):
    for j in range(BOARD_SIZE):
        if (i + j) % 2 == 0:
            board[i][j] = "black"
        else:
            board[i][j] = "red"

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Handle mouse clicks
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position and convert it to a square on the board
            mouse_x, mouse_y = pygame.mouse.get_pos()
            row = mouse_y // SQUARE_SIZE
            col = mouse_x // SQUARE_SIZE
            # Select the square if it is not already selected
            if board[row][col] == "selected":
                board[row][col] = "red"
            else:
                board[row][col] = "selected"
    # Clear the window
    window.fill(WHITE)
    # Draw the board and pieces
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == "black":
                pygame.draw.rect(window, BLACK, (j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            elif board[i][j] == "red":
                pygame.draw.rect(window, RED, (j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            elif board[i][j] == "selected":
                pygame.draw.rect(window, GREEN, (j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    # Update the window
    pygame.display.update()

# Quit Pygame
pygame.quit()
