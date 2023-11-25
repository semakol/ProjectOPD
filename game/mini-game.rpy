
init python:

    import random

    def DoButtons(height, width, d2, splitChars, ind, id):
        listOfButtons = [[] for i in range(height)]
        flag = True
        for y in range(height):
            k = 0
            while k < width:
                if id in (1,30):
                    id += 1
                    continue
                rand = random.randint(1, 30)
                if rand in range(1, 4) and flag:
                    ind += 1
                    but = d2[ind]
                    if (k + len(but) <= width):
                        listOfButtons[y].append([but, ind, id])
                        id += 1
                    flag = False
                elif rand in (5, 25) and flag:
                    if rand in (5, 9):
                        if random.randint(1,2) == 2 or width-k-2 <= 0:
                            listOfButtons[y].append([random.choice(('<', '>')), -(len(splitChars)-1)-1, -1])
                        else:
                            textBut = '<'
                            for i in range(random.randint(0, min(width-k-2, 5))):
                                textBut += splitChars[random.randint(0, len(splitChars)-3)]
                            textBut += '>'
                            listOfButtons[y].append([textBut, -99, id])
                            id += 1
                        flag = True
                    elif rand in (10, 25):
                        if random.randint(1,2) == 2 or width-k-2 <= 0:
                            listOfButtons[y].append([random.choice(('(', ')')), -(len(splitChars)-2)-1, -1])
                        else:
                            textBut = '('
                            for i in range(random.randint(0, min(width-k-2, 5))):
                                textBut += splitChars[random.randint(0, len(splitChars)-3)]
                            textBut += ')'
                            listOfButtons[y].append([textBut, -99, id])
                            id += 1
                        flag = True
                else:
                    ind1 = random.randint(0, len(splitChars)-3)
                    listOfButtons[y].append([splitChars[ind1], -ind1-1, -1])
                    flag = True
                k = len(''.join([i[0] for i in listOfButtons[y]]))
        return listOfButtons, ind, id

    def check(w1, w2):
        repeated = 0
        for s in range(len(w1)):
            if w1[s] == w2[s]:
                repeated += 1
        return repeated

define darker = Solid("72619c")
define brighter = Solid("c6bfd7")
define white = Solid("#fff")
define time_out = False
define font_hack = "consolas.ttf"

style mini_game_frame:
    xpadding 20
    ypadding 20

style mini_game_button:
    background "#000000"
    hover_background "#04408f"
    align (0.5, 0.5)
    xpadding 0
    top_padding 5
    bottom_padding 0

style mini_game_text:
    antialias True
    font font_hack
    justify True
    size 32
    color "08a"
    align (0.5, 0.5)

screen print(text1):
    zorder 100

    frame:
        style style.mini_game_frame
        xalign 1.0
        yalign 1.0
        xsize 0.2
        hbox:
            text '> ':
                style style.mini_game_text
                align (0.0, 0.0)
            text text1:
                style style.mini_game_text
                align (0.0, 0.0)
                slow_cps 50

screen game_timer(time):
    zorder 100

    if time < 1:
        timer 1 action [SetVariable('time_out', True), Hide('game_timer')]
    frame:
        style style.mini_game_frame
        xalign 1.0
        yalign 0.0  
        background "black"
        text hex(time)[2:].upper():
            style style.mini_game_text
            size 60
    timer 1 action [Hide('game_timer'),Show("game_timer", time = time - 1)]

screen click(id2, game):
    timer 0.00001 action [Show('miniGame', id2 = id2, game = game), Hide('click')]
        

screen miniGame(id2 = -1000, game = HakingGame()):
    $ game.ClickCheck(id2 = id2)
    if not(game.timer):
        timer 0.00001 action [Show('game_timer', time = game.time)]
        $ game.timer = True
    tag menu
    zorder 100
    if game.game_win:
        timer 0.00001 action [Return(value = True), Hide('print'), Hide('game_timer')]
    if game.hp == 0 or time_out:
        timer 0.00001 action [Return(value = False), Hide('print'), Hide('game_timer')]
    add 'miniFon.jpg'
    frame:
        style style.mini_game_frame
        xalign 0.0
        yalign 0.0
        background "black"
        hbox:
            for i in range(game.hp):
                text 'H':
                    style style.mini_game_text
                    size 60
    frame:
        style style.mini_game_frame
        xalign 0.3
        yalign 0.5

        vbox:
            for i in game.listOfButtons1:
                hbox:
                    for t in i:
                        button:
                            style style.mini_game_button
                            if (t[1] == -99) or (t[1] >= 0):
                                action Show("click", id2=t[2], game = game)
                            else:
                                action NullAction()
                            hovered Show('print', text1 = t[0])
                            unhovered Hide('print')
                            text t[0]:
                                style style.mini_game_text
    frame:
        style style.mini_game_frame
        xalign 0.7
        yalign 0.5

        vbox:
            for i in game.listOfButtons2:
                hbox:
                    for t in i:
                        button:
                            style style.mini_game_button
                            if (t[1] == -99) or (t[1] >= 0):
                                action Show("click", id2=t[2], game = game)
                            else:
                                action NullAction()
                            hovered Show('print', text1 = t[0])
                            unhovered Hide('print')
                            text t[0]:
                                style style.mini_game_text
    frame:
        style style.mini_game_frame
        yanchor 1.0
        xalign 1.0
        xsize 0.2
        ypos 0.94
        
        vbox:
            for i in game.logList:
                text i:
                    style style.mini_game_text
                    align (0.0, 0.0)
    frame:
        style style.mini_game_frame
        xalign 0.19
        yalign 0.5
        vbox:
            for i in game.listSing1:
                button:
                    style style.mini_game_button
                    text i:
                        style style.mini_game_text
    
    frame:
        style style.mini_game_frame
        xalign 0.55
        yalign 0.5
        vbox:
            for i in game.listSing2:
                button:
                    style style.mini_game_button
                    action NullAction()
                    text i:
                        style style.mini_game_text
   
    


