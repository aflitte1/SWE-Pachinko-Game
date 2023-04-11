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
space.gravity = (0, 100)  # gravity(horizontal gravity, vertical gravity)

balls = []

pegs = []
pegs.append(bnd.create_peg(space, (500, 500), 50, 0.5))
pegs.append(bnd.create_peg(space, (250, 600), 50, 0.5))

bnd.create_borders(space)
def draw_static_peg(pegs):
    for peg in pegs:
        pos_x = int(peg.body.position.x)
        pos_y = int(peg.body.position.y)
        # (place to draw, (R,G,B), placement, radius)
        pygame.draw.circle(screen, (0, 0, 0), (pos_x, pos_y), 50)

def main():
    while True:  # Game Start (We can implement a quit button if we wanted)
        for event in pygame.event.get():  # Checks for user input
            if event.type == pygame.QUIT:  # Checks for closing the game
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                balls.append(bnd.create_ball(space, event.pos, 80, 2))

        # This sets the background color. Im curious if we can just imput and image
        screen.fill((217, 217, 217))
        screen.blit(bnd.BackGround.IMAGE.image, bnd.BackGround.IMAGE.rect)
        bnd.draw_ball(screen, balls)
        draw_static_peg(pegs)
        space.step(1/50)  # Updating time for physics sim
        pygame.display.update()  # Renders the frame
        clock.tick(120)  # Sets the game FPS

if __name__ == "__main__":
    main()
