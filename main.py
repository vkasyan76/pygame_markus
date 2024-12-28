import pygame  # Main library for game development
import time    # To add delays or timing features
import random  # To generate random numbers or choices
pygame.font.init()

# Define the dimensions of the game window
WIDTH, HEIGHT = 1000, 800

# Create the game window with the specified dimensions
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the title of the game window
pygame.display.set_caption("Space Dodge")

# Scale the background image to fit the window dimensions
BG = pygame.transform.scale(pygame.image.load("bg.jpeg"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

PLAYER_VEL = 5
STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 3

FONT = pygame.font.SysFont("comicsans", 30) 

# Function to draw elements on the screen
def draw(player, elapsed_time, stars):
    WIN.blit(BG, (0, 0))  # Draw the scaled background at position (0, 0)

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1,"white")
    WIN.blit(time_text, (10, 10))

    pygame.draw.rect(WIN, "red", player)

    for star in stars:
        pygame.draw.rect(WIN, "white", star)

    for star in stars:
        pygame.draw.rect(WIN, "white", star)

    pygame.display.update()  # Refresh the display to show changes

# Main function to run the game
def main():
    run = True  # This variable will keep the game running

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT,
                          PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000
    star_count = 0

    stars = []
    hit = False

    # Game loop: This will keep running while 'run' is True
    while run:
        star_count+= clock.tick(60)
        elapsed_time = time.time() - start_time

        if star_count >= star_add_increment:
            for _ in range(9):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)
            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0
            

        # Check for user input events
        for event in pygame.event.get():
            # If the user clicks the close button, exit the loop
            if event.type == pygame.QUIT:
                run = False  # Stop the game loop
                break  # Exit the event loop

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL
        #if keys[pygame.K_UP] and player.y - PLAYER_VEL >= 0:
           # player.y -= PLAYER_VEL
       # if keys[pygame.K_DOWN] and player.x + PLAYER_VEL + player.height <= HEIGHT:
          #  player.y += PLAYER_VEL

        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break

        if hit:
           lost_text = FONT.render("You Lost!", 1, "red")
           WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
           pygame.display.update()
           pygame.time.delay(4000)
           break
                



        draw(player,elapsed_time, stars)  # Call the draw function to update the screen

    # Quit Pygame properly when the game loop ends
    pygame.quit()

# Ensures the main function runs only if this file is executed directly
if __name__ == "__main__":
    main()
