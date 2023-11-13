
init python:
    import random
    d = "aboba aboba aboba aboba aboba aboba aboba aboba aboba aboba aboba aboba aboba aboba aboba aboba aboba aboba aboba aboba aboba aboba aboba aboba aboba aboba aboba aboba aboba aboba aboba aboba aboba aboba aboba aboba aboba aboba aboba aboba".upper().split()
    splitChars = ';:./,"@#$%^&*~\\(<'
    d2 = d.copy()
    random.shuffle(d2)
    height = 20
    width = 16
    listOfButtons = [[] for i in range(height)]
    flag = True
    ind = 0
    for y in range(height):
        k = 0
        while k < width:
            rand = random.randint(1, 30)
            if rand in range(1, 5) and flag:
                ind += 1
                but = d2[ind]
                if (k + len(but) <= width):
                    listOfButtons[y].append([but, ind])
                    flag = False
                elif (k + len(but) > width) and (y != height-1):    
                    listOfButtons[y].append([but[0:width - k],ind])
                    listOfButtons[y+1].append([but[width - k:len(but)], ind])
                    flag = False
                    break
                else:
                    ind1 = random.randint(0, len(splitChars)-3)
                    listOfButtons[y].append([splitChars[ind1], -ind1-1])
                    flag = True
            elif rand in (5, 7) and flag:
                if rand == 5:
                    listOfButtons[y].append(['<', -(len(splitChars)-1)-1])
                    flag = True
                if rand == 6:
                    listOfButtons[y].append(['(', -(len(splitChars)-2)-1])
                    flag = True
            else:
                ind1 = random.randint(0, len(splitChars)-1)
                listOfButtons[y].append([splitChars[ind1], -ind1-1])
                flag = True
            k = len(''.join([i[0] for i in listOfButtons[y]]))
        for x in range(0, len(listOfButtons[y])-1):
            flag2 = False
            if listOfButtons[y][x][0] == '<' and listOfButtons[y][x+1][1] < 0:
                flag3 = False
                for x2 in range(x+1, len(listOfButtons[y])):
                    if (random.randint(1, 5) == 1 or listOfButtons[y][x+1][1] > 0) and flag3:
                        listOfButtons[y][x][0] = listOfButtons[y][x][0][0:len(listOfButtons[y][x][0])-1]
                        listOfButtons[y][x][0] += '>'
                        listOfButtons[y][x][1] = -99
                        flag2 = True
                        break 
                    elif listOfButtons[y][x+1][1] < 0:
                        listOfButtons[y][x][0] += listOfButtons[y][x+1][0]
                        listOfButtons[y].pop(x+1)
                        flag2 = True
                        flag3 = True
                    else:
                        listOfButtons[y][x][0] = listOfButtons[y][x][0][0:len(listOfButtons[y][x][0])-1]
                        listOfButtons[y][x][0] += '>'
                        listOfButtons[y][x][1] = -99
                        flag2 = True
                        break
            if listOfButtons[y][x][0] == '(' and listOfButtons[y][x+1][1] < 0:
                flag3 = False
                for x2 in range(x+1, len(listOfButtons[y])):
                    if (random.randint(1, 5) == 1 or listOfButtons[y][x+1][1] > 0) and flag3:
                        listOfButtons[y][x][0] = listOfButtons[y][x][0][0:len(listOfButtons[y][x][0])-1]
                        listOfButtons[y][x][0] += ')'
                        listOfButtons[y][x][1] = -99
                        flag2 = True
                        break 
                    elif listOfButtons[y][x+1][1] < 0:
                        listOfButtons[y][x][0] += listOfButtons[y][x+1][0]
                        listOfButtons[y].pop(x+1)
                        flag2 = True
                        flag3 = True
                    else:
                        listOfButtons[y][x][0] = listOfButtons[y][x][0][0:len(listOfButtons[y][x][0])-1]
                        listOfButtons[y][x][0] += ')'
                        listOfButtons[y][x][1] = -99
                        flag2 = True
                        break
            if flag2:
                break
                        
    


define darker = Solid("72619c")
define brighter = Solid("c6bfd7")
define white = Solid("#fff")

define font_hack = "consolas.ttf"

style button:
    background "#000000"
    hover_background "#04408f"

style button_hover:
    background "#04408f"

screen co(hov):
    zorder 100
    timer 0.00000001 action [Show('countdown', hov1 = hov), Hide("co")]

screen countdown(hov1 = -100):
    tag menu
    zorder 0
    $ hov = hov1
    frame:
        xpadding 20
        ypadding 20
        xalign 0.5
        yalign 0.5

        vbox:
            for i in listOfButtons:
                hbox:
                    for t in i:
                        button:
                            if hov == t[1] and (t[1] >= 0):
                                style style.button_hover
                                action Notify(d2[t[1]])
                            else:
                                style style.button
                                if (t[1] == -99):
                                    action Notify('da')
                                elif (t[1] >= 0):
                                    action Notify(d2[t[1]])
                                else:
                                    action Notify(splitChars[abs(t[1])-1])
                            align (0.5, 0.5)
                            hovered [Show("co", hov = t[1])]
                            unhovered [Show("co", hov = -100)]
                            xpadding 0
                            top_padding 5
                            bottom_padding 0

                            text t[0]:
                                antialias True
                                font font_hack
                                justify True
                                size 32
                                color "08a"
                                align (0.5, 0.5)



