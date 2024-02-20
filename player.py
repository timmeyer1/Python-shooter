import pygame
from bullet import Bullet


class Player(pygame.sprite.Sprite):

    def __init__(self, game): # le (self) permet de rappeler que l'init se fait dans la class Player (son objet courant)
        super().__init__() # avec ces 2 lignes, on a initialisé la classe
        self.game = game
        self.image = pygame.image.load('assets/player/player2.png')
        self.rect = self.image.get_rect()
        self.rect.x = 30
        self.rect.y = 425
        self.health = 100
        self.max_health = 100
        self.attack = 20
        self.velocity = 5
        self.all_bullets = pygame.sprite.Group()
        self.lives = 3

    def move_right(self):
        if not self.game.check_collision(self, self.game.all_enemies):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def update_health_bar(self, surface):
        bar_color = (32, 139, 58) # vert
        bg_bar_color = (23, 23, 23) #gris noir

        bg_bar_position = [self.rect.x+80, self.rect.y-20, self.max_health, 5]
        bar_position = [self.rect.x+80, self.rect.y-20, self.health, 5]

        pygame.draw.rect(surface, bg_bar_color, bg_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)


    def damage(self, attack):
        self.health -= attack
        print(self.health)
        if self.health <= 0:
            self.health = self.max_health
            self.rect.x = 30
            self.lives -= 1
            if self.lives < 0:
                print ('FIN DE LA PARTIE')
                

    def launch_bullets(self):
        self.all_bullets.add(Bullet(self))