import pygame
import sys
import pymunk
import components.Backend as bnd

# GLOBALS

# INITIALIZE PYGAME
pygame.init()
screen = pygame.display.set_mode((800, 800))  # Creates a window
clock = pygame.time.Clock()  # Creates a game clock
space = pymunk.Space()  # Creates bgndical space
space.gravity = (0, 500)  # gravity(horizontal gravity, vertical gravity)

BackGround = bnd.Background('assets/mm_background.jpg', [0, 0], 1.5)

balls = []
ball_surface = pygame.image.load('assets/base_ball.png')
ball_surface = pygame.transform.rotozoom(ball_surface, 0, 0.2)

pegs = []
pegs.append(bnd.create_peg(space, (500, 500)))
pegs.append(bnd.create_peg(space, (250, 600)))


def draw_ball(balls):
    for ball in balls:
        pos_x = int(ball.body.position.x)
        pos_y = int(ball.body.position.y)
        apple_rect = ball_surface.get_rect(center=(pos_x, pos_y))
        screen.blit(ball_surface, apple_rect)


def draw_static_peg(pegs):
    for peg in pegs:
        pos_x = int(peg.body.position.x)
        pos_y = int(peg.body.position.y)
        # (place to draw, (R,G,B), placement, radius)
        pygame.draw.circle(screen, (0, 0, 0), (pos_x, pos_y), 50)


while True:  # Game Start (We can implement a quit button if we wanted)
    for event in pygame.event.get():  # Checks for user input
        if event.type == pygame.QUIT:  # Checks for closing the game
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            balls.append(bnd.create_ball(space, event.pos))

    # This sets the background color. Im curious if we can just imput and image
    screen.fill((217, 217, 217))
    screen.blit(BackGround.image, BackGround.rect)
    draw_ball(balls)
    draw_static_peg(pegs)
    space.step(1/50)  # Updating time for physics sim
    pygame.display.update()  # Renders the frame
    clock.tick(120)  # Sets the game FPS
