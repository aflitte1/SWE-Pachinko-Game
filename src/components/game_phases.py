import sys
import pygame
from pygame.locals import *
from src.components.Backend import *
from src.components.music import MusicService
from typing import Tuple, Any
import time

flags = DOUBLEBUF
pygame.display.init()
pygame.display.set_mode((800, 800), flags)


def title_screen_phase(Screen):
    # BackGround.IMAGE = Background('assets/arcade_cabinet_background.jpg', [0, 0], 2.2)
    # Screen.blit(BackGround.IMAGE.image, BackGround.IMAGE.rect)

    draw_title(Screen, 0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                Username.name = Username.name[:-1]
            elif event.key == pygame.K_RETURN:
                for ii in range(20):
                    BackGround.IMAGE = Background(
                        'assets/mm_background.jpg', [0, 0], 1.5)
                    Screen.blit(BackGround.IMAGE.image, BackGround.IMAGE.rect)
                    draw_title(Screen, ii * 20)
                    pygame.display.update()
                GlobalState.GAME_STATE = GameStatus.MAIN_MENU
            else:
                if (len(Username.name) < 4):
                    Username.name = Username.name + event.unicode


def draw_title(Screen, x_val):
    Screen.blit(pygame.transform.scale(pygame.image.load(
        "assets/arcade_cabinet_left.png"), (800, 800)), [0 - x_val, 0])
    Screen.blit(pygame.transform.scale(pygame.image.load(
        "assets/arcade_cabinet_right.png"), (800, 800)), [0 + x_val, 0])

    match len(Username.name):
        case 0:
            pass
        case 1:
            draw_text(Screen, 400 - 40 - x_val, 500, Username.name + " ", "#b68f40", 40)
        case 2:
            draw_text(Screen, 400 - 40 - x_val, 500, Username.name, "#b68f40", 40)
        case 3:
            draw_text(Screen, 400 - 40 - x_val, 500, Username.name[:2], "#b68f40", 40)
            draw_text(Screen, 400 + 40 + x_val, 500, Username.name[2] + " ", "#b68f40", 40)
        case 4:
            draw_text(Screen, 400 - 40 - x_val, 500, Username.name[:2], "#b68f40", 40)
            draw_text(Screen, 400 + 40 + x_val, 500, Username.name[-2:], "#b68f40", 40)

def main_menu_phase(Screen) -> None:
    MusicService.start_menu_music()
    BackGround.IMAGE = Background('assets/mm_background.jpg', [0, 0], 1.5)
    Screen.blit(BackGround.IMAGE.image, BackGround.IMAGE.rect)
    MENU_MOUSE_POS = pygame.mouse.get_pos()

    draw_text(Screen, 400, 100, "MAIN MENU", "#b68f40", 50)

    LEVEL_SELECT_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(400, 250),
                                 text_input="Level Select", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
    OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(400, 400),
                            text_input="OPTIONS", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
    QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(400, 550),
                         text_input="QUIT", font=get_font(50), base_color="#d7fcd4", hovering_color="White")

    for button in [LEVEL_SELECT_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
        button.changeColor(MENU_MOUSE_POS)
        button.update(Screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if LEVEL_SELECT_BUTTON.checkForInput(MENU_MOUSE_POS):
                GlobalState.GAME_STATE = GameStatus.LEVEL_SELECT
            if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                GlobalState.GAME_STATE = GameStatus.COS_MENU
            if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                pygame.quit()
                sys.exit()


def level_select_phase(Screen):
    BackGround.IMAGE = Background(
        'assets/level_select_background.jpg', [0, 0], 1.5)
    Screen.blit(BackGround.IMAGE.image, BackGround.IMAGE.rect)
    MENU_MOUSE_POS = pygame.mouse.get_pos()

    LEVEL_SELECT_TEXT = "Level Select"

    PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(400, 720),
                         text_input="PLAY", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
    LEADERBOARD_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("assets/leaderboard_button.webp"), (75, 75)), pos=(750, 50),
                                text_input="", font=get_font(1), base_color="#d7fcd4", hovering_color="White")

    BACK_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("assets/back_arrow.png"), (75, 75)), pos=(50, 50),
                         text_input="", font=get_font(1), base_color="#d7fcd4", hovering_color="White")
    RIGHT_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("assets/right_button.png"), (100, 100)), pos=(725, 400),
                          text_input="", font=get_font(1), base_color="#d7fcd4", hovering_color="White")
    LEFT_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("assets/left_button.png"), (100, 100)), pos=(75, 400),
                         text_input="", font=get_font(1), base_color="#d7fcd4", hovering_color="White")

    match CurrentLevel.num:
        case 1:
            LEVEL_SELECT_TEXT = "Level 1"
            Screen.blit(pygame.transform.scale(pygame.image.load(
                "assets/space_background.jpg").convert(), (500, 500)), [150, 150])
        case 2:
            LEVEL_SELECT_TEXT = "Level 2"
            Screen.blit(pygame.transform.scale(pygame.image.load(
                "assets/medieval_background.jpg").convert(), (500, 500)), [150, 150])
        case 3:
            LEVEL_SELECT_TEXT = "Level 3"
            Screen.blit(pygame.transform.scale(pygame.image.load(
                "assets/haunted_background.jpeg").convert(), (500, 500)), [150, 150])
        case 4:
            LEVEL_SELECT_TEXT = "Level 4"
            Screen.blit(pygame.transform.scale(pygame.image.load(
                "assets/city_background.jpg").convert(), (500, 500)), [150, 150])

    draw_text(Screen, 400, 100, LEVEL_SELECT_TEXT, "#b68f40", 50)

    for button in [PLAY_BUTTON, LEADERBOARD_BUTTON, RIGHT_BUTTON, LEFT_BUTTON, BACK_BUTTON]:
        button.changeColor(MENU_MOUSE_POS)
        button.update(Screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                match CurrentLevel.num:
                    case 1:
                        GlobalState.GAME_STATE = GameStatus.LEVEL_1
                    case 2:
                        GlobalState.GAME_STATE = GameStatus.LEVEL_2
                    case 3:
                        GlobalState.GAME_STATE = GameStatus.LEVEL_3
                    case 4:
                        GlobalState.GAME_STATE = GameStatus.LEVEL_4
            elif BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                GlobalState.GAME_STATE = GameStatus.MAIN_MENU
            elif LEADERBOARD_BUTTON.checkForInput(MENU_MOUSE_POS):
                GlobalState.GAME_STATE = GameStatus.LEADERBOARD
            elif RIGHT_BUTTON.checkForInput(MENU_MOUSE_POS):
                if CurrentLevel.num != 4:
                    CurrentLevel.num = CurrentLevel.num + 1
            elif LEFT_BUTTON.checkForInput(MENU_MOUSE_POS):
                if CurrentLevel.num != 1:
                    CurrentLevel.num = CurrentLevel.num - 1


def leaderboard_phase(Screen):
    BackGround.IMAGE = Background(
        'assets/Leaderboard_background.jpg', [0, 0], 1.5)
    Screen.blit(BackGround.IMAGE.image, BackGround.IMAGE.rect)
    MENU_MOUSE_POS = pygame.mouse.get_pos()

    draw_text(Screen, 400, 100, "Leaderboard", "#b68f40", 50)

    BACK_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("assets/back_arrow.png"), (75, 75)), pos=(50, 50),
                         text_input="", font=get_font(1), base_color="#d7fcd4", hovering_color="White")

    for ii in range(len(scores[CurrentLevel.num-1])):
        display_string = format_leaderboard_display(
            scores[CurrentLevel.num-1][ii], ii)

        draw_text(Screen, 400, 150 + ii * 50, display_string, "#b68f40", 25)

    if (last_score[CurrentLevel.num - 1] != []):
        display_string = format_leaderboard_display(
            last_score[CurrentLevel.num - 1], -1)

        draw_text(Screen, 400, 675, "Last Score", "#b68f40", 40)
        draw_text(Screen, 400, 750, display_string, "#b68f40", 25)

    for button in [BACK_BUTTON]:
        button.changeColor(MENU_MOUSE_POS)
        button.update(Screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                GlobalState.GAME_STATE = GameStatus.LEVEL_SELECT


def level_one() -> None:
    # Background Image Setup
    # The background image will eventually become a global variable dependent on cosmetics
    MusicService.stop_music()
    MusicService.start_level_1_music()
    BallSurface.SURFACE = ball_look('assets/space_ball.png', 0.05)
    PegSurface.SURFACE = ball_look('assets/space_peg.png', 0.05)
    BackGround.IMAGE = Background('assets/space_background.jpg', [0, 0], 1.0)


def level_two(ball_size, peg_size) -> None:
    MusicService.stop_music()
    MusicService.start_level_2_music()
    BallSurface.SURFACE = ball_look(
        'assets/medieval_ball.png', ball_size / 1439 * 2)
    PegSurface.SURFACE = ball_look(
        'assets/medieval_peg.png', peg_size / 812 * 2)
    BackGround.IMAGE = Background(
        'assets/medieval_background.jpg', [0, 0], 800 / 1776)


def level_three() -> None:
    MusicService.stop_music()
    MusicService.start_level_3_music()
    BackGround.IMAGE = Background(
        'assets/haunted_background.jpeg', [-8, 0], 0.56)
    BallSurface.SURFACE = ball_look('assets/haunted_ball.png', 0.10)
    PegSurface.SURFACE = ball_look('assets/haunted_peg.png', 0.20)


def level_four() -> None:
    MusicService.stop_music()
    MusicService.start_level_4_music()
    BackGround.IMAGE = Background('assets/city_background.jpg', [-250, 0], .7)
    BallSurface.SURFACE = ball_look('assets/city_ball.png', 0.06)
    PegSurface.SURFACE = ball_look('assets/city_peg.png', 0.10)


def cos_menu(Screen):
    BackGround.IMAGE = Background(
        'assets/level_select_background.jpg', [0, 0], 1.5)
    Screen.blit(BackGround.IMAGE.image, BackGround.IMAGE.rect)
    COS_MOUSE_POS = pygame.mouse.get_pos()

    draw_text(Screen, 400, 50, "Cosmetics", "#b68f40", 50)
    draw_text(Screen, 175, 200, "Background", "#b68f40", 33)
    draw_text(Screen, 200, 350, "Peg", "#b68f40", 50)
    draw_text(Screen, 200, 500, "Ball", "#b68f40", 50)

    RIGHT_BUTTON1 = Button(image=pygame.transform.scale(pygame.image.load("assets/right_button.png"), (100, 100)), pos=(725, 200),
                           text_input="", font=get_font(1), base_color="#d7fcd4", hovering_color="White")
    LEFT_BUTTON1 = Button(image=pygame.transform.scale(pygame.image.load("assets/left_button.png"), (100, 100)), pos=(400, 200),
                          text_input="", font=get_font(1), base_color="#d7fcd4", hovering_color="White")
    RIGHT_BUTTON2 = Button(image=pygame.transform.scale(pygame.image.load("assets/right_button.png"), (100, 100)), pos=(725, 350),
                           text_input="", font=get_font(1), base_color="#d7fcd4", hovering_color="White")
    LEFT_BUTTON2 = Button(image=pygame.transform.scale(pygame.image.load("assets/left_button.png"), (100, 100)), pos=(400, 350),
                          text_input="", font=get_font(1), base_color="#d7fcd4", hovering_color="White")
    RIGHT_BUTTON3 = Button(image=pygame.transform.scale(pygame.image.load("assets/right_button.png"), (100, 100)), pos=(725, 500),
                           text_input="", font=get_font(1), base_color="#d7fcd4", hovering_color="White")
    LEFT_BUTTON3 = Button(image=pygame.transform.scale(pygame.image.load("assets/left_button.png"), (100, 100)), pos=(400, 500),
                          text_input="", font=get_font(1), base_color="#d7fcd4", hovering_color="White")
    PLAY_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(400, 625),
                         text_input="PLAY", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
    BACK_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(400, 750),
                         text_input="BACK", font=get_font(50), base_color="#d7fcd4", hovering_color="White")

    for button in [RIGHT_BUTTON1, LEFT_BUTTON1, RIGHT_BUTTON2, LEFT_BUTTON2, RIGHT_BUTTON3, LEFT_BUTTON3, PLAY_BUTTON, BACK_BUTTON]:
        button.changeColor(COS_MOUSE_POS)
        button.update(Screen)

    match CurrentBackground.num:
        case 1:
            Screen.blit(pygame.transform.scale(pygame.image.load(
                "assets/space_background.jpg").convert(), (150, 150)), [500, 125])
            BackGround.IMAGE = Background(
                'assets/space_background.jpg', [0, 0], 1.0)
        case 2:
            Screen.blit(pygame.transform.scale(pygame.image.load(
                "assets/medieval_background.jpg").convert(), (150, 150)), [500, 125])
            BackGround.IMAGE = Background('assets/medieval_background.jpg', [0, 0], 800 / 1776)
        case 3:
            Screen.blit(pygame.transform.scale(pygame.image.load(
                "assets/haunted_background.jpeg").convert(), (150, 150)), [500, 125])
            BackGround.IMAGE = Background(
                'assets/haunted_background.jpeg', [-8, 0], 0.56)
        case 4:
            Screen.blit(pygame.transform.scale(pygame.image.load("assets/city_background.jpg").convert(), (150, 150)), [500, 125])
            BackGround.IMAGE = Background('assets/city_background.jpg', [-250, 0], .7)

    match CurrentPeg.num:
        case 1:
            Screen.blit(pygame.transform.scale(pygame.image.load(
                "assets/space_peg.png"), (150, 150)), [500, 275])
            PegSurface.SURFACE = ball_look('assets/space_peg.png', 0.05)
            CosPeg.size = 10
        case 2:
            Screen.blit(pygame.transform.scale(pygame.image.load(
                "assets/medieval_peg.png"), (150, 150)), [500, 275])  # REPLACE WITH LEVEL 2 PEG
            PegSurface.SURFACE = ball_look('assets/medieval_peg.png', 20 / 812 * 2)
            CosPeg.size = 20
        case 3:
            Screen.blit(pygame.transform.scale(pygame.image.load(
                "assets/haunted_peg.png"), (150, 150)), [500, 275])
            PegSurface.SURFACE = ball_look('assets/haunted_peg.png', 0.20)
            CosPeg.size = 25
        case 4:
            Screen.blit(pygame.transform.scale(pygame.image.load(
                "assets/city_peg.png"), (150, 150)), [500, 275])  # REPLACE WITH LEVEL 4 PEG
            PegSurface.SURFACE = ball_look('assets/city_peg.png', 0.10)
            CosPeg.size = 10

    match CurrentBall.num:
        case 1:
            Screen.blit(pygame.transform.scale(pygame.image.load(
                "assets/space_ball.png"), (150, 150)), [500, 425])
            BallSurface.SURFACE = ball_look('assets/space_ball.png', 0.05)
            CosBall.size = 25
        case 2:
            Screen.blit(pygame.transform.scale(pygame.image.load(
                "assets/medieval_ball.png"), (150, 150)), [500, 425])  # REPLACE WITH LEVEL 2 BALL
            BallSurface.SURFACE = ball_look('assets/medieval_ball.png', 25 / 1439 * 2)
            CosBall.size = 25
        case 3:
            Screen.blit(pygame.transform.scale(pygame.image.load(
                "assets/haunted_ball.png"), (150, 150)), [500, 425])
            BallSurface.SURFACE = ball_look('assets/haunted_ball.png', 0.10)
            CosBall.size = 20
        case 4:
            Screen.blit(pygame.transform.scale(pygame.image.load(
                "assets/city_ball.png"), (150, 150)), [500, 425])  # REPLACE WITH LEVEL 4 BALL
            BallSurface.SURFACE = ball_look('assets/city_ball.png', 0.06)
            CosBall.size = 25

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if PLAY_BUTTON.checkForInput(COS_MOUSE_POS):
                GlobalState.GAME_STATE = GameStatus.COS_LEVEL
            elif BACK_BUTTON.checkForInput(COS_MOUSE_POS):
                GlobalState.GAME_STATE = GameStatus.MAIN_MENU
            elif RIGHT_BUTTON1.checkForInput(COS_MOUSE_POS):
                if CurrentBackground.num != 4:
                    CurrentBackground.num = CurrentBackground.num + 1
            elif LEFT_BUTTON1.checkForInput(COS_MOUSE_POS):
                if CurrentBackground.num != 1:
                    CurrentBackground.num = CurrentBackground.num - 1
            elif RIGHT_BUTTON2.checkForInput(COS_MOUSE_POS):
                if CurrentPeg.num != 4:
                    CurrentPeg.num = CurrentPeg.num + 1
            elif LEFT_BUTTON2.checkForInput(COS_MOUSE_POS):
                if CurrentPeg.num != 1:
                    CurrentPeg.num = CurrentPeg.num - 1
            elif RIGHT_BUTTON3.checkForInput(COS_MOUSE_POS):
                if CurrentBall.num != 4:
                    CurrentBall.num = CurrentBall.num + 1
            elif LEFT_BUTTON3.checkForInput(COS_MOUSE_POS):
                if CurrentBall.num != 1:
                    CurrentBall.num = CurrentBall.num - 1
