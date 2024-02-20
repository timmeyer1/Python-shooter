import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, player,):
        super().__init__()
        self.player = player
        self.image = pygame.image.load("assets/bullet.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 220
        self.rect.y = player.rect.y + 100
        self.velocity = 10
        self.angle = 0
        self.origine = self.image


    def remove(self):
        self.player.all_bullets.remove(self)

    def move(self, game):
        self.game = game
        self.rect.x += self.velocity
        self.angle += 10
        self.image = pygame.transform.rotozoom(self.origine, self.angle, 1)
        self.rect = self.image.get_rect(center = self.rect.center)

        # quand un ennemi est touche:
        for enemy in self.player.game.check_collision(self, self.player.game.all_enemies):
            self.remove() # on enleve la balle
            enemy.damage(self.player.attack) # on fait des degats

        if self.rect.x > 1080:
            self.remove