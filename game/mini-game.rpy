
style mini_game_frame:
    background None
    xpadding 20
    ypadding 20

style mini_game_frame_console:
    background None
    xpadding 5
    ypadding 5

style mini_game_button:
    background None
    hover_background "#04408f"
    align (0.5, 0.5)
    xpadding 0
    top_padding 5
    bottom_padding 0

style mini_game_text:
    background None
    antialias True
    font font_hack
    justify True
    size 32
    color "08a"
    align (0.5, 0.5)



init python:

    import random

    darker = Solid("72619c")
    brighter = Solid("c6bfd7")
    white = Solid("#fff")
    time_out = False
    font_hack = "consolas.ttf"
    screen_on = True

    def PrinText(st, at):
        return Text(prtext, slow = 50, color = "08a"), .2

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

screen con():
    frame:
        style style.mini_game_frame_console
        align (0.0, 1.0)
        button:
            hover_background "#04408f"
            action [Return(), Hide("con", transition=fade), Hide("text_con", transition=fade)]
            text 'Пропустить':
                style style.mini_game_text
                align (0.0, 0.0)
                size 50
                slow_cps 10
    timer 2 action Show("text_con")

screen text_con(t = '',y = 300):
    add 'images/bg/cont.png'
    frame:
        style style.mini_game_frame_console
        xalign 0.5
        ypos y
        text 'Игру разработали:\n\nКоманда "P&S.Gang"\n\nТимлид:        Ковшевников Павел\nРазработчик:   Колыванов Семён\nДизайнер:      Коньшин Антон\nГейм-Дизайнер: Тюриков Данил\nАналитик:      Романов Станислав\n                            \nСпасибо что играли <3':
            style style.mini_game_text
            color '#07f7eb'
            size 45
            slow_cps 8

screen pass_game():
    frame:
        style style.mini_game_frame_console
        align (0.0, 1.0)
        button:
            hover_background "#04408f"
            action [Return(value = True), Hide("pass_game")]
            text 'Пропустить':
                style style.mini_game_text
                align (0.0, 0.0)
                size 50
                slow_cps 10


screen print(text1):
    zorder 100
    frame:
        style style.mini_game_frame_console
        pos (1564, 946)
        xysize (280, 40)
        hbox:
            text '> ':
                style style.mini_game_text
                align (0.0, 0.0)
            text text1:
                style style.mini_game_text
                align (0.0, 0.0)
                slow_cps 30

screen tutorial():
    zorder 101
    add "tutorial.png"
    frame:
        style style.mini_game_frame
        align (1.0, 0.0)
        button:
            background "black"
            hover_background "#04408f"
            action [Hide('tutorial'), SetVariable('screen_on', True)]
            text "Закрыть":
                style style.mini_game_text
                size 48

screen win():
    zorder 101
    add "win.png":
        align (0.5, 0.5)

screen fin():
    zorder 101
    add "fin.png":
        align (0.5, 0.5)
                
screen game_timer(time, game):
    zorder 100

    if time < 1:
        timer 1 action [SetVariable('time_out', True), Hide('game_timer'), Show("click", id2 = -1000, game = game)]
    frame:
        style style.mini_game_frame
        pos (1562, 83)
        xysize (242, 144)
        text hex(time)[2:].upper():
            style style.mini_game_text
            size 100
    timer 1 action [Hide('game_timer'),Show("game_timer", time = time - 1, game = game)]

screen click(id2, game):
    timer 0.00001 action [Show('miniGame', id2 = id2, game = game), Hide('click')]
        

screen miniGame(id2 = -1000, game = HakingGame()):
    $ game.ClickCheck(id2 = id2)
    $ text2 = ''
    if not(game.start):
        $ game.start = True
        timer 0.01 action [SetVariable('screen_on', True), SetVariable('time_out', False)]
    if not(game.timer):
        timer 0.00001 action [Show('game_timer', time = game.time, game = game)]
        $ game.timer = True
    tag menu
    zorder 100
    if game.game_win:
        timer 0.1 action [SetVariable('screen_on', False), Show('win', transition=dissolve), Hide('game_timer'), Play("audio", 'audio/effects/win_sound.ogg')]
        timer 4 action [Return(value = True), Hide('print'), Hide('game_timer'), Hide('tutorial'), Hide('win'), Hide('click'), Hide('print'), Hide('miniGame'), SetVariable('screen_on', True)]
    if game.hp == 0 or time_out:
        timer 0.1 action [SetVariable('screen_on', False), Show('fin', transition=dissolve), Hide('game_timer'), Play("audio", 'audio/effects/fin_sound.ogg')]
        timer 4 action [Return(value = False), Hide('print'), Hide('game_timer'), Hide('tutorial'), Hide('fin'), Hide('click'), Hide('print'), Hide('miniGame'), SetVariable('screen_on', True)]
    add 'miniFon.jpg'
    add 'mini_game_mon.png'
    frame:
        style style.mini_game_frame
        pos (80, 520)
        xysize (120, 200)
        button:
            style style.mini_game_button
            if screen_on:
                action [Show('tutorial'), SetVariable('screen_on', False)]
            text "Помощь":
                style style.mini_game_text
    frame:
        style style.mini_game_frame
        pos (98, 69)
        xysize (130, 400)
        vbox:
            spacing 15
            align (0.5, 0.5)
            for i in range(game.hp):
                text 'H':
                    style style.mini_game_text
                    size 62
                    if game.hp == 1:
                        color "#b90a04"
    frame:
        style style.mini_game_frame
        pos (493, 146)
        xysize (360, 800)

        vbox:
            align (0.5, 0.5)
            for i in game.listOfButtons1:
                hbox:
                    for t in i:
                        button:
                            style style.mini_game_button
                            if screen_on:
                                if (t[1] == -99) or (t[1] >= 0):
                                    action [Show("click", id2=t[2], game = game), SetVariable('screen_on', True)]
                                    activate_sound "audio/effects/keyboard.mp3"
                                else:
                                    action NullAction()
                            hovered [Show('print', text1 = t[0])]
                            unhovered [Hide('print')]
                            
                            text t[0]:
                                style style.mini_game_text
    frame:
        style style.mini_game_frame
        pos (1073, 146)
        xysize (360, 800)

        vbox:
            align (0.5, 0.5)
            for i in game.listOfButtons2:
                hbox:
                    for t in i:
                        button:
                            style style.mini_game_button
                            if screen_on:
                                if (t[1] == -99) or (t[1] >= 0):
                                    action [Show("click", id2=t[2], game = game), SetVariable('screen_on', True)]
                                    activate_sound "audio/effects/keyboard.mp3"
                                else:
                                    action NullAction()
                            hovered Show('print', text1 = t[0])
                            unhovered Hide('print')

                            text t[0]:
                                style style.mini_game_text
    frame:
        style style.mini_game_frame_console
        pos (1564, 388)
        xysize (280, 558)
        
        vbox:
            yalign 1.0
            for i in game.logList:
                text i:
                    style style.mini_game_text
                    if i == '> Доступ разрешён':
                        color "#14cf24"
                    elif i == '> Отказано в доступе':
                        color "#b90a04"
                    align (0.0, 1.0)
    frame:
        style style.mini_game_frame
        pos (353, 146)
        xysize (140, 800)
        vbox:
            align (0.5, 0.5)
            for i in game.listSing1:
                button:
                    style style.mini_game_button
                    action NullAction()
                    text i:
                        style style.mini_game_text
    
    frame:
        style style.mini_game_frame
        pos (933, 146)
        xysize (140, 800)
        vbox:
            align (0.5, 0.5)
            for i in game.listSing2:
                button:
                    style style.mini_game_button
                    action NullAction()
                    text i:
                        style style.mini_game_text
   
    


