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

# Sprite Setup
P1 = Player()

all_balls = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)


def update_game_display():
    pygame.display.update()
    Clock.tick(120)
    Space.step(1/50)  # Updating time for physics sim

def game_over():
    MENU_MOUSE_POS = pygame.mouse.get_pos()
    MENU_TEXT = bnd.get_font(50).render("GAME OVER", True, "#b68f40")
    MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))

    PLAY_BUTTON = bnd.Button(image=pygame.image.load("assets/Play Rect.png"), pos=(400, 400), 
                        text_input="PLAY AGAIN", font=bnd.get_font(35), base_color="#d7fcd4", hovering_color="White")
    QUIT_BUTTON = bnd.Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(400, 550), 
                        text_input="MAIN MENU", font=bnd.get_font(35), base_color="#d7fcd4", hovering_color="White")
    Screen.blit(MENU_TEXT, MENU_RECT)

    for button in [PLAY_BUTTON, QUIT_BUTTON]:
        button.changeColor(MENU_MOUSE_POS)
        button.update(Screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                return True
            if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                GamePhases.GlobalState.GAME_STATE = GamePhases.GameStatus.MAIN_MENU
                return True
    return False

def main():
    Balls = []
    Pegs = []
    ball_max = 29
    ball_count = 0
    ball_pos = 0
    level_start = False
    collision_count = 0
    bnd.create_borders(Space)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        match bnd.GlobalState.GAME_STATE:
            case bnd.GameStatus.MAIN_MENU:
                GamePhases.main_menu_phase(Screen)
            case bnd.GameStatus.LEVEL_SELECT:
                GamePhases.level_select_phase(Screen)
            case bnd.GameStatus.LEVEL_1:
                Space.gravity = (0, 100)
                if not level_start:
                    GamePhases.level_one()
                    for i in range(10):
                        x_pos = np.random.uniform(20, 780)
                        y_pos = np.random.uniform(40, 700)
                        Pegs.append(bnd.create_peg(
                            Space, (x_pos, y_pos), 25, 0.5))
                    level_start = True

                if ball_count <= ball_max:
                    spawn_ball = np.random.randint(0, 250)
                    if spawn_ball == 0:
                        x_pos = np.random.uniform(20, 780)
                        ball_sprite = bnd.Ball(x_pos, Space, 40, 2)
                        Balls.append(ball_sprite)
                        all_balls.add(ball_sprite)
                        ball_count += 1

                if bnd.collide(P1, Balls):
                    collision_count += 1
                    print("Collision ", collision_count)

            case bnd.GameStatus.LEVEL_2:
                GamePhases.level_two()

            case bnd.GameStatus.LEVEL_3:
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
                        ball_sprite = bnd.Ball(ball_pos, Space, 43, 1)
                        Balls.append(ball_sprite)
                        all_balls.add(ball_sprite)
                        ball_count += 1

                if bnd.collide(P1, Balls):
                    collision_count += 1
                    print("Collision ", collision_count)

            case bnd.GameStatus.LEVEL_4:
                #using cosmetics selections
                Space.gravity = (0, 300)
                if not level_start:
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
                        ball_sprite = bnd.Ball(ball_pos, Space, 43, 1)
                        Balls.append(ball_sprite)
                        all_balls.add(ball_sprite)
                        ball_count += 1

                if bnd.collide(P1, Balls):
                    collision_count += 1
                    print("Collision ", collision_count)

            case bnd.GameStatus.COS_MENU:
                GamePhases.cos_menu(Screen)

        if bnd.GlobalState.GAME_STATE not in {bnd.GameStatus.MAIN_MENU, bnd.GameStatus.COS_MENU, bnd.GameStatus.LEVEL_SELECT}:
            Screen.fill((217, 217, 217))
            Screen.blit(bnd.BackGround.IMAGE.image, bnd.BackGround.IMAGE.rect)
            for i in range(len(Balls)):
                Balls[i].draw(Screen)
            bnd.draw_peg(Screen, Pegs)
            P1.move()
            P1.draw(Screen)
            if(ball_count == ball_max+1) & (len(Balls) == 0):
                if(game_over()):
                    Pegs.clear()
                    ball_count = 0
                    ball_pos = 0
                    level_start = False
                    collision_count = 0 

            for ball in Balls:
                if (bnd.delete_ball(ball.phys.body.position.y)):
                    Balls.remove(ball)
                    # del ball
        update_game_display()


if __name__ == "__main__":
    main()
