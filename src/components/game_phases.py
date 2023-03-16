import sys
import pymunk
import pygame
from Game import *
from components.Backend import *


def main_menu_phase():
    BackGround.IMAGE = Background('assets/mm_background.jpg', [0, 0], 1.5)
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            GlobalState.GAME_STATE = GameStatus.LEVEL_1


def level_one():
    # Pysics Space Setup
    # space = pymunk.Space()
    # space.gravity = (0, 500) # X gravity, Y gravity
    # space.step(1/50) # Updating time for physics sim

    # Background Image Setup
    BackGround.IMAGE = Background('assets/Number_1.png', [0, 0], 1.5) # The background image will eventually become a global variable dependent on cosmetics

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.exit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            Balls.append(create_ball(space, event.pos))
    
    # draw_ball(Screen, Balls, BallSurface.SURFACE)
    
def level_two():
    BackGround.IMAGE = Background('assets/Number_2.png', [0, 0], 1.5)

# def level_three():

# def level_four():

# def cos_menu():
