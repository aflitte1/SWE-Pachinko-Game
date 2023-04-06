import pygame
from pygame.locals import *

vec = pygame.math.Vector2
ACC = 0.5
FRIC = -0.10
HIGHT = 800
WIDTH = 800


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/bucket.png')
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.pos = vec((400, 400))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.player_position = vec(400, 400)

    def move(self):
        self.acc = vec(0, 0)

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT] or pressed_keys[K_a]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
            self.acc.x = ACC

        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.player_position = self.pos.copy()

        if self.pos.x > WIDTH:
            self.pos.x = WIDTH
        if self.pos.x < 0:
            self.pos.x = 0

        self.rect.center = self.pos

    def draw(self, screen):
        screen.blit(self.image, self.rect)
