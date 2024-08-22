from cmath import pi
from turtle import back
import pygame

from pygame.locals import(
    K_a,
    K_s,
    K_w,
    K_d
)

screenwidth = 800
screenheight = 600

pygame.init() 
screen = pygame.display.set_mode((screenwidth, screenheight)) 
pygame.display.set_caption("How Pikachu Fly")

pikachu_x = 300
pikachu_y = 400
pikachu_speed = 0.5

pikachu_left = pygame.image.load("./pikachu_pixel.png") #image name
scale_factor_pika = 3
pikachu_left = pygame.transform.scale(pikachu_left, (pikachu_left.get_width() // scale_factor_pika, pikachu_left.get_height() // scale_factor_pika))

pikachu_right = pygame.transform.flip(pikachu_left, True, False)

background = pygame.image.load("./df4e8ba28f912bf9cdf9fa0dfc196411.png")
background = pygame.transform.scale(background, (800, 600))

direction = 'right'
pikachu_sprite = pikachu_right

running = True
while running:
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False


        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         pikachu_speed =- pikachu_speed
        #     if event.key == pygame.K_RIGHT:
        #         pikachu_speed =+ pikachu_speed

    action = pygame.key.get_pressed()
    if action[pygame.K_LEFT]:
        pikachu_x -= pikachu_speed
        direction = 'left'
    if action[pygame.K_RIGHT]:
        pikachu_x += pikachu_speed
        direction = 'right'

    if direction == 'left':
        pikachu_sprite = pikachu_left
    elif direction == 'right':
        pikachu_sprite = pikachu_right

    screen.blit(background, (0,0))

    pygame.draw.ellipse(screen,
                        (26, 24,28),
                        (pikachu_x, pikachu_y + pikachu_sprite.get_height() - 20, 110, 30))

    screen.blit(pikachu_sprite, (pikachu_x,pikachu_y))

    pygame.display.flip()

pygame.quit()