import pygame

pygame.init() # initialize = to start

screen = pygame.display.set_mode((800, 600)) # size
#                                  w    h

x = 10
y = 20

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
        pygame.Rect(x, y, 150, 100) # x, y, width, height
    )

    if x > 500:
        x -= 1
    elif x < 9:
        x += 1
    elif x > 10:
        x += 1

    # note: keep this line at the bottom below everything
    pygame.display.flip() # mean the same =v=
    # pygame.display.update()

pygame.quit()

