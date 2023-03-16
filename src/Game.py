import pygame
import pymunk
import sys
import components.Backend as bnd
import components.game_phases as GamePhases

pygame.init()
Screen = pygame.display.set_mode((800, 800))
Clock = pygame.time.Clock()
Space = pymunk.Space()
Space.gravity = (0, 500)  # X gravity, Y gravity


def update_game_display():
    pygame.display.update()
    Clock.tick(120)
    Space.step(1/50)  # Updating time for physics sim


def main():
    balls = []
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        match bnd.GlobalState.GAME_STATE:
            case bnd.GameStatus.MAIN_MENU:
                GamePhases.main_menu_phase()
            case bnd.GameStatus.LEVEL_1:
                GamePhases.level_one()

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        balls.append(bnd.create_ball(Space, event.pos))
            case bnd.GameStatus.LEVEL_2:
                GamePhases.level_two()

            case bnd.GameStatus.LEVEL_3:
                GamePhases.level_three()

            case bnd.GameStatus.LEVEL_4:
                GamePhases.cos_menu()
            
        Screen.fill((217, 217, 217))
        Screen.blit(bnd.BackGround.IMAGE.image, bnd.BackGround.IMAGE.rect)
        bnd.draw_ball(Screen, balls)
        update_game_display()


if __name__ == "__main__":
    main()
