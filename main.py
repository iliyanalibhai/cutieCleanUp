import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the screen
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cutie Clean Up")  # Game name
clock = pygame.time.Clock()

# Define colors
white = (255, 255, 255)
orange = (255, 165, 0)
blue = (0, 0, 255)
azureBlue = (0, 127, 255)
green = (0, 255, 0)
dark_green = (0, 200, 0)

# map image

map_image = pygame.image.load('map.png')  # Replace with your map image file name
map_rect = map_image.get_rect(center=(width // 2, height // 2))


# Create a font object
font = pygame.font.SysFont('comicsansms', 120)
text = font.render('Cutie Clean-up', True, orange, None)  # Set background color to None
textRect = text.get_rect(center=(width // 2, height // 3))

# Define button dimensions and positions
button_width = 140
button_height = 40
button_x = (width // 2) - (button_width // 2)
button_y = height // 2

# Create a font for the button text
button_font = pygame.font.SysFont('Corbel', 35)
button_text = button_font.render('Play', True, white)
button_text_rect = button_text.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))

running = True
game_started = False
while running:
    screen.fill(azureBlue)  # Fill the screen with azure blue

    # Draw the game title text
    screen.blit(text, textRect)

    # Get mouse position and check for clicks
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Draw the button
    if button_x <= mouse_pos[0] <= button_x + button_width and button_y <= mouse_pos[1] <= button_y + button_height:
        pygame.draw.rect(screen, green, (button_x, button_y, button_width, button_height))
    else:
        pygame.draw.rect(screen, dark_green, (button_x, button_y, button_width, button_height))

    # Show button text
    screen.blit(button_text, button_text_rect)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_x <= mouse_pos[0] <= button_x + button_width and button_y <= mouse_pos[1] <= button_y + button_height:
                print("Starting the game...")  # Replace with your game logic
                game_started = True
    if game_started:
        screen.blit(map_image, map_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
