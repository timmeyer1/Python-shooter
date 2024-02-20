import os
import pygame


class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f'{sprite_name}/{sprite_name}01.png')
        self.current_image = 0
        self.images = animations.get(sprite_name)
    
def load_animation_images(sprite_name):
    images = []
    path = f"{sprite_name}"

    folder = os.listdir(path)
    print(folder)

    for file in folder:
        image_path = path +"/"+ str(file)
        print(image_path)
        images.append(pygame.image.load(image_path))
        print(len(images))
    return images

animations = {
    "enemy":load_animation_images("enemy"),
    "player": load_animation_images("player"),
    
    }