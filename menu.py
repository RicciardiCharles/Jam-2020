from pygame_functions import *
from board import *

def menu():
    screen = screenSize(1920, 1080)
    count = 0
    while True:
        mouse = pygame.mouse.get_pos()
        if count == 0:
            setBackgroundImage(["ressources/menu_jam.png"])
        if count == 1:
            setBackgroundImage(["ressources/bureau_hacker.png"])
            board()
        if count == 2:
            setBackgroundImage(["ressources/menu_settings.png"])
        for ev in pygame.event.get():
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if mouse[0] > 817 and mouse[1] > 412 and mouse[0] < 1104 and mouse[1] < 445:
                    count = 1
                if mouse[0] > 817 and mouse[1] > 507 and mouse[0] < 1104 and mouse[1] < 540:
                    pygame.quit()
                if mouse[0] > 817 and mouse[1] > 593 and mouse[0] < 1104 and mouse[1] < 626:
                    count = 2
                if count == 2 and mouse[0] > 9 and mouse[0] < 131 and mouse[1] > 14 and mouse[1] < 136:
                    count = 0
            if ev.type == pygame.QUIT:
                pygame.quit()