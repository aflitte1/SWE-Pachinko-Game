import sys
import pymunk
import pygame
from Game import *
import components.Backend as bnd

def main_menu_phase():
    BackGround = bnd.Background('assets/mm_background.jpg', [0, 0], 1.5)
    screen.blit(BackGround.image, BackGround.rect)
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            bnd.GlobalState.GAME_STATE = bnd.GameStatus.LEVEL_1

def level_one():
    BackGround = bnd.Background('assets/base_ball.png', [0, 0], 1.5)
    screen.blit(BackGround.image, BackGround.rect)

# def level_two():

# def level_three():

# def level_four():

# def cos_menu():