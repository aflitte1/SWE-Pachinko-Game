import pygame
from pygame.locals import *

vec = pygame.math.Vector2
ACC = 1.0
FRIC = -0.10
WIDTH = 800


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/bucket.png')
        self.image = pygame.transform.rotozoom(self.image, 0, 0.40)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.pos = vec((400, 700))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.player_position = vec(0, 0)

    def move(self):
        self.acc = vec(0, 0)

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT] or pressed_keys[K_a]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
            self.acc.x = +ACC

        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.player_position = self.pos.copy()

        if self.pos.x > WIDTH - 65:
            self.pos.x = WIDTH - 65
        if self.pos.x < 65:
            self.pos.x = 65

        self.rect.center = self.pos

    def draw(self, screen):
        screen.blit(self.image, self.rect)
