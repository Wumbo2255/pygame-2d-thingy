import pygame, os, sys, time
leftt = False
rightt = False
upt = False
downt = False
pygame.init()
background_color = (0, 0, 0)
(width, height) = (1000, 800)
x = 425
y = 325
animcount = 1
boxx = 600
boxy = 480
x_change = 0
y_change = 0
upcounter = 0
downcounter = 0
leftcounter = 0
rightcounter = 0
screen = pygame.display.set_mode((width, height))
screen.fill(background_color)
pygame.display.set_caption("Map")
pygame.display.flip()
playerImg = pygame.image.load(r"textures\robod2.png")
bgImg = pygame.image.load(r"textures\background.png")
boxImg = pygame.image.load(r"textures\box.png")
screen.blit(playerImg, (x, y))
screen.blit(bgImg, (0, 0))
pygame.display.flip()
clock = pygame.time.Clock()
while True:
    if x < 70:
        x_change = 0
        x += 1
    if x+150 > 926:
        x_change = 0
        x -= 1
    if y < 280:
        y_change = 0
        y += 1 
    if y+150 > 800:
        y_change = 0
        y -= 1
    if boxx < 70:
        x_change = 0
        boxx += 1
        x += 1
    if boxx+150 > 926:
        x_change = 0
        boxx -= 1
        x -= 1
    if boxy < 280:
        y_change = 0
        boxy += 1
        y += 1 
    if boxy+150 > 800:
        y_change = 0
        boxy -= 1
        y -= 1
    if 318 < boxy+150 < 574 and 318 < boxy < 574 and 90 < boxx < 348 and 90 < boxx+150 < 348:
        import level2
        sys.exit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            pygame.key.get_pressed()
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                y_change -= 2
                upt = True
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                x_change -= 2
                leftt = True
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                x_change += 2
                rightt = True
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                y_change += 2
                downt = True
            elif event.key == pygame.K_r:
                x = 400
                y = 300
                boxx = 600
                boxy = 500
                del playerImg
                playerImg = pygame.image.load(r"textures\robod2.png")
                
        if event.type == pygame.KEYUP:
            pygame.key.get_pressed()
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                y_change = 0
                downt = False
                animcount = 0
                del playerImg
                playerImg = pygame.image.load(r"textures\robod2.png")
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                y_change = 0
                upt = False
                animcount = 0
                del playerImg
                playerImg = pygame.image.load(r"textures\roboup2.png")
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                x_change = 0
                leftt = False
                animcount = 0
                del playerImg
                playerImg = pygame.image.load(r"textures\robol2.png")
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                x_change = 0
                rightt = False
                animcount = 0
                del playerImg
                playerImg = pygame.image.load(r"textures\robor2.png")
    x += x_change
    y += y_change
    if x+150 == boxx and boxy-150 < y < boxy+150:
        boxx += x_change
    if y+150 == boxy and boxx-150 < x < boxx+150:
        boxy += y_change
    if x-150 == boxx and boxy-150 < y < boxy+150:
        boxx += x_change
    if y-150 == boxy and boxx-150 < x < boxx+150:
        boxy += y_change
    if upt == True:
        if animcount == 1:
            del playerImg
            playerImg = pygame.image.load(r"textures\roboup1.png")
        if animcount == 15:
            del playerImg
            playerImg = pygame.image.load(r"textures\roboup2.png")
        if animcount == 30:
            del playerImg
            playerImg = pygame.image.load(r"textures\roboup3.png")
        if animcount == 45:
            del playerImg
            playerImg = pygame.image.load(r"textures\roboup4.png")
        if animcount == 60:
            animcount = 0
        animcount += 1
    if downt == True:
        if animcount == 1:
            del playerImg
            playerImg = pygame.image.load(r"textures\robod1.png")
        if animcount == 15:
            del playerImg
            playerImg = pygame.image.load(r"textures\robod2.png")
        if animcount == 30:
            del playerImg
            playerImg = pygame.image.load(r"textures\robod3.png")
        if animcount == 60:
            del playerImg
            playerImg = pygame.image.load(r"textures\robod4.png")
        if animcount == 60:
            animcount = 0
        animcount += 1
    if rightt == True:
        if animcount == 1:
            del playerImg
            playerImg = pygame.image.load(r"textures\robor1.png")
        if animcount == 15:
            del playerImg
            playerImg = pygame.image.load(r"textures\robor2.png")
        if animcount == 30:
            del playerImg
            playerImg = pygame.image.load(r"textures\robor3.png")
        if animcount == 45:
            del playerImg
            playerImg = pygame.image.load(r"textures\robor4.png")
        if animcount == 60:
            animcount = 0
        animcount += 1
    if leftt == True:
        if animcount == 1:
            del playerImg
            playerImg = pygame.image.load(r"textures\robol1.png")
        if animcount == 15:
            del playerImg
            playerImg = pygame.image.load(r"textures\robol2.png")
        if animcount == 30:
            del playerImg
            playerImg = pygame.image.load(r"textures\robol3.png")
        if animcount == 45:
            del playerImg
            playerImg = pygame.image.load(r"textures\robol4.png")
        if animcount == 60:
            animcount = 0
        animcount += 1
    screen.fill(background_color)
    screen.blit(bgImg, (0, 0))
    screen.blit(playerImg, (x, y))
    screen.blit(boxImg, (boxx, boxy))
    pygame.display.flip()
    clock.tick(60)
