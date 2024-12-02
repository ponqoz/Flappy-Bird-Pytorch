import pygame
import numpy as np
import time

"""
|----x
|
|
y
"""
# Variablen deklarieren
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 700

SPEED = 4
GRAVITY = 0.1
GAME_SPEED = 15

PIPE_WIDTH = 50
PIPE_HEIGHT = 100


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = [pygame.image.load('../assets/sprites/yellowbird-downflap.png').convert_alpha(),
                       pygame.image.load('../assets/sprites/yellowbird-midflap.png').convert_alpha(),
                       pygame.image.load('../assets/sprites/yellowbird-upflap.png').convert_alpha()]
        
        self.speed = SPEED # Start bei 20
        
        self.current_image = 0
        self.animation_counter = 0
        self.image = self.images[0]
        self.mask = pygame.mask.from_surface(self.image)
        
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH / 2
        self.rect.y = SCREEN_HEIGHT / 2
    
    def update(self): 
        self.animation_counter += 1
        if self.animation_counter > 6:
            self.animation_counter = 0
            self.current_image = (self.current_image + 1) % 3
            self.image = self.images[self.current_image]
        self.speed += GRAVITY
        print(f"Geschwindigkeit ohne Space: {self.speed}")
        
        # Update Height of Bird
        self.rect.y += self.speed
        print(f"Y COOR: {self.rect.y}")
    
    def bump(self):
        self.speed = -SPEED
        print(f"Geschwindigkeit Space: {self.speed}")




class Ground(pygame.sprite.Sprite):
    def __init__(self):
        pass

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x_pos):
        self.image = pygame.image.load('../assets/sprites/pipe-green.png')
        self.image = pygame.transform(self.image, (PIPE_WIDTH, PIPE_HEIGHT))
        


# Initialisieren der Module
pygame.init() # Spiel
pygame.mixer.init() # Audio

# Audio-Test
pygame.mixer.music.load('../assets/audio/hit.wav')


# Initialisieren des Screens
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")
pygame.display.flip()

# Uhr
clock = pygame.time.Clock()

# Erstellen der Objekte
bird_group = pygame.sprite.Group()
bird = Bird()
bird_group.add(bird)

# Test
PIPE = pygame.image.load('../assets/sprites/pipe-green.png')
PIPE = pygame.transform.scale(PIPE, (PIPE_WIDTH, PIPE_HEIGHT))

pipe_rect = PIPE.get_rect()

# Hintergrund laden und skalieren
BACKGROUND = pygame.image.load('../assets/sprites/background-night.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))



# Hintergrund auf den Screen zeichnen
screen.blit(BACKGROUND, (0, 0))
screen.blit(PIPE, (0, 0))
pygame.display.update()


running = True
while running:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.bump()

    screen.blit(BACKGROUND, (0, 0))
    bird_group.update()
    bird_group.draw(screen)
    screen.blit(PIPE, (pipe_rect.x, pipe_rect.y)) 
    pygame.display.update()               
 
    




