import pygame
import sys
import pymunk
from enum import Enum


def create_ball(space, pos):
    body = pymunk.Body(1, 100, body_type=pymunk.Body.DYNAMIC)
    # body.position = (400, 0)
    body.position = pos
    shape = pymunk.Circle(body, 80)  # Pass in body and radius
    shape.elasticity = 1
    space.add(body, shape)
    return shape


def create_peg(space, pos):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = pos
    shape = pymunk.Circle(body, 50)
    shape.elasticity = 0.5
    space.add(body, shape)
    return shape


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location, scale):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.rotozoom(self.image, 0, scale)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location\



class GameStatus(Enum):
    MAIN_MENU = 0
    LEVEL_1 = 1
    LEVEL_2 = 2
    LEVEL_3 = 3
    LEVEL_4 = 4
    COS_MENU = 5

class GlobalState:
    GAME_STATE = GameStatus.MAIN_MENU
