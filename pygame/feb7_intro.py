import pygame

pygame.init() # initialize = to start

screen = pygame.display.set_mode((500, 500)) # size
#                                  w    h
running = True
# main game loop
while running:
    # event: an action triggered by a user input
    for event in pygame.event.get(): # responsible to get events coming from user
        if event.type == pygame.QUIT:
            running = False

    screen.fill((176, 62, 189)) # what color you want to fill in your screen

    pygame.draw.circle(
        screen, 
        (255, 0, 166), # color
        (100, 300), # centrer cords
        100 # radius
    )

    # note: keep this line at the bottom below everything
    pygame.display.flip() # mean the same =v=
    # pygame.display.update()

pygame.quit()

