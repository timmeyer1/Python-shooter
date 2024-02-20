import pygame

class SoundManager:

    def __init__(self):
        self.sounds = {
            'shoot': pygame.mixer.Sound("assets/sounds/shoot.mp3"),
            'game_over': pygame.mixer.Sound("assets/sounds/game_over.ogg")
        }

    def play(self, name):
        self.sounds[name].play()