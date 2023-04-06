import pygame
import sys
import pymunk
from enum import Enum


def create_ball(space, pos, size, elastic):
    body = pymunk.Body(1, 100, body_type=pymunk.Body.DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body, size)  # Pass in body and radius
    shape.elasticity = elastic
    space.add(body, shape)
    return shape


def draw_ball(screen, balls):
    for ball in balls:
        pos_x = int(ball.body.position.x)
        pos_y = int(ball.body.position.y)
        ball_rect = BallSurface.SURFACE.get_rect(center=(pos_x, pos_y))
        screen.blit(BallSurface.SURFACE, ball_rect)


def ball_look(file_name, scale) -> pygame.SurfaceType:
    surface = pygame.image.load(file_name)
    surface = pygame.transform.rotozoom(surface, 0, scale)
    return surface


def create_peg(space, pos, size, elastic):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = pos
    shape = pymunk.Circle(body, size)
    shape.elasticity = elastic
    space.add(body, shape)
    return shape


def draw_peg(screen, pegs):
    for peg in pegs:
        pos_x = int(peg.body.position.x)
        pos_y = int(peg.body.position.y)
        peg_rect = PegSurface.SURFACE.get_rect(center=(pos_x, pos_y))
        screen.blit(PegSurface.SURFACE, peg_rect)


def create_rectangle_static(space, pos_x, pos_y, width, height):

    body = pymunk.Body(body_type=pymunk.Body.STATIC)

    body.position = (pos_x, pos_y)
    shape = pymunk.Poly.create_box(body, (width, height))
    shape.elasticity = 0.1
    space.add(body, shape)


def create_borders(space):
    # create_rectangle_static(space, 400, -100, 800, 200)  # ceiling
    create_rectangle_static(space, -100, 400, 200, 800)  # left wall
    create_rectangle_static(space, 899, 400, 200, 800)  # right wall


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location, scale):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.rotozoom(self.image, 0, scale)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class GameStatus(Enum):
    MAIN_MENU = 0
    LEVEL_1 = 1
    LEVEL_2 = 2
    LEVEL_3 = 3
    LEVEL_4 = 4
    COS_MENU = 5


class GlobalState:
    GAME_STATE = GameStatus.MAIN_MENU


class BackGround:
    IMAGE = Background('assets/mm_background.jpg', [0, 0], 1.5)


class BallSurface:
    SURFACE = ball_look('assets/base_ball.png', 0.15)


class PegSurface:
    SURFACE = ball_look('assets/peg.png', 0.28)
