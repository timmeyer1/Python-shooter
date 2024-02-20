import pygame 


from game import Game 

 
pygame.init()

clock = pygame.time.Clock()
FPS = 90

game = Game()
#apres avoir importe la classe, on doit l initialiser


pygame.display.set_caption("Fortnite 2")
screen = pygame.display.set_mode((1080, 720))

background = pygame.image.load('assets/background.png')



running = True


while running:
    #appelle ecran qu on a creer, blit appplique l image
    screen.blit(background, (0, 0))
    #appelle fonction et attribu de la class
    screen.blit(game.player.image, game.player.rect)

    font = pygame.font.SysFont("monospace", 16)
    score_text = font.render(f"Score : {game.score}", 1, (0, 0, 0))
    screen.blit(score_text, (20, 20))

    font = pygame.font.SysFont("monospace", 16)
    lives_text = font.render(f"Vie(s) restante(s) : {game.player.lives}", 1, (0, 0, 0))
    screen.blit(lives_text, (20, 40))

    

    game.player.update_health_bar(screen)

    #function draw pour grp d image
    game.player.all_bullets.draw(screen)


    if game.pressed_keys.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed_keys.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

   
    for bullet in game.player.all_bullets:
        bullet.move(game)
 
    for monster in game.all_enemies:
        monster.move()
        monster.update_health_bar(screen)
    game.all_enemies.draw(screen)

    pygame.display.flip()

    #gestion des events tjrs a la fin 
    for event in pygame.event.get():
        #si mon type est egal a la constante quite, tu arrete la boucle et quitte le jeu
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("I CLOSE THE GAME")
            #joue avec la pression des touches, down on appui et up on appui plus
        elif event.type == pygame.KEYDOWN:
            game.pressed_keys[event.key] = True

            if event.key == pygame.K_SPACE:
                game.player.launch_bullets()
                game.sound.play('shoot')

        elif event.type == pygame.KEYUP:
            game.pressed_keys[event.key] = False

    clock.tick(FPS)