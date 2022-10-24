from pygame_functions import *
from board_pdg import *

def board():
    count = 1
    nrvpn = 0
    avast = 0
    vpn_on = 0
    avast_on = 0
    damso = 0
    holo = makeSprite("ressources/hollow_icons.png")
    holo2 = makeSprite("ressources/hollow_icons_moins_opac.png")
    vpn = makeSprite("ressources/vpn.jpg")
    addSpriteImage(vpn, "ressources/vpn_activated.png")
    avast_menu = makeSprite("ressources/avst.jpg")
    addSpriteImage(avast_menu, "ressources/avst_done.jpg")
    bloc_note = makeSprite("bloc_note_hacker.JPG")
    while True:
        mouse = pygame.mouse.get_pos()
        for ev in pygame.event.get():
            if ev.type == pygame.MOUSEBUTTONDOWN:
                print("x")
                print(mouse[0])
                print("y")
                print(mouse[1])
                if nrvpn != 2 and avast != 2 and damso != 2:
                    if mouse[0] > 136 and mouse[0] < 219 and mouse[1] > 342 and mouse[1] < 442:
                        moveSprite(holo2, 110, 320)
                        showSprite(holo2)
                    elif mouse[0] > 358 and mouse[0] < 434 and mouse[1] > 171 and mouse[1] < 260 and nrvpn == 0:
                        moveSprite(holo2, 332, 149)
                        showSprite(holo2)
                        nrvpn = 1
                    elif mouse[0] > 358 and mouse[0] < 434 and mouse[1] > 171 and mouse[1] < 260 and nrvpn == 1:
                        nrvpn = 2
                        hideSprite(holo2)
                        hideSprite(holo)
                        moveSprite(vpn, 500, 150)
                        showSprite(vpn)
                    elif mouse[0] > 837 and mouse[0] < 890 and mouse[1] > 453 and mouse[1] < 540 and avast == 0:
                        moveSprite(holo2, 800, 418)
                        showSprite(holo2)
                        avast = 1
                    elif mouse[0] > 837 and mouse[0] < 890 and mouse[1] > 453 and mouse[1] < 540 and avast == 1:
                        hideSprite(holo)
                        hideSprite(holo2)
                        avast = 2
                        moveSprite(avast_menu, 300, 50)
                        showSprite(avast_menu)
                    elif mouse[0] > 923 and mouse[0] < 1064 and mouse[1] > 193 and mouse[1] < 270 and count == 0:
                        moveSprite(holo2, 925, 165)
                        showSprite(holo2)
                        count = 1
                    elif mouse[0] > 923 and mouse[0] < 1064 and mouse[1] > 193 and mouse[1] < 270 and count == 1:
                        moveSprite(holo2, 925, 165)
                        showSprite(holo2)
                        count = 2
                    elif mouse[0] > 923 and mouse[0] < 1064 and mouse[1] > 193 and mouse[1] < 270 and count == 2:
                        hideSprite(holo)
                        hideSprite(holo2)
                        board_pdg(vpn_on, avast_on)
                    elif mouse[0] > 1469 and mouse[0] < 1551 and mouse[1] > 146 and mouse[1] < 232 and damso == 0:
                        moveSprite(holo2, 1445, 132)
                        showSprite(holo2)
                        damso = 1
                    elif mouse[0] > 1469 and mouse[0] < 1551 and mouse[1] > 146 and mouse[1] < 232 and damso == 1:
                        damso = 2
                        hideSprite(holo)
                        hideSprite(holo2)
                        moveSprite(bloc_note, 200, 100)
                        showSprite(bloc_note)
                    else:
                        hideSprite(holo2)
                        count = 0
                else:
                    if mouse[0] > 952 and mouse[1] > 211 and mouse[0] < 1015 and mouse[1] < 271 and nrvpn == 2:
                        changeSpriteImage(vpn, 1)
                        pause(2500)
                        hideSprite(vpn)
                        vpn_on = 1
                        nrvpn = 3
                    if mouse[0] > 1342 and mouse[1] > 152 and mouse[0] < 1524 and mouse[1] < 189 and nrvpn == 2:
                        hideSprite(vpn)
                        nrvpn = 0
                    if mouse[0] > 511 and mouse[1] > 325 and mouse[0] < 738 and mouse[1] < 386 and avast == 2:
                        changeSpriteImage(avast_menu, 1)
                        avast_on = 1
                    if mouse[0] > 1456 and mouse[1] > 56 and mouse[0] < 1561 and mouse[1] < 102 and avast == 2 and avast_on == 0:
                        hideSprite(avast_menu)
                        avast = 0
                    if mouse[0] > 1456 and mouse[1] > 56 and mouse[0] < 1561 and mouse[1] < 102 and avast == 2 and avast_on == 1:
                        hideSprite(avast_menu)
                        avast = 3
                    if mouse[0] > 1010 and mouse[1] > 103 and mouse[0] < 1140 and mouse[1] < 125 and damso == 2:
                        hideSprite(bloc_note)
                        damso = 0
            if nrvpn != 2 and avast != 2 and damso != 2:
                if mouse[0] > 136 and mouse[0] < 219 and mouse[1] > 342 and mouse[1] < 442:
                    moveSprite(holo, 110, 320)
                    showSprite(holo)
                elif mouse[0] > 358 and mouse[0] < 434 and mouse[1] > 171 and mouse[1] < 260:
                    moveSprite(holo, 332, 149)
                    showSprite(holo)
                elif mouse[0] > 837 and mouse[0] < 890 and mouse[1] > 453 and mouse[1] < 540:
                    moveSprite(holo, 800, 418)
                    showSprite(holo)
                elif mouse[0] > 923 and mouse[0] < 1064 and mouse[1] > 193 and mouse[1] < 270:
                    moveSprite(holo, 925, 165)
                    showSprite(holo)
                elif mouse[0] > 1469 and mouse[0] < 1551 and mouse[1] > 146 and mouse[1] < 232:
                    moveSprite(holo, 1445, 132)
                    showSprite(holo)
                else:
                    hideSprite(holo)
            if ev.type == pygame.QUIT:
                pygame.quit()
