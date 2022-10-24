from pygame_functions import *

def tictactoe():
    screen = screenSize(1920, 1080)
    setBackgroundImage(["ressources/bgttt.jpg"])
    map = makeSprite("ressources/gamezone1.png")
    addSpriteImage(map, "ressources/gamezone2.png")
    addSpriteImage(map, "ressources/gamezone3.png")
    addSpriteImage(map, "ressources/gamezone4.png")
    addSpriteImage(map, "ressources/gamezone5.png")
    addSpriteImage(map, "ressources/gamezone6.png")
    addSpriteImage(map, "ressources/gamezone7.png")
    addSpriteImage(map, "ressources/gamezone8.png")
    addSpriteImage(map, "ressources/gamezone9.png")
    addSpriteImage(map, "ressources/gamezone10.png")
    addSpriteImage(map, "ressources/gamezone11.png")
    addSpriteImage(map, "ressources/gamezone12.png")
    round1 = makeSprite("ressources/round1.png")
    addSpriteImage(round1, "ressources/round2.png")
    addSpriteImage(round1, "ressources/round3.png")
    addSpriteImage(round1, "ressources/round4.png")
    addSpriteImage(round1, "ressources/round5.png")
    addSpriteImage(round1, "ressources/round6.png")
    round2 = makeSprite("ressources/round1.png")
    addSpriteImage(round2, "ressources/round2.png")
    addSpriteImage(round2, "ressources/round3.png")
    addSpriteImage(round2, "ressources/round4.png")
    addSpriteImage(round2, "ressources/round5.png")
    addSpriteImage(round2, "ressources/round6.png")
    round3 = makeSprite("ressources/round1.png")
    addSpriteImage(round3, "ressources/round2.png")
    addSpriteImage(round3, "ressources/round3.png")
    addSpriteImage(round3, "ressources/round4.png")
    addSpriteImage(round3, "ressources/round5.png")
    addSpriteImage(round3, "ressources/round6.png")
    round4 = makeSprite("ressources/round1.png")
    addSpriteImage(round4, "ressources/round2.png")
    addSpriteImage(round4, "ressources/round3.png")
    addSpriteImage(round4, "ressources/round4.png")
    addSpriteImage(round4, "ressources/round5.png")
    addSpriteImage(round4, "ressources/round6.png")
    round5 = makeSprite("ressources/round1.png")
    addSpriteImage(round5, "ressources/round2.png")
    addSpriteImage(round5, "ressources/round3.png")
    addSpriteImage(round5, "ressources/round4.png")
    addSpriteImage(round5, "ressources/round5.png")
    addSpriteImage(round5, "ressources/round6.png")
    round6 = makeSprite("ressources/round1.png")
    addSpriteImage(round6, "ressources/round2.png")
    addSpriteImage(round6, "ressources/round3.png")
    addSpriteImage(round6, "ressources/round4.png")
    addSpriteImage(round6, "ressources/round5.png")
    addSpriteImage(round6, "ressources/round6.png")
    round7 = makeSprite("ressources/round1.png")
    addSpriteImage(round7, "ressources/round2.png")
    addSpriteImage(round7, "ressources/round3.png")
    addSpriteImage(round7, "ressources/round4.png")
    addSpriteImage(round7, "ressources/round5.png")
    addSpriteImage(round7, "ressources/round6.png")
    round8 = makeSprite("ressources/round1.png")
    addSpriteImage(round8, "ressources/round2.png")
    addSpriteImage(round8, "ressources/round3.png")
    addSpriteImage(round8, "ressources/round4.png")
    addSpriteImage(round8, "ressources/round5.png")
    addSpriteImage(round8, "ressources/round6.png")
    round9 = makeSprite("ressources/round1.png")
    addSpriteImage(round9, "ressources/round2.png")
    addSpriteImage(round9, "ressources/round3.png")
    addSpriteImage(round9, "ressources/round4.png")
    addSpriteImage(round9, "ressources/round5.png")
    addSpriteImage(round9, "ressources/round6.png")
    hover_round = makeSprite("ressources/hover_round.png")
    cross1 = makeSprite("ressources/cross1.png")
    addSpriteImage(cross1, "ressources/cross2.png")
    addSpriteImage(cross1, "ressources/cross3.png")
    addSpriteImage(cross1, "ressources/cross4.png")
    addSpriteImage(cross1, "ressources/cross5.png")
    addSpriteImage(cross1, "ressources/cross6.png")
    cross2 = makeSprite("ressources/cross1.png")
    addSpriteImage(cross2, "ressources/cross2.png")
    addSpriteImage(cross2, "ressources/cross3.png")
    addSpriteImage(cross2, "ressources/cross4.png")
    addSpriteImage(cross2, "ressources/cross5.png")
    addSpriteImage(cross2, "ressources/cross6.png")
    cross3 = makeSprite("ressources/cross1.png")
    addSpriteImage(cross3, "ressources/cross2.png")
    addSpriteImage(cross3, "ressources/cross3.png")
    addSpriteImage(cross3, "ressources/cross4.png")
    addSpriteImage(cross3, "ressources/cross5.png")
    addSpriteImage(cross3, "ressources/cross6.png")
    cross4 = makeSprite("ressources/cross1.png")
    addSpriteImage(cross4, "ressources/cross2.png")
    addSpriteImage(cross4, "ressources/cross3.png")
    addSpriteImage(cross4, "ressources/cross4.png")
    addSpriteImage(cross4, "ressources/cross5.png")
    addSpriteImage(cross4, "ressources/cross6.png")
    cross5 = makeSprite("ressources/cross1.png")
    addSpriteImage(cross5, "ressources/cross2.png")
    addSpriteImage(cross5, "ressources/cross3.png")
    addSpriteImage(cross5, "ressources/cross4.png")
    addSpriteImage(cross5, "ressources/cross5.png")
    addSpriteImage(cross5, "ressources/cross6.png")
    cross6 = makeSprite("ressources/cross1.png")
    addSpriteImage(cross6, "ressources/cross2.png")
    addSpriteImage(cross6, "ressources/cross3.png")
    addSpriteImage(cross6, "ressources/cross4.png")
    addSpriteImage(cross6, "ressources/cross5.png")
    addSpriteImage(cross6, "ressources/cross6.png")
    cross7 = makeSprite("ressources/cross1.png")
    addSpriteImage(cross7, "ressources/cross2.png")
    addSpriteImage(cross7, "ressources/cross3.png")
    addSpriteImage(cross7, "ressources/cross4.png")
    addSpriteImage(cross7, "ressources/cross5.png")
    addSpriteImage(cross7, "ressources/cross6.png")
    cross8 = makeSprite("ressources/cross1.png")
    addSpriteImage(cross8, "ressources/cross2.png")
    addSpriteImage(cross8, "ressources/cross3.png")
    addSpriteImage(cross8, "ressources/cross4.png")
    addSpriteImage(cross8, "ressources/cross5.png")
    addSpriteImage(cross8, "ressources/cross6.png")
    cross9 = makeSprite("ressources/cross1.png")
    addSpriteImage(cross9, "ressources/cross2.png")
    addSpriteImage(cross9, "ressources/cross3.png")
    addSpriteImage(cross9, "ressources/cross4.png")
    addSpriteImage(cross9, "ressources/cross5.png")
    addSpriteImage(cross9, "ressources/cross6.png")
    eraser = makeSprite("ressources/eraser.png")
    addSpriteImage(eraser, "ressources/eraserslected.png")
    pencil = makeSprite("ressources/pencilselect.png")
    addSpriteImage(pencil, "ressources/pencil.png")
    end = makeSprite("ressources/loose.png")
    addSpriteImage(end, "ressources/win.png")
    moveSprite(eraser, 100, 300)
    showSprite(eraser)
    moveSprite(pencil, 1500, 100)
    showSprite(pencil)
    moveSprite(map, 550, 100)
    showSprite(map)
    for i in range (1, 12):
        pause(100)
        changeSpriteImage(map, i)
        i = i + 1
    moveSprite(cross1, 606, 121)
    showSprite(cross1)
    for i in range (1, 6):
        pause(100)
        changeSpriteImage(cross1, i)
        i = i + 1
    moveSprite(cross9, 1220, 650)
    showSprite(cross9)
    for i in range (1, 6):
        pause(100)
        changeSpriteImage(cross9, i)
        i = i + 1
    spot1 = 2
    spot2 = 0
    spot3 = 0
    spot4 = 0
    spot5 = 0
    spot6 = 0
    spot7 = 0
    spot8 = 0
    spot9 = 2
    turn = 1
    tool = 1
    while True:
        if spot1 != 0 and spot2 != 0 and spot3 != 0 and spot4 != 0 and spot5 != 0 and spot6 != 0 and spot7 != 0 and spot8 != 0 and spot9 != 0:
            moveSprite(end, 500, 300)
            showSprite(end)
            pause(2000)
            hideSprite(end)
            hideSprite(pencil)
            hideSprite(eraser)
            hideSprite(cross1)
            hideSprite(cross2)
            hideSprite(cross3)
            hideSprite(cross4)
            hideSprite(cross5)
            hideSprite(cross6)
            hideSprite(cross7)
            hideSprite(cross8)
            hideSprite(cross9)
            hideSprite(round1)
            hideSprite(round2)
            hideSprite(round3)
            hideSprite(round4)
            hideSprite(round5)
            hideSprite(round6)
            hideSprite(round7)
            hideSprite(round8)
            hideSprite(round9)
            hideSprite(hover_round)
            hideSprite(map)
            return (0)
        if (spot1 == 2 and spot2 == 2 and spot3 == 2) or (spot4 == 2 and spot5 == 2 and spot6 == 2) or (spot7 == 2 and spot8 == 2 and spot9 == 2) or (spot1 == 2 and spot4 == 2 and spot7 == 2) or (spot2 == 2 and spot5 == 2 and spot8 == 2) or (spot3 == 2 and spot6 == 2 and spot9 == 2) or (spot1 == 2 and spot5 == 2 and spot9 == 2) or (spot3 == 2 and spot5 == 2 and spot7 == 2):
            moveSprite(end, 500, 300)
            showSprite(end)
            pause(2000)
            hideSprite(end)
            hideSprite(pencil)
            hideSprite(eraser)
            hideSprite(cross1)
            hideSprite(cross2)
            hideSprite(cross3)
            hideSprite(cross4)
            hideSprite(cross5)
            hideSprite(cross6)
            hideSprite(cross7)
            hideSprite(cross8)
            hideSprite(cross9)
            hideSprite(round1)
            hideSprite(round2)
            hideSprite(round3)
            hideSprite(round4)
            hideSprite(round5)
            hideSprite(round6)
            hideSprite(round7)
            hideSprite(round8)
            hideSprite(round9)
            hideSprite(hover_round)
            hideSprite(map)
            return (0)
        if (spot1 == 1 and spot2 == 1 and spot3 == 1) or (spot4 == 1 and spot5 == 1 and spot6 == 1) or (spot7 == 1 and spot8 == 1 and spot9 == 1) or (spot1 == 1 and spot4 == 1 and spot7 == 1) or (spot2 == 1 and spot5 == 1 and spot8 == 1) or (spot3 == 1 and spot6 == 1 and spot9 == 1) or (spot1 == 1 and spot5 == 1 and spot9 == 1) or (spot3 == 1 and spot5 == 1 and spot7 == 1):
            moveSprite(end, 500, 300)
            changeSpriteImage(end, 1)
            showSprite(end)
            pause(2000)
            hideSprite(end)
            hideSprite(pencil)
            hideSprite(eraser)
            hideSprite(cross1)
            hideSprite(cross2)
            hideSprite(cross3)
            hideSprite(cross4)
            hideSprite(cross5)
            hideSprite(cross6)
            hideSprite(cross7)
            hideSprite(cross8)
            hideSprite(cross9)
            hideSprite(round1)
            hideSprite(round2)
            hideSprite(round3)
            hideSprite(round4)
            hideSprite(round5)
            hideSprite(round6)
            hideSprite(round7)
            hideSprite(round8)
            hideSprite(round9)
            hideSprite(hover_round)
            hideSprite(map)
            return (1)
        mouse = pygame.mouse.get_pos()
        if tool == 1:
            changeSpriteImage(pencil, 0)
            changeSpriteImage(eraser, 0)
        elif tool == 2:
            changeSpriteImage(pencil, 1)
            changeSpriteImage(eraser, 1)
        if turn == 2 and spot5 == 0:
            moveSprite(cross5, 900, 378)
            showSprite(cross5)
            for i in range (1, 6):
                pause(100)
                changeSpriteImage(cross5, i)
                i = i + 1
            spot5 = 2
            turn = 1
        elif turn == 2 and spot5 == 1 and spot7 == 0:
            moveSprite(cross7, 595, 634)
            showSprite(cross7)
            for i in range (1, 6):
                pause(100)
                changeSpriteImage(cross7, i)
                i = i + 1
            spot7 = 2
            turn = 1
        elif turn == 2 and spot8 == 1 and spot4 == 0:
            moveSprite(cross4, 590, 365)
            showSprite(cross4)
            for i in range (1, 6):
                pause(100)
                changeSpriteImage(cross4, i)
                i = i + 1
            spot4 = 2
            turn = 1
        elif turn == 2 and spot4 == 1 and spot8 == 0:
            moveSprite(cross8, 905, 633)
            showSprite(cross8)
            for i in range (1, 6):
                pause(100)
                changeSpriteImage(cross8, i)
                i = i + 1
            spot8 = 2
            turn = 1
        elif turn == 2:
            if spot1 == 0:
                moveSprite(cross1, 606, 121)
                showSprite(cross1)
                for i in range (1, 6):
                    pause(100)
                    changeSpriteImage(cross1, i)
                    i = i + 1
                turn = 1
                spot1 = 2
            elif spot2 == 0:
                moveSprite(cross2, 865, 121)
                showSprite(cross2)
                for i in range (1, 6):
                    pause(100)
                    changeSpriteImage(cross2, i)
                    i = i + 1
                turn = 1
                spot2 = 2
            elif spot3 == 0:
                moveSprite(cross3, 1170, 121)
                showSprite(cross3)
                for i in range (1, 6):
                    pause(100)
                    changeSpriteImage(cross3, i)
                    i = i + 1
                turn = 1
                spot3 = 2
            elif spot4 == 0:
                moveSprite(cross4, 590, 365)
                showSprite(cross4)
                for i in range (1, 6):
                    pause(100)
                    changeSpriteImage(cross4, i)
                    i = i + 1
                turn = 1
                spot4 = 2
            elif spot5 == 0:
                moveSprite(cross5, 900, 378)
                showSprite(cross5)
                for i in range (1, 6):
                    pause(100)
                    changeSpriteImage(cross5, i)
                    i = i + 1
                turn = 1
                spot5 = 2
            elif spot6 == 0:
                moveSprite(cross6, 1180, 370)
                showSprite(cross6)
                for i in range (1, 6):
                    pause(100)
                    changeSpriteImage(cross6, i)
                    i = i + 1
                turn = 1
                spot6 = 2
            elif spot7 == 0:
                moveSprite(cross7, 595, 634)
                showSprite(cross7)
                for i in range (1, 6):
                    pause(100)
                    changeSpriteImage(cross7, i)
                    i = i + 1
                turn = 1
                spot7 = 2
            elif spot8 == 0:
                moveSprite(cross8, 905, 633)
                showSprite(cross8)
                for i in range (1, 6):
                    pause(100)
                    changeSpriteImage(cross8, i)
                    i = i + 1
                turn = 1
                spot8 = 2
            elif spot9 == 0:
                moveSprite(cross9, 1220, 650)
                showSprite(cross9)
                for i in range (1, 6):
                    pause(100)
                    changeSpriteImage(cross9, i)
                    i = i + 1
                turn = 1
                spot9 = 2
        if mouse[0] < 761 and mouse[1] < 290 and mouse[0] > 606 and mouse[1] > 151 and spot1 == 0 and turn == 1 and tool == 1:
            moveSprite(hover_round, 606, 121)
            showSprite(hover_round)
        elif mouse[0] < 1095 and mouse[1] < 297 and mouse[0] > 845 and mouse[1] > 135 and spot2 == 0 and turn == 1 and tool == 1:
            moveSprite(hover_round, 865, 121)
            showSprite(hover_round)
        elif mouse[0] < 1344 and mouse[1] < 297 and mouse[0] > 1169 and mouse[1] > 135 and spot3 == 0 and turn == 1 and tool == 1:
            moveSprite(hover_round, 1170, 121)
            showSprite(hover_round)
        elif mouse[0] < 792 and mouse[1] < 542 and mouse[0] > 586 and mouse[1] > 365 and spot4 == 0 and turn == 1 and tool == 1:
            moveSprite(hover_round, 590, 365)
            showSprite(hover_round)
        elif mouse[0] < 1109 and mouse[1] < 558 and mouse[0] > 860 and mouse[1] > 378 and spot5 == 0 and turn == 1 and tool == 1:
            moveSprite(hover_round, 900, 378)
            showSprite(hover_round)
        elif mouse[0] < 1372 and mouse[1] < 570 and mouse[0] > 1184 and mouse[1] > 372 and spot6 == 0 and turn == 1 and tool == 1:
            moveSprite(hover_round, 1180, 370)
            showSprite(hover_round)
        elif mouse[0] < 780 and mouse[1] < 807 and mouse[0] > 595 and mouse[1] > 634 and spot7 == 0 and turn == 1 and tool == 1:
            moveSprite(hover_round, 595, 634)
            showSprite(hover_round)
        elif mouse[0] < 1121 and mouse[1] < 811 and mouse[0] > 866 and mouse[1] > 633 and spot8 == 0 and turn == 1 and tool == 1:
            moveSprite(hover_round, 905, 633)
            showSprite(hover_round)
        elif mouse[0] < 1381 and mouse[1] < 811 and mouse[0] > 1204 and mouse[1] > 644 and spot9 == 0 and turn == 1 and tool == 1:
            moveSprite(hover_round, 1220, 650)
            showSprite(hover_round)
        else:
            hideSprite(hover_round)
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if mouse[0] > 1580 and mouse[1] > 124 and mouse[0] < 1746 and mouse[1] < 940:
                    tool = 1
                if mouse[0] > 134 and mouse[1] > 321 and mouse[0] < 304 and mouse[1] < 763:
                    tool = 2
                if mouse[0] < 761 and mouse[1] < 290 and mouse[0] > 606 and mouse[1] > 151 and spot1 == 0 and turn == 1 and tool == 1:
                    hideSprite(hover_round)
                    moveSprite(round1, 606, 121)
                    showSprite(round1)
                    for i in range (1, 6):
                        pause(100)
                        changeSpriteImage(round1, i)
                        i = i + 1
                    spot1 = 1
                    turn = 2
                elif mouse[0] < 1095 and mouse[1] < 297 and mouse[0] > 845 and mouse[1] > 135 and spot2 == 0 and turn == 1 and tool == 1:
                    hideSprite(hover_round)
                    moveSprite(round2, 865, 121)
                    showSprite(round2)
                    for i in range (1, 6):
                        pause(100)
                        changeSpriteImage(round2, i)
                        i = i + 1
                    spot2 = 1
                    turn = 2
                elif mouse[0] < 1344 and mouse[1] < 297 and mouse[0] > 1169 and mouse[1] > 135 and spot3 == 0 and turn == 1 and tool == 1:
                    hideSprite(hover_round)
                    moveSprite(round3, 1170, 121)
                    showSprite(round3)
                    for i in range (1, 6):
                        pause(100)
                        changeSpriteImage(round3, i)
                        i = i + 1
                    spot3 = 1
                    turn = 2
                elif mouse[0] < 792 and mouse[1] < 542 and mouse[0] > 586 and mouse[1] > 365 and spot4 == 0 and turn == 1 and tool == 1:
                    hideSprite(hover_round)
                    moveSprite(round4, 590, 365)
                    showSprite(round4)
                    for i in range (1, 6):
                        pause(100)
                        changeSpriteImage(round4, i)
                        i = i + 1
                    spot4 = 1
                    turn = 2
                elif mouse[0] < 1109 and mouse[1] < 558 and mouse[0] > 860 and mouse[1] > 378 and spot5 == 0 and turn == 1 and tool == 1:
                    hideSprite(hover_round)
                    moveSprite(round5, 900, 378)
                    showSprite(round5)
                    for i in range (1, 6):
                        pause(100)
                        changeSpriteImage(round5, i)
                        i = i + 1
                    spot5 = 1
                    turn = 2
                elif mouse[0] < 1372 and mouse[1] < 570 and mouse[0] > 1184 and mouse[1] > 372 and spot6 == 0 and turn == 1 and tool == 1:
                    hideSprite(hover_round)
                    moveSprite(round6, 1180, 370)
                    showSprite(round6)
                    for i in range (1, 6):
                        pause(100)
                        changeSpriteImage(round6, i)
                        i = i + 1
                    spot6 = 1
                    turn = 2
                elif mouse[0] < 780 and mouse[1] < 807 and mouse[0] > 595 and mouse[1] > 634 and spot7 == 0 and turn == 1 and tool == 1:
                    hideSprite(hover_round)
                    moveSprite(round7, 595, 634)
                    showSprite(round7)
                    for i in range (1, 6):
                        pause(100)
                        changeSpriteImage(round7, i)
                        i = i + 1
                    spot7 = 1
                    turn = 2
                elif mouse[0] < 1121 and mouse[1] < 811 and mouse[0] > 866 and mouse[1] > 633 and spot8 == 0 and turn == 1 and tool == 1:
                    hideSprite(hover_round)
                    moveSprite(round8, 905, 633)
                    showSprite(round8)
                    for i in range (1, 6):
                        pause(100)
                        changeSpriteImage(round8, i)
                        i = i + 1
                    spot8 = 1
                    turn = 2
                elif mouse[0] < 1381 and mouse[1] < 811 and mouse[0] > 1204 and mouse[1] > 644 and spot9 == 0 and turn == 1 and tool == 1:
                    hideSprite(hover_round)
                    moveSprite(round9, 1220, 650)
                    showSprite(round9)
                    for i in range (1, 6):
                        pause(100)
                        changeSpriteImage(round9, i)
                        i = i + 1
                    spot9 = 1
                    turn = 2
                if mouse[0] < 761 and mouse[1] < 290 and mouse[0] > 606 and mouse[1] > 151 and spot1 == 2 and turn == 1 and tool == 2:
                    i = 5
                    while i > 0:
                        pause(100)
                        changeSpriteImage(cross1, i)
                        i = i - 1
                    hideSprite(cross1)
                    spot1 = 0
                elif mouse[0] < 1095 and mouse[1] < 297 and mouse[0] > 845 and mouse[1] > 135 and spot2 == 2 and turn == 1 and tool == 2:
                    i = 5
                    while i > 0:
                        pause(100)
                        changeSpriteImage(cross2, i)
                        i = i - 1
                    hideSprite(cross2)
                    spot2 = 0
                elif mouse[0] < 1344 and mouse[1] < 297 and mouse[0] > 1169 and mouse[1] > 135 and spot3 == 2 and turn == 1 and tool == 2:
                    i = 5
                    while i > 0:
                        pause(100)
                        changeSpriteImage(cross3, i)
                        i = i - 1
                    hideSprite(cross3)
                    spot3 = 0
                elif mouse[0] < 792 and mouse[1] < 542 and mouse[0] > 586 and mouse[1] > 365 and spot4 == 2 and turn == 1 and tool == 2:
                    i = 5
                    while i > 0:
                        pause(100)
                        changeSpriteImage(cross4, i)
                        i = i - 1
                    hideSprite(cross4)
                    spot4 = 0
                elif mouse[0] < 1109 and mouse[1] < 558 and mouse[0] > 860 and mouse[1] > 378 and spot5 == 2 and turn == 1 and tool == 2:
                    i = 5
                    while i > 0:
                        pause(100)
                        changeSpriteImage(cross5, i)
                        i = i - 1
                    hideSprite(cross5)
                    spot5 = 0
                elif mouse[0] < 1372 and mouse[1] < 570 and mouse[0] > 1184 and mouse[1] > 372 and spot6 == 2 and turn == 1 and tool == 2:
                    i = 5
                    while i > 0:
                        pause(100)
                        changeSpriteImage(cross6, i)
                        i = i - 1
                    hideSprite(cross6)
                    spot6 = 0
                elif mouse[0] < 780 and mouse[1] < 807 and mouse[0] > 595 and mouse[1] > 634 and spot7 == 2 and turn == 1 and tool == 2:
                    i = 5
                    while i > 0:
                        pause(100)
                        changeSpriteImage(cross7, i)
                        i = i - 1
                    hideSprite(cross7)
                    spot7 = 0
                elif mouse[0] < 1121 and mouse[1] < 811 and mouse[0] > 866 and mouse[1] > 633 and spot8 == 2 and turn == 1 and tool == 2:
                    i = 5
                    while i > 0:
                        pause(100)
                        changeSpriteImage(cross8, i)
                        i = i - 1
                    hideSprite(cross8)
                    spot8 = 0
                elif mouse[0] < 1381 and mouse[1] < 811 and mouse[0] > 1204 and mouse[1] > 644 and spot9 == 2 and turn == 1 and tool == 2:
                    i = 5
                    while i > 0:
                        pause(100)
                        changeSpriteImage(cross9, i)
                        i = i - 1
                    hideSprite(cross9)
                    spot9 = 0