import pygame



pygame.init()  # Initializes a pygame

screen = pygame.display.set_mode((800, 800))  # Creates a window
clock = pygame.time.Clock()  # Creates a game clock

level_count = 1
screen.fill((217, 217, 217))
pygame.display.set_caption('Pachinko Main Menu')

background1 = pygame.image.load('assets/background1.png')
background2 = pygame.image.load('assets/background2.png')
background3 = pygame.image.load('assets/background3.png')
background4 = pygame.image.load('assets/background4.png')


playbutton = pygame.image.load('assets/play_button.png')

def DrawLevelBackground(level):
    match level:#image should fill whole background
        case 1:
            screen.blit(background1, (0,0))
        case 2:
            screen.blit(background2, (0,0))
        case 3:
            screen.blit(background3, (0,0))
        case 4:
            screen.blit(background4, (0,0))
    screen.blit(playbutton, (400, 400))
    DrawLeaderboard()

def DrawLeaderboard(level):
    pass
    


while True:  # Game Start (We can implement a quit button if we wanted)
    for event in pygame.event.get():  # Checks for user input
        if event.type == pygame.QUIT:  # Checks for closing the game
            pygame.quit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]:
            if level_count > 1:
                level_count -= 1
                DrawLevelBackground(level_count)
        elif pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]:
            if level_count < 4:
                level_count += 1
                DrawLevelBackground(level_count)
    # This sets the background color. Im curious if we can just imput and image

    print(level_count)
    pygame. display.update()  # Renders the frame
    clock.tick(120)  # Sets the game FPS
