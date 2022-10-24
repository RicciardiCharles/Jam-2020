from pygame_functions import *
from tictactoe import *
from jumpman import *
from blackjack import *

def board_pdg(vpn_on, avast_on):
    holo = makeSprite("ressources/hollow_icons.png")
    holo2 = makeSprite("ressources/hollow_icons_moins_opac.png")
    folder = makeSprite("ressources/fold.jpg")
    banque = makeSprite("ressources/menu_banque1.png")
    banque2 = makeSprite("ressources/menu_banque2.png")
    banque3 = makeSprite("ressources/menu_banque3.png")
    banque4 = makeSprite("ressources/menu_banque4.png")
    loose1 = makeSprite("ressources/policier.png")
    loose2 = makeSprite("ressources/prison.png")
    win2 = makeSprite("ressources/screen_win.png")
    bloc_note = makeSprite("bloc_note_pdg.JPG")
    count = 0
    count_bq = 0
    jump = 0
    bj = 0
    fold = 0
    menu = 0
    jeu = 0
    oui = 0
    non = 0
    peut = 0
    aze = 0
    ty = 0
    damso = 0
    while True:
        # print(jeu)
        # print (ty)
        mouse = pygame.mouse.get_pos()
        setBackgroundImage(["ressources/bureau_pdg.png"])
        for ev in pygame.event.get():
            if ev.type == pygame.MOUSEBUTTONDOWN:
                print("x")
                print(mouse[0])
                print("y")
                print(mouse[1])
                if fold != 2 and damso != 2:
                    if mouse[0] > 188 and mouse[0] < 270 and mouse[1] > 204 and mouse[1] < 285 and damso == 0:
                        moveSprite(holo2, 166, 180)
                        showSprite(holo2)
                        damso = 1
                    elif mouse[0] > 188 and mouse[0] < 270 and mouse[1] > 204 and mouse[1] < 285 and damso == 1:
                        hideSprite(holo)
                        hideSprite(holo2)
                        moveSprite(bloc_note, 200, 100)
                        showSprite(bloc_note)
                        damso = 2
                    elif mouse[0] > 257 and mouse[0] < 328 and mouse[1] > 741 and mouse[1] < 826 and count == 0:
                        moveSprite(holo2, 230, 721)
                        showSprite(holo2)
                        count = 1
                    elif mouse[0] > 257 and mouse[0] < 328 and mouse[1] > 741 and mouse[1] < 826 and count == 1:
                        if tictactoe() == 1 and oui == 0:
                            jeu+=1
                            oui = 1
                    elif mouse[0] > 540 and mouse[0] < 601 and mouse[1] > 283 and mouse[1] < 372 and fold == 0:
                        moveSprite(holo2, 507, 260)
                        showSprite(holo2)
                        fold = 1
                    elif mouse[0] > 540 and mouse[0] < 601 and mouse[1] > 283 and mouse[1] < 372 and fold == 1:
                        hideSprite(holo2)
                        hideSprite(holo)
                        fold = 2
                        moveSprite(folder, 200, 200)
                        showSprite(folder)
                    elif mouse[0] > 755 and mouse[0] < 835 and mouse[1] > 509 and mouse[1] < 603:
                        moveSprite(holo2, 735, 490)
                        showSprite(holo2)
                    elif mouse[0] > 968 and mouse[0] < 1053 and mouse[1] > 212 and mouse[1] < 303 and bj == 0:
                        moveSprite(holo2, 948, 190)
                        showSprite(holo2)
                        bj = 1
                    elif mouse[0] > 968 and mouse[0] < 1053 and mouse[1] > 212 and mouse[1] < 303 and bj == 1:
                        hideSprite(holo2)
                        hideSprite(holo)
                        if blackjack() == 1 and non == 0:
                            jeu+=1
                            non = 1
                    elif mouse[0] > 1488 and mouse[0] < 1664 and mouse[1] > 181 and mouse[1] < 285 and menu == 0:
                        moveSprite(holo2, 1505, 163)
                        showSprite(holo2)
                        menu = 1
                    elif mouse[0] > 1488 and mouse[0] < 1664 and mouse[1] > 181 and mouse[1] < 285 and menu == 1:
                        moveSprite(holo2, 1505, 163)
                        showSprite(holo2)
                        ty = 0
                        menu = 2
                    elif mouse[0] > 1592 and mouse[0] < 1679 and mouse[1] > 624 and mouse[1] < 700 and jump == 0:
                        moveSprite(holo2, 1572, 600)
                        showSprite(holo2)
                        jump = 1
                    elif mouse[0] > 1592 and mouse[0] < 1679 and mouse[1] > 624 and mouse[1] < 700 and jump == 1:
                        print(jumpman_game())
                        if jumpman_game() == 1 and peut == 0:
                            jeu+=1
                            peut = 1
                    else:
                        hideSprite(holo2)
                        count = 0
                else:
                    if mouse[0] > 910 and mouse[1] > 203 and mouse[0] < 1043 and mouse[1] < 227 and fold == 2:
                        fold = 0
                        hideSprite(folder)
                    if mouse[0] > 1010 and mouse[1] > 98 and mouse[0] < 1140 and mouse[1] < 128 and damso == 2:
                        hideSprite(bloc_note)
                        damso = 0
            if fold != 2 and damso != 2:
                if mouse[0] > 188 and mouse[0] < 270 and mouse[1] > 204 and mouse[1] < 285:
                    moveSprite(holo, 166, 180)
                    showSprite(holo)
                elif mouse[0] > 257 and mouse[0] < 328 and mouse[1] > 741 and mouse[1] < 826:
                    moveSprite(holo, 230, 721)
                    showSprite(holo)
                elif mouse[0] > 540 and mouse[0] < 601 and mouse[1] > 283 and mouse[1] < 372:
                    moveSprite(holo, 507, 260)
                    showSprite(holo)
                elif mouse[0] > 755 and mouse[0] < 835 and mouse[1] > 509 and mouse[1] < 603:
                    moveSprite(holo, 735, 490)
                    showSprite(holo)
                elif mouse[0] > 968 and mouse[0] < 1053 and mouse[1] > 212 and mouse[1] < 303:
                    moveSprite(holo, 948, 190)
                    showSprite(holo)
                elif mouse[0] > 1488 and mouse[0] < 1664 and mouse[1] > 181 and mouse[1] < 285:
                    moveSprite(holo, 1505, 163)
                    showSprite(holo)
                elif mouse[0] > 1592 and mouse[0] < 1679 and mouse[1] > 624 and mouse[1] < 700:
                    moveSprite(holo, 1572, 600)
                    showSprite(holo)
                else:
                    hideSprite(holo)
                if ev.type == pygame.QUIT:
                    pygame.quit()
            if (menu == 2):
                if jeu == 0:
                    showSprite(banque)
                    if mouse[0] > 397 and mouse[0] < 1671 and mouse[1] > 980 and mouse[1] < 1051:
                        showSprite(loose1)
                        menu = 3
                    if mouse[0] > 397 and mouse[0] < 1671 and mouse[1] > 980 and mouse[1] < 1051 and vpn_on == 0:
                        showSprite(loose1)
                        menu = 3
                    if mouse[0] > 397 and mouse[0] < 1671 and mouse[1] > 980 and mouse[1] < 1051 and avast_on == 0:
                        showSprite(loose1)
                        menu = 3
                elif jeu == 1:
                    showSprite(banque2)
                    if mouse[0] > 397 and mouse[0] < 1671 and mouse[1] > 980 and mouse[1] < 1051:
                        showSprite(loose1)
                        menu = 3
                    if mouse[0] > 397 and mouse[0] < 1671 and mouse[1] > 980 and mouse[1] < 1051 and vpn_on == 0:
                        showSprite(loose1)
                        menu = 3
                    if mouse[0] > 397 and mouse[0] < 1671 and mouse[1] > 980 and mouse[1] < 1051 and avast_on == 0:
                        showSprite(loose1)
                        menu = 3
                elif jeu == 2:
                    showSprite(banque3)
                    if mouse[0] > 397 and mouse[0] < 1671 and mouse[1] > 980 and mouse[1] < 1051:
                        showSprite(loose1)
                        menu = 3
                    if mouse[0] > 397 and mouse[0] < 1671 and mouse[1] > 980 and mouse[1] < 1051 and vpn_on == 0:
                        showSprite(loose1)
                        menu = 3
                    if mouse[0] > 397 and mouse[0] < 1671 and mouse[1] > 980 and mouse[1] < 1051 and avast_on == 0:
                        showSprite(loose1)
                        menu = 3
                elif jeu == 3:
                    showSprite(banque4)
                    if mouse[0] > 397 and mouse[0] < 1671 and mouse[1] > 980 and mouse[1] < 1051 and vpn_on == 0:
                        showSprite(loose1)
                        hideSprite(holo)
                        hideSprite(holo2)
                        menu = 3
                    if mouse[0] > 397 and mouse[0] < 1671 and mouse[1] > 980 and mouse[1] < 1051 and avast_on == 0:
                        showSprite(loose1)
                        hideSprite(holo)
                        hideSprite(holo2)
                        menu = 3
                    if mouse[0] > 397 and mouse[0] < 1671 and mouse[1] > 980 and mouse[1] < 1051 and vpn_on == 1 and avast_on == 1:
                        showSprite(win2)
                if (keyPressed(keyCheck='q') == True) and ty == 0:
                    ty = 1
                    menu = 0
                    hideSprite(banque)
                    hideSprite(banque2)
                    hideSprite(banque3)
            if menu == 3:
                if (keyPressed(keyCheck='p') == True):
                    showSprite(loose2)