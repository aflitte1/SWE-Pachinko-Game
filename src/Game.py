import pygame
import pymunk
import sys
import components.Backend as bnd
import components.game_phases as GamePhases

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
space = pymunk.Space()

def update_game_display():
    pygame.display.update()

def main():
    while True:
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((0,0,0))
        if bnd.GlobalState.GAME_STATE == bnd.GameStatus.MAIN_MENU:
            GamePhases.main_menu_phase()
        elif bnd.GlobalState.GAME_STATE == bnd.GameStatus.LEVEL_1:
            GamePhases.level_one()
        # elif bnd.GlobalState.GAME_STATE == bnd.GameStatus.LEVEL_2:
        #     GamePhases.level_two()
        # elif bnd.GlabalState.GAME_STATE == bnd.GameStatus.LEVEL_3:
        #     GamePhases.level_three()
        # elif bnd.GlobalState.GAME_STATE == bnd.GameStatus.LEVEL_4:
        #     GamePhases.level_four()
        # elif bnd.GlobalState.GAME_STATE == bnd.GameStatus.COS_MENU:
        #     GamePhases.cos_munu()

        update_game_display()

if __name__ == "__main__":
    main()