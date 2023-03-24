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
    # Background Image Setup
    # The background image will eventually become a global variable dependent on cosmetics
    BackGround.IMAGE = Background('assets/1.jpg', [0, 0], 1.0)


def level_two():
    BackGround.IMAGE = Background('assets/2.jpg', [0, 0], 1.5)


def level_three():
    BackGround.IMAGE = Background('assets/haunted_background.jpeg', [-8, 0], 0.56)
    BallSurface.SURFACE = ball_look('assets/haunted_ball.png', 0.15)
    PegSurface.SURFACE = ball_look('assets/haunted_peg.png', 0.40)


def level_four():
    BackGround.IMAGE = Background('assets/4.jpg', [0, 0], 1.5)


def cos_menu():
    BackGround.IMAGE = Background('assets/cosmetic.jpg', [0, 0], 1.5)
