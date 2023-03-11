import pygame, sys

pygame.init() # Initializes a pygame
screen = pygame.display.set_mode((800, 800)) # Creates a window
clock = pygame.time.Clock() # Creates a game clock

while True: # Game Start (We can implement a quit button if we wanted)
    for event in pygame.event.get(): # Checks for user input
        if event.type == pygame.QUIT: # Checks for closing the game
            pygame.quit()
            sys.exit()

    screen.fill((217, 217, 217)) # This sets the background color. Im curious if we can just imput and image
    pygame. display.update() # Renders the frame
    clock.tick(120) # Sets the game FPS
