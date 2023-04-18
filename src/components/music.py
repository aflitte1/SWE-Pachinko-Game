import pygame
from paths import MUSIC_DIR

class MusicService:
    pygame.mixer.init()
    def start_menu_music():
        if pygame.mixer.music.get_busy():
            return
        music = MUSIC_DIR / "menu.ogg"
        print(music)
        pygame.mixer.music.load(music)
        pygame.mixer.music.play()
    
    def start_level_1_music():
        if pygame.mixer.music.get_busy():
            return
        music = MUSIC_DIR / "level1.ogg"
        pygame.mixer.music.load(music)
        pygame.mixer.music.play()

    def start_level_2_music():
        if pygame.mixer.music.get_busy():
            return
        music = MUSIC_DIR / "level3.ogg"
        pygame.mixer.music.load(music)
        pygame.mixer.music.play()

    def start_level_3_music():
        if pygame.mixer.music.get_busy():
            return
        music = MUSIC_DIR / "level3.ogg"
        pygame.mixer.music.load(music)
        pygame.mixer.music.play()

    def start_level_4_music():
        if pygame.mixer.music.get_busy():
            return
        music = MUSIC_DIR / "level3.ogg"
        pygame.mixer.music.load(music)
        pygame.mixer.music.play()

    def play_finish_sound():
        if pygame.mixer.music.get_busy():
            return
        filename = MUSIC_DIR / "level_finish.ogg"
        sound = pygame.mixer.Sound(filename)
        pygame.mixer.Sound.play(sound)

    def stop_music():
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        return