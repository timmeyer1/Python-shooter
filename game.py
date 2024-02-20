import pygame
from enemy import Enemy
from player import Player
from sound import SoundManager


class Game:

    def __init__(self):
        self.player = Player(self)
        self.enemy = Enemy(self)
        self.sound = SoundManager()
        self.score = 0
        self.all_players = pygame.sprite.Group()
        self.all_players.add(self.player)
        self.all_enemies = pygame.sprite.Group()
        self.spawn_enemy(2)
        self.pressed_keys = {}
    
    def spawn_enemy(self, number):
        for _ in range(number):
            enemy = Enemy(self)
            self.all_enemies.add(enemy)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)