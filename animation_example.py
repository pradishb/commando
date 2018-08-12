import sys, os
import pygame
from soldier import Soldier
from cannon import Cannon

BACKGROUND = pygame.image.load('flapBG.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, (800, 600))
BACKGROUND_RECT = BACKGROUND.get_rect()


class Game(object):
    """Controls entire game"""
    def __init__(self):
        self.soldier = Soldier(100, 400)
        self.screen = self.setup_pygame()
        self.screen_rect = self.screen.get_rect()
        self.soldier_group = self.create_digimon()
        self.cannon_group = self.create_cannon()
        self.bullet_group = self.create_bullet()
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.done = False
        self.current_time = 0.0


    def setup_pygame(self):
        """Initializes pygame and produces a surface to blit on"""
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        pygame.display.set_caption('Commando')
        screen = pygame.display.set_mode((800, 600))

        return screen

    def create_digimon(self):
        sprite_group = pygame.sprite.Group()
        sprite_group.add(self.soldier)
        return sprite_group

    def create_cannon(self):
        """Creates a digimon to control"""
        sprite_group = pygame.sprite.Group()
        cannon = Cannon(500, 100)
        sprite_group.add(cannon)
        return sprite_group

    def create_bullet(self):
        sprite_group = pygame.sprite.Group()
        return sprite_group


    def update(self):
        """Updates entire game"""
        while not self.done:
            self.current_time = pygame.time.get_ticks()
            self.keys = self.get_user_input()
            self.soldier_group.update(self.current_time, self.keys)
            self.cannon_group.update(self.soldier, self.bullet_group)
            self.bullet_group.update()
            self.screen.blit(BACKGROUND, BACKGROUND_RECT)
            self.soldier_group.draw(self.screen)
            self.cannon_group.draw(self.screen)
            self.bullet_group.draw(self.screen)
            pygame.display.update()
            self.clock.tick(self.fps)


    def get_user_input(self):
        """Get's user events and keys pressed"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True

        keys = pygame.key.get_pressed()

        return keys


if __name__ == '__main__':
    game = Game()
    game.update()
    pygame.quit()
    sys.exit()

















