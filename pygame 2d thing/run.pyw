import os, sys
import pygame
pygame.init()
width = 400
height = 500
x = 20
y = 30
screen = pygame.display.set_mode((width, height))
newimg = pygame.image.load(r"textures\button.png")
loadimg = pygame.image.load(r"textures\button.png")
optimg = pygame.image.load(r"textures\button.png")
screen.blit(newimg,(x, y))
font = pygame.font.Font(r'fonts\LiberationSans-Regular.ttf', 32) 
newtext = font.render('New Game', False, (0, 0, 0)) 
screen.blit(newtext, (117, 60))
pygame.display.flip() 
 
running = True
while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
            ex, ey = event.pos
            if ex > x and ex < x+360 and ey > y and ey < y+107:
                import level1
                break
pygame.quit()