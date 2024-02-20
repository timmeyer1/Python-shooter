import random
import pygame

class Enemy(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load('assets/player/monster.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 525
        self.health = 100
        self.max_health = 100
        self.attack = 0.5
        self.velocity = random.randint(2, 5)
    
    def damage(self ,attack):
        self.health -= attack
        print(self.health)
        if self.health <= 0:
            self.health = self.max_health
            self.rect.x = 1000 + random.randint(0, 300)
            self.game.score += 20

    def update_health_bar(self, surface):
        bar_color = (32, 139, 58) # vert
        bg_bar_color = (23, 23, 23) #gris noir

        bg_bar_position = [self.rect.x, self.rect.y-20, self.max_health, 5]
        bar_position = [self.rect.x, self.rect.y-20, self.health, 5]

        pygame.draw.rect(surface, bg_bar_color, bg_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def move(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else:
             self.game.player.damage(self.attack)
             
        if self.rect.x < 0:
                self.remove()