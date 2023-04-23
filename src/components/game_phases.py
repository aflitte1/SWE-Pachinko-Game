import sys
import pygame
from src.components.Backend import *
from src.components.music import MusicService
import pygame_menu
from typing import Tuple, Any
import time

def title_screen_phase(Screen):
    #BackGround.IMAGE = Background('assets/arcade_cabinet_background.jpg', [0, 0], 2.2)
    #Screen.blit(BackGround.IMAGE.image, BackGround.IMAGE.rect)

    draw_title(Screen , 0)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                Username.name = Username.name[:-1]
                print("In backspace")
            elif event.key == pygame.K_RETURN:
                for ii in range(20):
                    BackGround.IMAGE = Background('assets/mm_background.jpg', [0, 0], 1.5)
                    Screen.blit(BackGround.IMAGE.image, BackGround.IMAGE.rect)
                    draw_title(Screen, ii * 20)
                    pygame.display.update()
                GlobalState.GAME_STATE = GameStatus.MAIN_MENU
            else:
                print("Trying to add a character")
                if(len(Username.name) < 4):
                    Username.name = Username.name + event.unicode

def draw_title(Screen, x_val):
    Screen.blit(pygame.transform.scale(pygame.image.load("assets/arcade_cabinet_left.png"),(800,800)), [0 - x_val,0])
    Screen.blit(pygame.transform.scale(pygame.image.load("assets/arcade_cabinet_right.png"),(800,800)), [0 + x_val,0])

    #NAME_REGISTRAITON_TEXT1 = get_font(30).render("ENTER", True, "#b68f40")
    #NAME_REGISTRAITON_RECT1 = NAME_REGISTRAITON_TEXT1.get_rect(center=(400 - 75 - x_val, 400))
    #NAME_REGISTRAITON_TEXT2 = get_font(30).render(" NAME", True, "#b68f40")
    #NAME_REGISTRAITON_RECT2 = NAME_REGISTRAITON_TEXT2.get_rect(center=(400 + 75 + x_val, 400))

    match len(Username.name):
        case 0:
            pass
        case 1:
            USER_NAME_TEXT1 = get_font(40).render(Username.name + " ", True, "#b68f40")        ###### NEED TO CHANGE THIS FOR SURE
            USER_NAME_RECT1 = USER_NAME_TEXT1.get_rect(center=(400 - 40 - x_val, 500))
            Screen.blit(USER_NAME_TEXT1, USER_NAME_RECT1)
        case 2:
            USER_NAME_TEXT1 = get_font(40).render(Username.name, True, "#b68f40")        ###### NEED TO CHANGE THIS FOR SURE
            USER_NAME_RECT1 = USER_NAME_TEXT1.get_rect(center=(400 - 40 - x_val, 500))
            Screen.blit(USER_NAME_TEXT1, USER_NAME_RECT1)
        case 3:
            USER_NAME_TEXT1 = get_font(40).render(Username.name[:2], True, "#b68f40")        ###### NEED TO CHANGE THIS FOR SURE
            USER_NAME_RECT1 = USER_NAME_TEXT1.get_rect(center=(400 - 40 - x_val, 500))
            USER_NAME_TEXT2 = get_font(40).render(Username.name[2] + " ", True, "#b68f40")        ###### NEED TO CHANGE THIS FOR SURE
            USER_NAME_RECT2 = USER_NAME_TEXT2.get_rect(center=(400 + 40 + x_val, 500))
            Screen.blit(USER_NAME_TEXT1, USER_NAME_RECT1)
            Screen.blit(USER_NAME_TEXT2, USER_NAME_RECT2)
        case 4:
            USER_NAME_TEXT1 = get_font(40).render(Username.name[:2], True, "#b68f40")        ###### NEED TO CHANGE THIS FOR SURE
            USER_NAME_RECT1 = USER_NAME_TEXT1.get_rect(center=(400 - 40 - x_val, 500))
            USER_NAME_TEXT2 = get_font(40).render(Username.name[-2:], True, "#b68f40")        ###### NEED TO CHANGE THIS FOR SURE
            USER_NAME_RECT2 = USER_NAME_TEXT2.get_rect(center=(400 + 40 + x_val, 500))
            Screen.blit(USER_NAME_TEXT1, USER_NAME_RECT1)
            Screen.blit(USER_NAME_TEXT2, USER_NAME_RECT2)
    
    #USER_NAME_slot_TEXT = get_font(40).render("____", True, "#b68f40")        ###### NEED TO CHANGE THIS FOR SURE
    #USER_NAME_slot_RECT = USER_NAME_slot_TEXT.get_rect(center=(400, 510))
    #Screen.blit(USER_NAME_slot_TEXT, USER_NAME_slot_RECT)


    #Screen.blit(NAME_REGISTRAITON_TEXT1, NAME_REGISTRAITON_RECT1)
    #Screen.blit(NAME_REGISTRAITON_TEXT2, NAME_REGISTRAITON_RECT2)
    

    





def main_menu_phase(Screen) -> None:
    MusicService.start_menu_music()
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
                GlobalState.GAME_STATE = GameStatus.LEADERBOARD
            elif RIGHT_BUTTON.checkForInput(MENU_MOUSE_POS):
                if CurrentLevel.num != 4:
                    CurrentLevel.num = CurrentLevel.num + 1
            elif LEFT_BUTTON.checkForInput(MENU_MOUSE_POS):
                if CurrentLevel.num != 1:
                    CurrentLevel.num = CurrentLevel.num - 1

def leaderboard_phase(Screen):
    BackGround.IMAGE = Background('assets/Leaderboard_background.jpg', [0, 0], 1.5)
    Screen.blit(BackGround.IMAGE.image, BackGround.IMAGE.rect)
    MENU_MOUSE_POS = pygame.mouse.get_pos()
    LEADERBOARD_TEXT = get_font(50).render("Leaderboard", True, "#b68f40")
    LEVEL_SELECT_RECT = LEADERBOARD_TEXT.get_rect(center=(400, 100))
    Screen.blit(LEADERBOARD_TEXT, LEVEL_SELECT_RECT)

    BACK_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("assets/back_arrow.png"),(75,75)), pos=(50, 50), 
                        text_input="", font=get_font(1), base_color="#d7fcd4", hovering_color="White")

    for ii in range(len(scores[CurrentLevel.num-1])):
        display_string = format_leaderboard_display(scores[CurrentLevel.num-1][ii], ii)
        DISPLAY_STRING_TEXT = get_font(25).render(display_string, True, "#b68f40")
        DISPLAY_STRING_RECT = DISPLAY_STRING_TEXT.get_rect(center=(400, 150 + ii * 50))
        Screen.blit(DISPLAY_STRING_TEXT, DISPLAY_STRING_RECT)
    if(last_score[CurrentLevel.num - 1] != []):
        display_string = format_leaderboard_display(last_score[CurrentLevel.num - 1], -1)
        LAST_SCORE_TEXT = get_font(40).render("Last Score", True, "#b68f40")
        LAST_SCORE_RECT = LAST_SCORE_TEXT.get_rect(center=(400, 675))
        DISPLAY_STRING_TEXT = get_font(25).render(display_string, True, "#b68f40")
        DISPLAY_STRING_RECT = DISPLAY_STRING_TEXT.get_rect(center=(400, 750))
        Screen.blit(LAST_SCORE_TEXT, LAST_SCORE_RECT)
        Screen.blit(DISPLAY_STRING_TEXT, DISPLAY_STRING_RECT)
        

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
    if Default_Cosmetics.state:
        BallSurface.SURFACE = ball_look('assets/space_ball.png', 0.075)
        PegSurface.SURFACE = ball_look('assets/space_peg.png', 0.1)
        BackGround.IMAGE = Background('assets/space_background.jpg', [0, 0], 1.0)


def level_two() -> None:
    MusicService.stop_music()
    MusicService.start_level_2_music()
    if Default_Cosmetics.state:
        BackGround.IMAGE = Background('assets/2.jpg', [0, 0], 1.5)


def level_three() -> None:
    MusicService.stop_music()
    MusicService.start_level_3_music()
    if Default_Cosmetics.state:
        BackGround.IMAGE = Background('assets/haunted_background.jpeg', [-8, 0], 0.56)
        BallSurface.SURFACE = ball_look('assets/haunted_ball.png', 0.15)
        PegSurface.SURFACE = ball_look('assets/haunted_peg.png', 0.40)


def level_four() -> None:
    MusicService.stop_music()
    MusicService.start_level_4_music()
    if Default_Cosmetics.state:
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
        GlobalState.GAME_STATE = GameStatus.LEVEL_3
    
    def menu_quit():
        menu.disable()
        GlobalState.GAME_STATE = GameStatus.MAIN_MENU

    def default_switch(state: bool) -> None:
        Default_Cosmetics.state = state
    
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
    if Default_Cosmetics.state:
        menu.add.toggle_switch(title='Set Default Cosmetics', default=True, onchange=default_switch)
    else:
        menu.add.toggle_switch(title='Set Default Cosmetics', default=False, onchange=default_switch)
    menu.add.selector('Background: ', [('Space', 'assets/space_background.jpg', [0, 0], 1.0), ('Haunted', 'assets/haunted_background.jpeg', [-8, 0], 0.56)], onchange=set_background)
    menu.add.selector('Peg: ', [('Space', 'assets/space_peg.png', 0.1), ('Haunted', 'assets/haunted_peg.png', 0.40)], onchange=set_peg)
    menu.add.selector('Ball: ', [('Space', 'assets/space_ball.png', 0.075), ('Haunted', 'assets/haunted_ball.png', 0.15)], onchange=set_ball)
    menu.add.button('Play', menu_play)
    menu.add.button('Back', menu_quit)
    menu.mainloop(Screen)
