
import pygame

from pygame.locals import(
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_SPACE,
    K_a,
    K_s,
    K_w,
    K_d,
    K_q
)

screenwidth = 800
screenheight = 600

pygame.init() # initialize = to start

screen = pygame.display.set_mode((screenwidth, screenheight)) # size
#                                  w    h

x = 10
y = 20
w = 250
h = 150

speed = 2

running = True
# main game loop
while running:
    # event: an action triggered by a user input
    for event in pygame.event.get(): # responsible to get events coming from user
        if event.type == pygame.QUIT:
            running = False

    screen.fill((176, 62, 189)) # what color you want to fill in your screen

    pygame.draw.rect(
        screen, 
        (255, 0, 166), # color
        pygame.Rect(x, y, w, h) # x, y, width, height
    )

    # if x > 500:
    #     x -= 1
    # elif x < 9:
    #     x += 1
    # elif x > 10:
    #     x += 1

    # Getting user input

    user_input = pygame.key.get_pressed()

    if user_input[K_w]:
        if y > 0:
            y -= speed
        else:
            y =0
    if user_input[K_s]:
        if y + h < screenheight:
            y += speed
        else:
            y = screenheight - h
    if user_input[K_a]:
        if x > 0:
            x -= speed
        else:
            x = 0
    if user_input[K_d]:
        if x + w < screenwidth:
            x += speed
        else:
            x = screenwidth - w
    
    if user_input[K_SPACE]:
        w += 1
        h += 1
        x -= 0.5
        y -= 0.5
        
    elif user_input[K_q]:
        w -= 1
        h -= 1
        x += 0.5
        y += 0.5

    # if x == 550:
    #     x = 549
    # elif x == 0:
    #     x = 1
    # elif y == 450:
    #     y = 449
    # elif y == 0:
    #     y = 1

    # note: keep this line at the bottom below everything
    pygame.display.flip() # mean the same =v=
    # pygame.display.update()

pygame.quit()

