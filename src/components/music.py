import pygame

class MusicService:
    def start_menu_music():
        if pygame.mixer.music.get_busy():
            return
    music = "assets/music/menu.mp3"
    pygame.mixer.music.load(music)
    pygame.mixer.music.play()

    def stop_music():
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
    
    def start_game_music():
        if pygame.mixer.music.get_busy():
            return
    music = "assets/music/game.mp3"
    pygame.mixer.music.load(music)
    pygame.mixer.music.play()

    def play_finish_sound():
        filename = "assets/music/level_finish.mp3"
        sound = pygame.mixer.Sound(filename)
        pygame.mixer.Sound.play(sound)