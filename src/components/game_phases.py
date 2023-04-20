import sys
import pygame
from components.Backend import *
import pygame_menu
from typing import Tuple, Any


def main_menu_phase(Screen):
    BackGround.IMAGE = Background('assets/mm_background.jpg', [0, 0], 1.5)
    Screen.blit(BackGround.IMAGE.image, BackGround.IMAGE.rect)
    MENU_MOUSE_POS = pygame.mouse.get_pos()
    MENU_TEXT = get_font(50).render("MAIN MENU", True, "#b68f40")
    MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))

    LEVEL_SELECT_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(400, 250), 
                        text_input="Level Select", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
    OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(400, 400), 
                         text_input="OPTIONS", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
    QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(400, 550), 
                        text_input="QUIT", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
    Screen.blit(MENU_TEXT, MENU_RECT)

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
    BackGround.IMAGE = Background('assets/level_select_background.jpg', [0, 0], 1.5)
    Screen.blit(BackGround.IMAGE.image, BackGround.IMAGE.rect)
    MENU_MOUSE_POS = pygame.mouse.get_pos()
    LEVEL_SELECT_TEXT = get_font(50).render("Level Select", True, "#b68f40")
    

    PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(400, 720), 
                        text_input="PLAY", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
    LEADERBOARD_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("assets/leaderboard_button.webp"),(75,75)), pos=(750, 50), 
                        text_input="", font=get_font(1), base_color="#d7fcd4", hovering_color="White")
                                
    BACK_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("assets/back_arrow.png"),(75,75)), pos=(50, 50), 
                        text_input="", font=get_font(1), base_color="#d7fcd4", hovering_color="White")
    RIGHT_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("assets/right_button.png"),(100,100)), pos=(725, 400),
                          text_input="", font=get_font(1), base_color="#d7fcd4", hovering_color="White")
    LEFT_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("assets/left_button.png"),(100,100)), pos=(75, 400),
                         text_input="", font=get_font(1), base_color="#d7fcd4", hovering_color="White")
    

    match CurrentLevel.num:
                    case 1:
                        LEVEL_SELECT_TEXT = get_font(50).render("Level 1", True, "#b68f40")
                        Screen.blit(pygame.transform.scale(pygame.image.load("assets/space_background.jpg"),(500,500)), [150,150])
                    case 2:
                        LEVEL_SELECT_TEXT = get_font(50).render("Level 2", True, "#b68f40")
                        Screen.blit(pygame.transform.scale(pygame.image.load("assets/2.jpg"),(500,500)), [150,150])#REPLACE WITH LEVEL 2 BACKGROUND
                    case 3:
                        LEVEL_SELECT_TEXT = get_font(50).render("Level 3", True, "#b68f40")
                        Screen.blit(pygame.transform.scale(pygame.image.load("assets/haunted_background.jpeg"),(500,500)), [150,150])
                    case 4:
                        LEVEL_SELECT_TEXT = get_font(50).render("Level 4", True, "#b68f40")
                        Screen.blit(pygame.transform.scale(pygame.image.load("assets/4.jpg"),(500,500)), [150,150])#REPLACE WITH LEVEL 4 BACKGROUND

    LEVEL_SELECT_RECT = LEVEL_SELECT_TEXT.get_rect(center=(400, 100))
    Screen.blit(LEVEL_SELECT_TEXT, LEVEL_SELECT_RECT)

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
                pass
            elif RIGHT_BUTTON.checkForInput(MENU_MOUSE_POS):
                if CurrentLevel.num != 4:
                    CurrentLevel.num = CurrentLevel.num + 1
                    print("Current Level is now", CurrentLevel.num)
            elif LEFT_BUTTON.checkForInput(MENU_MOUSE_POS):
                if CurrentLevel.num != 1:
                    CurrentLevel.num = CurrentLevel.num - 1
                    print("Current Level is now", CurrentLevel.num)


def level_one():
    # Background Image Setup
    # The background image will eventually become a global variable dependent on cosmetics
    BallSurface.SURFACE = ball_look('assets/space_ball.png', 0.075)
    PegSurface.SURFACE = ball_look('assets/space_peg.png', 0.1)
    BackGround.IMAGE = Background('assets/space_background.jpg', [0, 0], 1.0)


def level_two():
    BackGround.IMAGE = Background('assets/2.jpg', [0, 0], 1.5)


def level_three():
    BackGround.IMAGE = Background('assets/haunted_background.jpeg', [-8, 0], 0.56)
    BallSurface.SURFACE = ball_look('assets/haunted_ball.png', 0.15)
    PegSurface.SURFACE = ball_look('assets/haunted_peg.png', 0.40)


def level_four():
    BackGround.IMAGE = Background('assets/4.jpg', [0, 0], 1.5)


def cos_menu(Screen):
    def set_background(selected: Tuple, file: Any, location: Any, scale: Any) -> None:
        BackGround.IMAGE = Background(file, location, scale)

    def set_peg(selected: Tuple, file: Any, scale: Any) -> None:
        PegSurface.SURFACE = ball_look(file, scale)

    def set_ball(selected: Tuple, file: Any, scale: Any) -> None:
        BallSurface.SURFACE = ball_look(file, scale)
    
    def menu_play():
        menu.disable()
        GlobalState.GAME_STATE = GameStatus.LEVEL_4
    
    def menu_quit():
        menu.disable()
        GlobalState.GAME_STATE = GameStatus.MAIN_MENU
    
    #intializing selections
    BallSurface.SURFACE = ball_look('assets/space_ball.png', 0.075)
    PegSurface.SURFACE = ball_look('assets/space_peg.png', 0.1)
    BackGround.IMAGE = Background('assets/space_background.jpg', [0, 0], 1.0)

    menu = pygame_menu.Menu(
        height=800,
        theme=pygame_menu.themes.THEME_BLUE,
        title='Cosemtics',
        width=800
    )

    menu.add.selector('Background: ', [('Space', 'assets/space_background.jpg', [0, 0], 1.0), ('Haunted', 'assets/haunted_background.jpeg', [-8, 0], 0.56)], onchange=set_background)
    menu.add.selector('Peg: ', [('Space', 'assets/space_peg.png', 0.1), ('Haunted', 'assets/haunted_peg.png', 0.40)], onchange=set_peg)
    menu.add.selector('Ball: ', [('Space', 'assets/space_ball.png', 0.075), ('Haunted', 'assets/haunted_ball.png', 0.15)], onchange=set_ball)
    menu.add.button('Play', menu_play)
    menu.add.button('Back', menu_quit)
    menu.mainloop(Screen)
