import pygame
import sys
import random

from pollutionTips import tips

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
orange_color = (255, 165, 0)
blue = (0, 0, 255)
azureBlue = (0, 127, 255)
green = (0, 255, 0)
dark_green = (0, 200, 0)
bright_orange = (255,95,31)

# trashcan image 

trashcan_image = pygame.image.load('th.png')  
new_width = 100  
new_height = 100 
trashcan_image = pygame.transform.scale(trashcan_image, (new_width, new_height))  





trashcan_rect = trashcan_image.get_rect(topleft=(20, 20))  


# people image

people_image = pygame.image.load('people.png')
new_width = 100  
new_height = 100 
people_image = pygame.transform.scale(people_image, (new_width, new_height))

people_rect = people_image.get_rect(topright=(780, 20))  



# map image

map_image = pygame.image.load('map.png') 
map_rect = map_image.get_rect(center=(width // 2, height // 2))




# Final Screen

final_screen = pygame.image.load("Finalscreen.PNG")
final_screen_rect = final_screen.get_rect(center=(width // 2, height // 2))


# back to menu button

back_button_width = 200
back_button_height = 50
back_button_x = (width // 2) - (back_button_width // 2)
back_button_y = (height // 2) + 50  

back_button_font = pygame.font.SysFont('Corbel', 35)
back_button_text = back_button_font.render('Return To Main Menu', True, white)
back_button_text_rect = back_button_text.get_rect(center=(back_button_x + back_button_width // 2, back_button_y + back_button_height // 2))


# orange image

orange_image = pygame.image.load('character.png')  #
orange_rect = orange_image.get_rect(top=50, left=50)  # Initial position of the orange

# orange functionality

class Orange:
    def __init__(self, x, y):
        self.rect = orange_rect
        self.speed = 30
        self.rect.topleft = (x, y)

    def move(self, dx, dy):
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

    def draw(self, surface):
        surface.blit(orange_image, self.rect)
orange = Orange(50, 50)


# Waterbottle object
class WaterBottle:
    def __init__(self, x, y):
        self.image = pygame.image.load('waterbottle.PNG')  
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 5

    def move(self):
        # Randomly move the water bottle in a random direction
        direction = random.choice(['up', 'down', 'left', 'right'])
        if direction == 'up':
            self.rect.y -= self.speed
        elif direction == 'down':
            self.rect.y += self.speed
        elif direction == 'left':
            self.rect.x -= self.speed
        elif direction == 'right':
            self.rect.x += self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Initialize the water bottle object
middle_bottom_range = (height // 3) * 2
water_bottle = WaterBottle(random.randint(0, width - 50), random.randint(height // 2, middle_bottom_range))


# Ciggarette Butt object

class Ciggarette:
    def __init__(self, x, y):
        self.image = pygame.image.load('ciggarette.PNG')  
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 5

    def move(self):
        # Randomly move the ciggarette in a random direction
        direction = random.choice(['up', 'down', 'left', 'right'])
        if direction == 'up':
            self.rect.y -= self.speed
        elif direction == 'down':
            self.rect.y += self.speed
        elif direction == 'left':
            self.rect.x -= self.speed
        elif direction == 'right':
            self.rect.x += self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Initialize the ciggarette bottle object
Ciggarette = Ciggarette(random.randint(0, width - 50), random.randint(height // 2, middle_bottom_range))



# Create a font object
font = pygame.font.SysFont('comicsansms', 120)
text = font.render('Cutie Clean-up', True, orange_color, None)  # Set background color to None
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

def display_pink_text_box(surface, text):
    # Pink text box properties
    text_box_color = (255, 192, 203)  # Pink color
    text_box_width = 700  
    text_box_height = 150  # Increased box height
    text_box_x = (width // 2) - (text_box_width // 2)
    text_box_y = (height // 2) + (height // 4) 

    # Create font for the pink text box
    pink_font = pygame.font.SysFont('Arial', 18)  # Smaller text size
    pink_text_rendered = pink_font.render(text, True, white)  # Render the text

    # Draw the pink text box
    pygame.draw.rect(surface, text_box_color, (text_box_x, text_box_y, text_box_width, text_box_height))
    surface.blit(pink_text_rendered, (text_box_x + 20, text_box_y + 20))  

running = True
game_started = False
tip_displayed = False
show_back_button = False
running_game = False
restart_game = False

screen.blit(trashcan_image, trashcan_rect)

def reset_game():
    global game_started, tip_displayed, show_back_button
    game_started = False
    tip_displayed = False
    show_back_button = False

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

    # Show trashcan
    screen.blit(trashcan_image, trashcan_rect)

    # Show people
    screen.blit(people_image,people_rect)

    display_pink_text_box(screen, "Run around as Cutie the Orange and pick up trash in the ocean. Save the Earth!")



    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_x <= mouse_pos[0] <= button_x + button_width and button_y <= mouse_pos[1] <= button_y + button_height:
                print("Starting the game...") 
                game_started = True
            elif back_button_x <= mouse_pos[0] <= back_button_x + back_button_width and back_button_y <= mouse_pos[1] <= back_button_y + back_button_height:
                reset_game()  # Reset the game when the back button is clicked
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                orange.move(-1, 0)  # Move left
            elif event.key == pygame.K_RIGHT:
                orange.move(1, 0)  # Move right
            elif event.key == pygame.K_UP:
                orange.move(0, -1)  # Move up
            elif event.key == pygame.K_DOWN:
                orange.move(0, 1)  # Move down
    if game_started:
        screen.blit(map_image, map_rect)
        orange.draw(screen)
        # water_bottle.move()  # Move the water bottle randomly
        water_bottle.draw(screen)  # Draw the water bottle
        Ciggarette.draw(screen)
            # Check for collisions between orange and objects
       # Check for collisions between orange and objects
        if orange.rect.colliderect(water_bottle.rect) and not tip_displayed:
            random_tip = random.choice(tips)
            tip_font = pygame.font.SysFont('Arial', 22)
            tip_text = tip_font.render(random_tip, True, bright_orange)
            tip_displayed = True  # Set the flag to True once the tip is displayed
        
        if orange.rect.colliderect(Ciggarette.rect) and not tip_displayed:
            random_tip = random.choice(tips)
            tip_font = pygame.font.SysFont('Arial', 22)
            tip_text = tip_font.render(random_tip, True, bright_orange)
            tip_displayed = True  # Set the flag to True once the tip is displayed

        if tip_displayed:
            screen.blit(final_screen, final_screen_rect)
            screen.blit(tip_text, (50, height // 1.5))  # Adjust position as needed
            show_back_button = True
        if show_back_button:
            pygame.draw.rect(screen, dark_green, (back_button_x, back_button_y, back_button_width, back_button_height))
            screen.blit(back_button_text, back_button_text_rect)
                    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
