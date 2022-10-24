from pygame_functions import *
#  // burger
def blackjack():
    showhitxt = 0
    showlosetxt = 0
    player_turn = 0
    bot_turn = 0
    count_ch = 0
    count_bot = 0
    count_quit = 0
    count = 0
    hack = 0
    screen = screenSize(1920, 1080)
    dlcardpos2 = 950
    dlcardpos3 = 1000
    i = 0
    plcardy = 775
    dlcardy = 330
    setBackgroundImage(["ressources/bj.jpg"])
    border = makeSprite("ressources/border.png")
    player_card1 = makeSprite("ressources/cardpl1.png")
    player_card2 = makeSprite("ressources/cardpl2.png")
    dl_card1 = makeSprite("ressources/dlcard1.png")
    dl_card2 = makeSprite("ressources/dlcard2.png")
    rect1 = makeSprite("ressources/rect1.png")
    rect2 = makeSprite("ressources/rect2.png")
    back_card2 = makeSprite("ressources/backcard.png")
    hit = makeSprite("ressources/hit.png")
    stand = makeSprite("ressources/stand.png")
    score1 = makeLabel("17", 36, 945, 900, fontColour='white')
    score2 = makeLabel("21", 36, 960, 450, fontColour='white')
    score3 = makeLabel("21", 36, 945, 900, fontColour='white')
    score4 = makeLabel("17", 36, 960, 450, fontColour='white')
    texthit = makeLabel("Ah le paquet de carte est vide, mince...", 36, 200, 200, fontColour='white')
    textboxlose = makeLabel("Blackjack pour le dealer, dommage... Appuie sur 'p' pour rejouer", 30, 200, 200, fontColour='white')
    textboxwin = makeLabel("Aie, c'est vrai que vous pouvez juste me racketter et me voler la carte... Vous avez gagné", 30, 200, 200, fontColour='white')
    posx = mouseX()
    posy = mouseY()
    #showSprite(border)
    moveSprite(player_card1, 920, 775)
    moveSprite(player_card2, 950, 775)
    moveSprite(dl_card1, 920, 330)
    moveSprite(back_card2, 950, 330)
    moveSprite(hit, 806, 494)
    moveSprite(stand, 1050, 494)
    moveSprite(rect1, 200, 200)
    moveSprite(rect2, 200, 200)
    showSprite(player_card1)
    pause(300)
    showSprite(player_card2)
    pause(300)
    showSprite(dl_card1)
    pause(300)
    showSprite(back_card2)
    pause(300)
    showLabel(score1)
    player_turn = 1
    showSprite(hit)
    showSprite(stand)

    while True:
        if (spriteClicked(hit) == True and player_turn == 1):
            transformSprite(hit, 0, 0.75)
            pause(75)
            transformSprite(hit, 0, 1)
            pause(75)
            showhitxt = 1
        if (spriteClicked(stand) == True and player_turn == 1):
            transformSprite(stand, 0, 0.75)
            pause(75)
            transformSprite(stand, 0, 1)
            pause(75)
            player_turn = 0
            bot_turn = 1
            hideSprite(hit)
            hideSprite(stand)
        if (showhitxt == 1):
            textboxhit = makeTextBox(200, 200, 635, case=0, startingText='Ah le paquet de carte est vide, mince...', maxLength=0, fontSize=36)
            pause(1500)
            hideTextBox(textboxhit)
            showhitxt = 0
        if (bot_turn == 1):
            if (dlcardpos2 != 1000 and count_bot != 1):
                moveSprite(back_card2, dlcardpos2 + 1, 330)
                dlcardpos2 += 1
            elif (dlcardpos2 == 1000 and count_ch == 0):
                count_ch = 1
            elif (count_ch == 1 and count_bot != 1):
                hideSprite(back_card2)
                count_bot = 1
            elif (count_bot == 1):
                showSprite(dl_card2)
                if (dlcardpos3 >= 950):
                    moveSprite(dl_card2, dlcardpos3 - 1, 330)
                    dlcardpos3 -= 1
                if (dlcardpos3 == 949):
                    if (hack != 1):
                        showLabel(score2)
                        showSprite(rect1)
                        showLabel(textboxlose)
                    if (spriteClicked(dl_card2) == True):
                        hack = 1
                    if (keyPressed(keyCheck='p') == True):
                        count_bot = 0
                        dlcardpos3 = 1000
                        hideSprite(dl_card2)
                        count_ch = 0
                        dlcardpos2 = 950
                        bot_turn = 0
                        hideLabel(textboxlose)
                        hideLabel(score2)
                        player_turn = 1
                        moveSprite(back_card2, 950, 330)
                        hideSprite(dl_card1)
                        hideSprite(player_card1)
                        hideSprite(player_card2)
                        hideLabel(score1)
                        hideSprite(rect2)
                        hideSprite(rect1)
                        blackjack()
                        return 1
                    if (hack == 1 and dlcardy != 780):
                        moveSprite(dl_card2, 949, dlcardy + 2)
                        dlcardy += 2
                    if (hack == 1 and plcardy >= 330):
                        moveSprite(player_card2, 985, plcardy - 2)
                        plcardy -= 2
                    if (hack == 1 and dlcardy == 780 and plcardy < 330):
                        hideLabel(score1)
                        hideLabel(score2)
                        showLabel(score3)
                        showLabel(score4)
                        hideLabel(textboxlose)
                        showSprite(rect2)
                        showLabel(textboxwin)
                        pause(3000)
                        hideLabel(textboxwin)
                        hideLabel(score3)
                        hideLabel(score4)
                        hideSprite(player_card1)
                        hideSprite(player_card2)
                        hideSprite(rect1)
                        hideSprite(rect2)
                        hideSprite(dl_card1)
                        hideSprite(dl_card2)
                        count_quit = 1
                        return 1


        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()