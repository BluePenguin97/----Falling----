import pygame 
import math 
import random 
import time 
import sys 
from pygame.locals import * 
# ===== 
pygame.init() 
# ===== 
white = (255,255,255) 
black = (0,0,0) 
red = (255,0,0) 
orange = () 
yellow = () 
green = (0,255,0) 
blue = (0,0,255) 
indigo = () 
magenta = ()
# =====
rect1 = pygame.Rect(random.randint(0,1000),random.randint(100,400),random.randint(100,300),15)
# =====
rect2 = pygame.Rect(random.randint(0,1000),random.randint(100,400),random.randint(100,300),15)
# =====
rect3 = pygame.Rect(random.randint(0,1000),random.randint(100,400),random.randint(100,300),15) 
# =====
rect4 = pygame.Rect(random.randint(0,1000),random.randint(100,400),random.randint(100,300),15)
# =====
rect5 = pygame.Rect(random.randint(0,1000),random.randint(100,400),random.randint(100,300),15)
# =====
playerRect = pygame.Rect(500,17,50,50)
# =====
finishRect =  pygame.Rect(0, 550, 1000, 100)
# =====
forever = True 
fps = 120 
clock = pygame.time.Clock() 
gameExit = False 
increase = False 
level = 0
loading = 0 
gameDisplayX = 1000 
gameDisplayY = 600 
Fall = 0
mx, my = 0,0
loading_screen = True
# =====
def Draw_rect1 ():
    pygame.draw.rect(gameDisplay, black, rect1)
    rect1.move_ip(random.randint(1,3),0)
# =====
def Draw_rect2 ():
    pygame.draw.rect(gameDisplay, black, rect2)
    rect2.move_ip(random.randint(1,3),0)
# =====
def Draw_rect3 ():
    pygame.draw.rect(gameDisplay, black, rect3)
    rect3.move_ip(random.randint(1,3),0)
# =====
def Draw_rect4 ():
    pygame.draw.rect(gameDisplay, black, rect4)
    rect4.move_ip(random.randint(1,3),0)
# =====
def Draw_rect5 ():
    pygame.draw.rect(gameDisplay, black, rect5)
    rect5.move_ip(random.randint(1,3),0)
# =====
def Player ():
    pygame.draw.ellipse(gameDisplay, red, playerRect)
    if not loading_screen == True and Fall == 1:
        playerRect.move_ip(0,3)
# =====
def Finish_rect ():
    pygame.draw.rect(gameDisplay, green, finishRect)
# =====
gameDisplay = pygame.display.set_mode((gameDisplayX, gameDisplayY))                                   
if loading == 0 and loading_screen == True: 
    pygame.display.set_caption('-=-= Falling | Loading =-=-') 
# ===== 
while not gameExit: 
# ===== 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            gameExit = True 
        if event.type == pygame.MOUSEBUTTONDOWN: #and loading_screen == :
            mx, my = pygame.mouse.get_pos()
            print(mx, my)
        if (event.type == pygame.KEYDOWN): 
            if (event.key == pygame.K_LEFT): 
                playerX -= 1
            if (event.key == pygame.K_RIGHT): 
                playerX += 1
            if (event.key == pygame.K_SPACE): 
                Fall = 1
            if (event.key == pygame.K_RETURN):
                print(forever)
# =====
    if loading == 0 and loading_screen == True: 
        pygame.display.set_caption('-=-= Falling | Loading =-=-')
    if loading_screen == True:
        pygame.display.set_caption('-=-= Falling | Home =-=-')
# =====
    if Fall == 1 or loading_screen == False and not level == 0:
        pygame.display.set_caption('-=-= Falling =-=-')
# =====
    gameDisplay.fill(white)
# =====
    if not level == 0:
        Player ()
# =====
    if level >= 1 and loading_screen == False:
        Draw_rect1 ()
        if rect1.left > 1000:
            rect1.right = 0
# =====
    if level >= 2 and loading_screen == False:
        Draw_rect2 ()
        if rect2.left >= 1000:
            rect2.right = 0        
# =====
    if level >= 3 and loading_screen == False:
        Draw_rect3 ()
        if rect3.left >= 1000:
            rect3.right = 0
# =====
    if level >= 4 and loading_screen == False:
        Draw_rect4 ()
        if rect4.left >= 1000:
            rect4.right = 0
# =====
    if level >= 5 and loading_screen == False:
        Draw_rect5 ()
        if rect5.left >= 1000:
            rect5.right = 0
# =====
    if loading_screen == True:
        img = pygame.image.load('Falling_Loading_screen.png')
        img1 = pygame.image.load('background1.png')
        img2 = pygame.image.load('Play_button.png')
        gameDisplay.fill(white)
        gameDisplay.blit(img1, (0,0))
        gameDisplay.blit(img, (0,-30))
        gameDisplay.blit(img2, (200,250))
#        pygame.draw.rect(gameDisplay, black, [253, 250, 500, 90])
        if loading_screen == True:
            if mx >= 254 and my >= 250 and mx <= 750 and my <= 340:
                loading_screen = False
                level = 1
    if level >= 1 and loading_screen == False:
#        pygame.draw.rect(gameDisplay, green, [0, 550, 1000, 100])
        Finish_rect ()
        img3 = pygame.image.load('home_button.png')
        gameDisplay.blit(img3, (725,325))
# =====
    if not loading_screen == True and level >= 1:
        if rect1.colliderect(playerRect):
            playerRect.top = 17
            Fall = 0
            pygame.display.set_caption('-=-= Falling | please try level  ' + str(level) + ' again, or press enter to leave the level and go to the home screen =-=-')
# =====
    if not loading_screen == True and level >= 2:
        if rect2.colliderect(playerRect):
            playerRect.top = 17
            Fall = 0
            pygame.display.set_caption('-=-= Falling | please try level  ' + str(level) + ' again, or press enter to leave the level and go to the home screen =-=-')
# =====
    if not loading_screen == True and level >= 3:
        if rect3.colliderect(playerRect):
            playerRect.top = 17
            Fall = 0
            pygame.display.set_caption('-=-= Falling | please try level  ' + str(level) + ' again, or press enter to leave the level and go to the home screen =-=-')
# =====
    if not loading_screen == True and level >= 4:
        if rect4.colliderect(playerRect):
            playerRect.top = 17
            Fall = 0
            pygame.display.set_caption('-=-= Falling | please try level  ' + str(level) + ' again, or press enter to leave the level and go to the home screen =-=-')
# =====
    if not loading_screen == True and level >= 5:
        if rect5.colliderect(playerRect):
            playerRect.top = 17
            Fall = 0
            pygame.display.set_caption('-=-= Falling | please try level  ' + str(level) + ' again, or press enter to leave the level and go to the home screen =-=-')
# =====
    if loading_screen == False and level >= 1:
        if Finish_rect. # hi # hi
            pygame.display.set_caption('-=-= Falling | congratulations you have completed level ' + str(level) + ' =-=-')
            time.sleep(3)
            Fall = 0
            playerRect.top = 17
            level += 1
        if level == 6:
            loading_screen = True
# =====
    loading = 100
# =====
    pygame.display.update()
# =====
pygame.quit()
quit()
