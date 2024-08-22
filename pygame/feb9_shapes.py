import pygame

pygame.init() # initialize = to start

screen = pygame.display.set_mode((800, 600)) # size
#                                  w    h
running = True
# main game loop
while running:
    # event: an action triggered by a user input
    for event in pygame.event.get(): # responsible to get events coming from user
        if event.type == pygame.QUIT:
            running = False

    screen.fill((176, 62, 189)) # what color you want to fill in your screen

    # Circle

    pygame.draw.circle(
        screen, 
        (255, 0, 166), # color
        (100, 300), # centrer cords
        50, # radius
        10 #size of border (optional, if no specified, everything will be fill)
    )

    # Rectangle

    pygame.draw.rect(
        screen, 
        (255, 0, 166), # color
        pygame.Rect(10, 20, 150, 100) # x, y, width, height
    )

    # Polygon

    pygame.draw.polygon(
        screen, 
        (255, 0, 166), # color
        (
            (500, 700), 
            (700, 700), 
            (700, 500)
        ) #cords of all the points (can be more than 2)
    )
    
    # Line

    pygame.draw.line(
        screen, 
        (255, 0, 166), # color
        (500, 700), 
        (700, 500) #cords of 2 of the points (line hve 2 cords)
    )


    # note: keep this line at the bottom below everything
    pygame.display.flip() # mean the same =v=
    # pygame.display.update()

pygame.quit()

