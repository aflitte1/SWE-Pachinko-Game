import pygame
import sys
import pymunk


def create_apple(space, pos):
    body = pymunk.Body(1, 100, body_type=pymunk.Body.DYNAMIC)
    # body.position = (400, 0)
    body.position = pos
    shape = pymunk.Circle(body, 80)  # Pass in body and radius
    shape.elasticity = 1
    space.add(body, shape)
    return shape


def draw_apples(apples):
    for apple in apples:
        pos_x = int(apple.body.position.x)
        pos_y = int(apple.body.position.y)
        apple_rect = apple_surface.get_rect(center=(pos_x, pos_y))
        screen.blit(apple_surface, apple_rect)


def static_ball(space, pos):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = pos
    shape = pymunk.Circle(body, 50)
    shape.elasticity = 0.5 
    space.add(body, shape)
    return shape


def draw_static_ball(balls,):
    for ball in balls:
        pos_x = int(ball.body.position.x)
        pos_y = int(ball.body.position.y)
        # (place to draw, (R,G,B), placement, radius)
        pygame.draw.circle(screen, (0, 0, 0), (pos_x, pos_y), 50)


pygame.init()  # Initializes a pygame
screen = pygame.display.set_mode((800, 800))  # Creates a window
clock = pygame.time.Clock()  # Creates a game clock
space = pymunk.Space()  # Creates physical space
space.gravity = (0, 500)  # gravity(horizontal gravity, vertical gravity)

apple_surface = pygame.image.load('assets/base_ball.png')
apple_surface = pygame.transform.rotozoom(apple_surface, 0, 0.2)
apples = []

balls = []
balls.append(static_ball(space, (500, 500)))
balls.append(static_ball(space, (250, 600)))

while True:  # Game Start (We can implement a quit button if we wanted)
    for event in pygame.event.get():  # Checks for user input
        if event.type == pygame.QUIT:  # Checks for closing the game
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            apples.append(create_apple(space, event.pos))

    # This sets the background color. Im curious if we can just imput and image
    screen.fill((217, 217, 217))
    draw_apples(apples)
    draw_static_ball(balls)
    space.step(1/50)  # Updating time for physics sim
    pygame. display.update()  # Renders the frame
    clock.tick(120)  # Sets the game FPS
