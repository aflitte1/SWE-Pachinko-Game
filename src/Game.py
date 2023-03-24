import pygame
import pymunk
import sys
import numpy as np
import components.Backend as bnd
import components.game_phases as GamePhases
from components.player import *

pygame.init()
Screen = pygame.display.set_mode((800, 800))
Clock = pygame.time.Clock()
Space = pymunk.Space()
#Space.gravity = (0, 500)  # X gravity, Y gravity


def update_game_display():
    pygame.display.update()
    Clock.tick(120)
    Space.step(1/50)  # Updating time for physics sim


def main():
    Balls = []
    Pegs = []
    ball_count = 0
    ball_pos = 0
    level_start = False
    bnd.create_borders(Space)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        match bnd.GlobalState.GAME_STATE:
            case bnd.GameStatus.MAIN_MENU:
                GamePhases.main_menu_phase()

            case bnd.GameStatus.LEVEL_1:
                ball_max = 50
                GamePhases.level_one()
                if not level_start:
                    Pegs.append(bnd.create_peg(Space, (500, 500)))
                    level_start = True

                if ball_count <= ball_max:
                    spawn_ball = np.random.randint(0, 50)
                    if spawn_ball == 0:
                        Balls.append(bnd.create_ball(Space, (400, 0)))
                        ball_count += 1

            case bnd.GameStatus.LEVEL_2:
                GamePhases.level_two()

            case bnd.GameStatus.LEVEL_3:
                ball_max = 29
                Space.gravity = (0, 300)
                if not level_start:
                    GamePhases.level_three()
                    Pegs.append(bnd.create_peg(Space, (465, 450), 43, 0.5))
                    Pegs.append(bnd.create_peg(Space, (310, 600), 43, 0.5))
                    Pegs.append(bnd.create_peg(Space, (130, 400), 43, 0.5))
                    Pegs.append(bnd.create_peg(Space, (665, 550), 43, 0.5))
                    Pegs.append(bnd.create_peg(Space, (325, 225), 43, 0.5))
                    Pegs.append(bnd.create_peg(Space, (625, 250), 43, 0.5))
                    level_start = True

                if ball_count <= ball_max:
                    spawn_ball = np.random.randint(0, 50)
                    if spawn_ball == 0:     
                        if ball_count % 10 == 0:
                            ball_pos += 180 
                        Balls.append(bnd.create_ball(Space, (ball_pos, 0), 43, 1))
                        ball_count += 1

            case bnd.GameStatus.LEVEL_4:
                GamePhases.cos_menu()

        Screen.fill((217, 217, 217))
        Screen.blit(bnd.BackGround.IMAGE.image, bnd.BackGround.IMAGE.rect)
        bnd.draw_ball(Screen, Balls)
        bnd.draw_peg(Screen, Pegs)
        update_game_display()


if __name__ == "__main__":
    main()
