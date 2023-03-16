import pygame
import pymunk
import sys
import components.Backend as bnd
import components.game_phases as GamePhases

pygame.init()
Screen = pygame.display.set_mode((800, 800))
Clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0, 500)  # X gravity, Y gravity


def update_game_display():
    pygame.display.update()
    Clock.tick(120)
    space.step(1/50)  # Updating time for physics sim


Balls = []


def main():
    while True:
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        Screen.fill((217, 217, 217))
        Screen.blit(bnd.BackGround.IMAGE.image, bnd.BackGround.IMAGE.rect)
        bnd.draw_ball(Screen, Balls)
        update_game_display()

        if bnd.GlobalState.GAME_STATE == bnd.GameStatus.MAIN_MENU:
            GamePhases.main_menu_phase()
        elif bnd.GlobalState.GAME_STATE == bnd.GameStatus.LEVEL_1:
            GamePhases.level_one()
        elif bnd.GlobalState.GAME_STATE == bnd.GameStatus.LEVEL_2:
            GamePhases.level_two()
        # elif bnd.GlabalState.GAME_STATE == bnd.GameStatus.LEVEL_3:
        #     GamePhases.level_three()
        # elif bnd.GlobalState.GAME_STATE == bnd.GameStatus.LEVEL_4:
        #     GamePhases.level_four()
        # elif bnd.GlobalState.GAME_STATE == bnd.GameStatus.COS_MENU:
        #     GamePhases.cos_munu()


if __name__ == "__main__":
    main()
