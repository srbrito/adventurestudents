import pygame, sys

class KeyEvents:
    def __init__(self, PLAYER, escolhido):
        self.PLAYER = PLAYER
        self.counter = 0
        self.movement = .2
        self.orbs = []

        if escolhido == "enzo":
            img_path = './sprites/chars/enzo/enzo_'
        else:
            img_path = './sprites/chars/valentina/valentina_'

        f_path = img_path + 'f'
        b_path = img_path + 'b'
        r_path = img_path + 'r'
        l_path = img_path + 'l'

        self.f_images = [f_path + str(f) + '.png' for f in range(3)]
        self.b_images = [b_path + str(b) + '.png' for b in range(3)]
        self.r_images = [r_path + str(r) + '.png' for r in range(3)]
        self.l_images = [l_path + str(l) + '.png' for l in range(3)]

    def global_events(self):
        self.movement = .2

    def quit(self):
        pygame.quit()
        sys.exit()

    def key_down(self):
        self.PLAYER.PLAYER_POS[1] += self.movement
        self.PLAYER.DIRECTION = 'd'

        self.PLAYER.SPRITE_POS = pygame.image.load(self.f_images[self.counter])
        self.counter = (self.counter + 1) % len(self.f_images)

    def key_up(self):
        self.PLAYER.PLAYER_POS[1] -= self.movement
        self.PLAYER.DIRECTION = 'u'

        self.PLAYER.SPRITE_POS = pygame.image.load(self.b_images[self.counter])
        self.counter = (self.counter + 1) % len(self.b_images)

    def key_left(self):
        self.PLAYER.PLAYER_POS[0] -= self.movement
        self.PLAYER.DIRECTION = 'l'
        
        self.PLAYER.SPRITE_POS = pygame.image.load(self.l_images[self.counter])
        self.counter = (self.counter + 1) % len(self.l_images)

    def key_right(self):
        self.PLAYER.PLAYER_POS[0] += self.movement
        self.PLAYER.DIRECTION = 'r'

        self.PLAYER.SPRITE_POS = pygame.image.load(self.r_images[self.counter])
        self.counter = (self.counter + 1) % len(self.r_images)