import pygame
import pymunk
import sys
import numpy as np
import src.components.Backend as bnd
import src.components.game_phases as GamePhases
from src.components.player import *
from src.components.music import MusicService
from pygame.locals import *

flags = DOUBLEBUF
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
pygame.event.set_allowed([QUIT, MOUSEBUTTONDOWN, KEYDOWN])
Screen = pygame.display.set_mode((800, 800), flags)
Clock = pygame.time.Clock()
Space = pymunk.Space()


# Sprite Setup
P1 = Player()

all_balls = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)


def update_game_display():
    pygame.display.update()
    Clock.tick(80)
    Space.step(1/50)  # Updating time for physics sim


def main():
    # Helper function to spawn all pegs in a level
    def spawn_pegs(pos_list, size, elastic):
        for pos in pos_list:
            Pegs.append(bnd.create_peg(Space, pos, size, elastic))

    Balls = []
    Pegs = []
    ball_max = 29
    ball_count = 0
    ball_pos = 0
    level_start = False
    score = 0
    bnd.read_to_file()
    bnd.UpdateLeaderboardBool.update = True
    bnd.Default_Cosmetics.state = True
    bnd.create_borders(Space)
    while (1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        match bnd.GlobalState.GAME_STATE:
            case bnd.GameStatus.TITLE_SCREEN:
                GamePhases.title_screen_phase(Screen)
            case bnd.GameStatus.MAIN_MENU:
                GamePhases.main_menu_phase(Screen)
            case bnd.GameStatus.LEVEL_SELECT:
                GamePhases.level_select_phase(Screen)
            case bnd.GameStatus.LEADERBOARD:
                GamePhases.leaderboard_phase(Screen)
            case bnd.GameStatus.LEVEL_1:
                Space.gravity = (0, 80)
                if not level_start:
                    GamePhases.level_one()

                    spawn_pegs(
                        pos_list = (
                            # Right side
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
                        ),
                        size = 10,
                        elastic = 0.5
                    )

                    level_start = True
                    bnd.UpdateLeaderboardBool.update = True

                if ball_count <= ball_max:
                    spawn_ball = np.random.randint(0, 125)
                    if spawn_ball == 0:
                        x_pos = np.random.uniform(20, 780)
                        ball_sprite = bnd.Ball(x_pos, Space, 26.6, 1.5)
                        Balls.append(ball_sprite)
                        all_balls.add(ball_sprite)
                        ball_count += 1

                if bnd.collide(P1, Balls):
                    MusicService.score_increase()
                    score += 1

            case bnd.GameStatus.LEVEL_2:
                Space.gravity = (0, 120)

                if not level_start:
                    level_start = True

                    ball_size = 25
                    peg_size = 20

                    GamePhases.level_two(ball_size=ball_size, peg_size=peg_size)

                    spawn_pegs(
                        pos_list = (
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
                        ),
                        size = peg_size,
                        elastic = 0.65
                    )

                if ball_count <= ball_max:
                    spawn_ball = np.random.randint(0, 250)
                    if spawn_ball == 0:
                        x_pos = np.random.uniform(20, 780)
                        ball_sprite = bnd.Ball(
                            x_pos, Space, ball_size, 1)
                        Balls.append(ball_sprite)
                        all_balls.add(ball_sprite)
                        ball_count += 1

                if bnd.collide(P1, Balls):
                    MusicService.score_increase()
                    score += 1

            case bnd.GameStatus.LEVEL_3:
                Space.gravity = (0, 200)
                if not level_start:
                    GamePhases.level_three()
                    spawn_pegs(
                        pos_list = (
                            (395, 100),
                            (275, 150),
                            (515, 150),
                            (70, 300),
                            (145, 225),
                            (145, 375),
                            (220, 300),
                            (395, 300),
                            (570, 300),
                            (645, 225),
                            (645, 375),
                            (720, 300),
                            (220, 475),
                            (569, 475),
                            (145, 575),
                            (295, 575),
                            (495, 575),
                            (645, 575),
                        ),
                        size = 25,
                        elastic = 0.5
                    )

                    level_start = True
                    bnd.UpdateLeaderboardBool.update = True

                if ball_count <= ball_max:
                    spawn_ball = np.random.randint(0, 75)
                    if spawn_ball == 0:
                        if ball_count % 10 == 0:
                            ball_pos += 120
                        ball_sprite = bnd.Ball(ball_pos, Space, 20, 1)
                        Balls.append(ball_sprite)
                        all_balls.add(ball_sprite)
                        ball_count += 1

                if bnd.collide(P1, Balls):
                    MusicService.score_increase()
                    score += 1

            case bnd.GameStatus.LEVEL_4:
                Space.gravity = (0, 400)
                if not level_start:
                    GamePhases.level_four()

                    spawn_pegs(
                        pos_list = (
                            # Right side
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
                        ),
                        size = 10,
                        elastic = 0.1
                    )

                    level_start = True
                    bnd.UpdateLeaderboardBool.update = True

                if ball_count <= ball_max:
                    spawn_ball = np.random.randint(0, 75)
                    if spawn_ball == 0:
                        x_pos = np.random.uniform(100, 700)
                        ball_sprite = bnd.Ball(x_pos, Space, 26.6, 2)
                        Balls.append(ball_sprite)
                        all_balls.add(ball_sprite)
                        ball_count += 1

                if bnd.collide(P1, Balls):
                    MusicService.score_increase()
                    score += 1

            case bnd.GameStatus.COS_LEVEL:
                Space.gravity = (0, 200)
                if not level_start:
                    spawn_pegs(
                        pos_list = bnd.CosPegLayout(num=bnd.CurrentPeg.num),
                        size = bnd.CosPeg.size,
                        elastic = 0.5
                    )
                    level_start = True

                if ball_count <= ball_max:
                    spawn_ball = np.random.randint(0, 75)
                    if spawn_ball == 0:
                        if ball_count % 10 == 0:
                            ball_pos += 180
                        ball_sprite = bnd.Ball(ball_pos, Space, bnd.CosBall.size, 1)
                        Balls.append(ball_sprite)
                        all_balls.add(ball_sprite)
                        ball_count += 1

                if bnd.collide(P1, Balls):
                    MusicService.score_increase()
                    score += 1

            case bnd.GameStatus.COS_MENU:
                GamePhases.cos_menu(Screen)

        if bnd.GlobalState.GAME_STATE not in {bnd.GameStatus.MAIN_MENU, bnd.GameStatus.COS_MENU, bnd.GameStatus.LEVEL_SELECT, bnd.GameStatus.LEADERBOARD, bnd.GameStatus.TITLE_SCREEN}:
            Screen.fill((217, 217, 217))
            Screen.blit(bnd.BackGround.IMAGE.image, bnd.BackGround.IMAGE.rect)
            for i in range(len(Balls)):
                Balls[i].draw(Screen)
            bnd.draw_peg(Screen, Pegs)
            P1.move()
            P1.draw(Screen)

            #bnd.draw_text_outlined(Screen, 740, 50, "Score", "#b68f40", 20, "#000000", 2)
            #bnd.draw_text_outlined(Screen, 750, 90, str(score), "#b68f40", 30, "#000000", 2)

            bnd.draw_text(Screen, 740, 50, "Score", "#b68f40", 20)
            bnd.draw_text(Screen, 750, 90, str(score), "#b68f40", 30)

            if (ball_count == ball_max+1) & (len(Balls) == 0):
                if (bnd.game_over(Screen, score, ball_count)):
                    for i in range(len(Pegs)):
                        Space.remove(Pegs[i])
                    Pegs.clear()
                    ball_count = 0
                    ball_pos = 0
                    level_start = False
                    score = 0

            for ball in Balls:
                if (bnd.delete_ball(ball.phys.body.position.y)):
                    Balls.remove(ball)
                    # del ball
        update_game_display()

if __name__ == "__main__":
    main()
