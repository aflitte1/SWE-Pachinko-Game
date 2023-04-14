import sys
import pygame
from components.Backend import *
import pygame_menu
from typing import Tuple, Any


def main_menu_phase(Screen) -> None:
    BackGround.IMAGE = Background('assets/mm_background.jpg', [0, 0], 1.5)
    Screen.blit(BackGround.IMAGE.image, BackGround.IMAGE.rect)
    MENU_MOUSE_POS = pygame.mouse.get_pos()
    MENU_TEXT = get_font(50).render("MAIN MENU", True, "#b68f40")
    MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))

    PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(400, 250), 
                        text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
    OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(400, 400), 
                         text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
    QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(400, 550), 
                        text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
    Screen.blit(MENU_TEXT, MENU_RECT)

    for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
        button.changeColor(MENU_MOUSE_POS)
        button.update(Screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                GlobalState.GAME_STATE = GameStatus.LEVEL_3
            if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                GlobalState.GAME_STATE = GameStatus.COS_MENU
            if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                pygame.quit()
                sys.exit()


def level_one() -> None:
    # Background Image Setup
    # The background image will eventually become a global variable dependent on cosmetics
    if DEFAULT:
        BallSurface.SURFACE = ball_look('assets/space_ball.png', 0.075)
        PegSurface.SURFACE = ball_look('assets/space_peg.png', 0.1)
        BackGround.IMAGE = Background('assets/space_background.jpg', [0, 0], 1.0)


def level_two() -> None:
    if DEFAULT:
        BackGround.IMAGE = Background('assets/2.jpg', [0, 0], 1.5)


def level_three():
    if DEFAULT:
        BackGround.IMAGE = Background('assets/haunted_background.jpeg', [-8, 0], 0.56)
        BallSurface.SURFACE = ball_look('assets/haunted_ball.png', 0.15)
        PegSurface.SURFACE = ball_look('assets/haunted_peg.png', 0.40)


def level_four() -> None:
    if DEFAULT:
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

    def default_switch(state: bool) -> None:
        DEFAULT = state
    
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

    menu.add.toggle_switch(title='Set Default Cosmetics', default=0, onchange=default_switch)
    menu.add.selector('Background: ', [('Space', 'assets/space_background.jpg', [0, 0], 1.0), ('Haunted', 'assets/haunted_background.jpeg', [-8, 0], 0.56)], onchange=set_background)
    menu.add.selector('Peg: ', [('Space', 'assets/space_peg.png', 0.1), ('Haunted', 'assets/haunted_peg.png', 0.40)], onchange=set_peg)
    menu.add.selector('Ball: ', [('Space', 'assets/space_ball.png', 0.075), ('Haunted', 'assets/haunted_ball.png', 0.15)], onchange=set_ball)
    menu.add.button('Play', menu_play)
    menu.add.button('Back', menu_quit)
    menu.mainloop(Screen)
