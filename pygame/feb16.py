
import pygame

from pygame.locals import(
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_q,
    K_e
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

pygame.init()

screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))

running = True

radius = 50

speed = 2

x = 500

y = 400

center_point = (x, y)

idkwhattoname = x + radius

idkwhattonameP2 = y + radius

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((176, 62, 189))

    pygame.draw.circle(
        screen,
        (255, 0, 166),
        center_point,
        radius
    )

    user_input = pygame.key.get_pressed()

    if user_input[K_UP]:
        if idkwhattonameP2 > 0:
            idkwhattonameP2 -= speed
        else:
            idkwhattonameP2 = 0

    # if user_input[K_DOWN]:
    #     if center_point + radius < SCREEN_HEIGHT:
    #         center_point += speed
    #     else:
    #         center_point = 0

    # if user_input[K_UP]:
    #     if center_point + radius > 0:
    #         center_point -= speed
    #     else:
    #         center_point = 0

    # if user_input[K_UP]:
    #     if center_point + radius > 0:
    #         center_point -= speed
    #     else:
    #         center_point = 0