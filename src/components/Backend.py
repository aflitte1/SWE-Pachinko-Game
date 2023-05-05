import pygame
from pygame.locals import *
import sys
import pymunk
from enum import Enum
from src.components.music import MusicService
from src.components.leaderboard import *

flags = DOUBLEBUF
pygame.display.init()
pygame.display.set_mode((800, 800), flags)

vec = pygame.math.Vector2


def create_ball(space, pos, size, elastic) -> pymunk.Circle:
    body = pymunk.Body(1, 100, body_type=pymunk.Body.DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body, size)  # Pass in body and radius
    shape.elasticity = elastic
    space.add(body, shape)
    return shape


def ball_look(file_name, scale) -> pygame.SurfaceType:
    surface = pygame.image.load(file_name)
    surface = pygame.transform.rotozoom(surface, 0, scale)
    return surface


def delete_ball(pos_y):
    if (pos_y > 850):
        return True
    else:
        return False


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, Space, size, elastic):
        super().__init__()
        self.image = BallSurface.SURFACE
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.phys = create_ball(Space, (x, 0), size, elastic)
        self.pos = vec((int(self.phys.body.position.x),
                       int(self.phys.body.position.y)))

    def draw(self, screen):
        pos_x = int(self.phys.body.position.x)
        pos_y = int(self.phys.body.position.y)
        self.pos = vec((pos_x, pos_y))
        self.rect = self.image.get_rect(center=(pos_x, pos_y))
        screen.blit(self.image, self.rect)


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
    create_rectangle_static(space, 400, -100, 800, 200)  # ceiling
    create_rectangle_static(space, -100, 400, 200, 1100)  # left wall
    create_rectangle_static(space, 899, 400, 200, 1100)  # right wall


def collide(Player, Balls):
    for ball in Balls:
        b_pixle_w = ball.image.get_width()
        b_pixle_h = ball.image.get_height()
        b_pos_x = ball.pos.x
        b_pos_y = ball.pos.y

        b_right = b_pos_x + (b_pixle_w / 2)
        b_left = b_pos_x - (b_pixle_w / 2)
        b_top = b_pos_y + (b_pixle_h / 2)
        b_bottom = b_pos_y - (b_pixle_h / 2)

        p_pixle_w = Player.image.get_width()
        p_pixle_h = Player.image.get_height()
        p_pos_x = Player.pos.x
        p_pos_y = Player.pos.y

        p_right = p_pos_x + (p_pixle_w / 2)
        p_left = p_pos_x - (p_pixle_w / 2)
        p_top = p_pos_y + (p_pixle_h / 2)
        p_bottom = p_pos_y - (p_pixle_h / 2)

        if ((((p_right >= b_left) and (p_left < b_left)) or ((p_left <= b_right) and (p_right > b_right)))
                and (((p_top >= b_bottom) and (p_bottom < b_bottom)))):
            Balls.remove(ball)
            return True
    return False


def game_over(Screen, score, total):
    # MusicService.stop_music()
    # MusicService.play_finish_sound()

    GAME_MOUSE_POS = pygame.mouse.get_pos()

    draw_text_outlined(Screen, 400, 100, "GAME OVER", "#b68f40", 50, "#000000", 2)
    draw_text_outlined(Screen, 400, 250, "SCORE", "#f5da0c", 50, "#000000", 2)
    draw_text_outlined(Screen, 400, 300, str(score) + "/" + str(total), "#f5da0c", 50, "#000000", 2)

    if (UpdateLeaderboardBool.update):
        update_leaderboard(CurrentLevel.num, str(score), Username.name)
        UpdateLeaderboardBool.update = False

    PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(400, 400),
                         text_input="PLAY AGAIN", font=get_font(35), base_color="#d7fcd4", hovering_color="White")
    MENU_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(400, 550),
                         text_input="MAIN MENU", font=get_font(35), base_color="#d7fcd4", hovering_color="White")

    for button in [PLAY_BUTTON, MENU_BUTTON]:
        button.changeColor(GAME_MOUSE_POS)
        button.update(Screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if PLAY_BUTTON.checkForInput(GAME_MOUSE_POS):
                return True
            if MENU_BUTTON.checkForInput(GAME_MOUSE_POS):
                MusicService.stop_music()
                GlobalState.GAME_STATE = GameStatus.MAIN_MENU
                return True
    return False


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location, scale):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file).convert()
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
    COS_LEVEL = 6
    LEVEL_SELECT = 7
    LEADERBOARD = 8
    TITLE_SCREEN = 9


class CurrentLevel:
    num = 1


class Username:
    name = ""


class UpdateLeaderboardBool:
    update = bool
    read_bool = bool


class CurrentBackground():
    num = 1


class CurrentPeg():
    num = 1


class CurrentBall():
    num = 1

class CosPeg():
    size = 1

class CosBall():
    size = 1

def CosPegLayout(num):
    match num:
        case 1:
            peg_list = (
                (125, 200),
                (225, 300),
                (175, 450),
                (325, 350),
                (125, 350),
                (275, 650),
                (200, 550),
                (75, 500),
                # Mid
                (400, 500),
                # Left side
                (675, 200),
                (575, 300),
                (625, 450),
                (475, 350),
                (675, 350),
                (525, 650),
                (600, 550),
                (725, 500),
            )
        case 2:
            peg_list = (
                (400, 100),
                (280, 150),
                (520, 150),
                (100, 300),
                (400, 300),
                (700, 300),
                (225, 400),
                (574, 400),
                (150, 500),
                (300, 500),
                (500, 500),
                (650, 500),
            )
        case 3:
            peg_list = (
                (400, 100),
                (280, 150),
                (520, 150),
                (75, 300),
                (150, 225),
                (150, 375),
                (225, 300),
                (400, 300),
                (575, 300),
                (650, 225),
                (650, 375),
                (725, 300),
                (225, 475),
                (574, 475),
                (150, 575),
                (300, 575),
                (500, 575),
                (650, 575),
            )
        case 4:
            peg_list = (
                (125, 200),
                (225, 300),
                (325, 350),
                (125, 350),
                (275, 650),
                (200, 550),

                (325, 225),
                (400, 200),
                (475, 225),

                # Left side
                (675, 200),
                (575, 300),
                (475, 350),
                (675, 350),
                (525, 650),
                (600, 550),
            )
    return peg_list

class GlobalState:
    GAME_STATE = GameStatus.TITLE_SCREEN


class Default_Cosmetics:
    state = bool


class BackGround:
    IMAGE = Background('assets/mm_background.jpg', [0, 0], 1.5)


class BallSurface:
    SURFACE = ball_look('assets/base_ball.png', 0.15)


class PegSurface:
    SURFACE = ball_look('assets/peg.png', 0.28)


def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def draw_text(screen, x, y, string, color, size):
    text = get_font(size).render(string, True, color)
    textbox = text.get_rect(center = (x, y))
    screen.blit(text, textbox)

def draw_text_outlined(screen, x, y, string, text_color, text_size, outline_color, outline_size):
    draw_text(screen, x + outline_size, y + outline_size, string, outline_color, text_size)
    draw_text(screen, x + outline_size, y - outline_size, string, outline_color, text_size)
    draw_text(screen, x - outline_size, y + outline_size, string, outline_color, text_size)
    draw_text(screen, x - outline_size, y - outline_size, string, outline_color, text_size)
    
    draw_text(screen, x, y, string, text_color, text_size)

class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(
                self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(
                self.text_input, True, self.base_color)
