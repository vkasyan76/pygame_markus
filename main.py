import pygame  # Main library for game development
import time    # To add delays or timing features
import random  # To generate random numbers or choices

# Define the dimensions of the game window
WIDTH, HEIGHT = 1000, 800

# Create the game window with the specified dimensions
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the title of the game window
pygame.display.set_caption("Space Dodge")

# Scale the background image to fit the window dimensions
BG = pygame.transform.scale(pygame.image.load("bg.jpeg"), (WIDTH, HEIGHT))

# Function to draw elements on the screen
def draw():
    WIN.blit(BG, (0, 0))  # Draw the scaled background at position (0, 0)
    pygame.display.update()  # Refresh the display to show changes

# Main function to run the game
def main():
    run = True  # This variable will keep the game running

    # Game loop: This will keep running while 'run' is True
    while run:
        # Check for user input events
        for event in pygame.event.get():
            # If the user clicks the close button, exit the loop
            if event.type == pygame.QUIT:
                run = False  # Stop the game loop
                break  # Exit the event loop

        draw()  # Call the draw function to update the screen

    # Quit Pygame properly when the game loop ends
    pygame.quit()

# Ensures the main function runs only if this file is executed directly
if __name__ == "__main__":
    main()
