import pygame
from settings import SOUND_BOUNCE, SOUND_BRICK_BREAK, SOUND_POWERUP, SOUND_LIFE_LOST, SOUND_GAME_OVER, SOUND_VOLUME

class SoundManager:
    def __init__(self):
        pygame.mixer.init()

        self.sounds = {
            "bounce": pygame.mixer.Sound(SOUND_BOUNCE),
            "brick_break": pygame.mixer.Sound(SOUND_BRICK_BREAK),
            "powerup": pygame.mixer.Sound(SOUND_POWERUP),
            "life_lost": pygame.mixer.Sound(SOUND_LIFE_LOST),
            "game_over": pygame.mixer.Sound(SOUND_GAME_OVER),
        }

        for sound in self.sounds.values():
            sound.set_volume(SOUND_VOLUME)

    def play(self, name):
        if name in self.sounds:
            self.sounds[name].play()
