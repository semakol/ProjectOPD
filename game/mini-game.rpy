
init python:
    import random
    d = "ancoming almoning ambuling attering atwiting astoning building bylining hairgrip hairiest hairkutt hairlace hairless hairlike hairline hairloss hairnets hairough hairpick hairpins hairseal hairsets hairslip hairston hairtail hairties hairweed hairwood hairwork hairworm hairyair hairyape haiseiko haisiyat haitanna haitches haitians haivoron haiwatha haizidao hajariya hajatria hajdaraj hajikano hajinski hajipour hajiwala hajjateh hajjilar hajjileh hajjiyeh hajnacka hajrovic hajtovka hajvalia hakafoth hakahana hakallen hakamada hakamaii hakanpaa hakapiks hakauata hakeborn hakelike haketone haketons hakewill hakimpet hakkafot hakkaria hakkasan hakkinen hakkoryu hakobune hakobyan hakodate haksberg hakuhodo hakunila hakuraku hakutaka halabiye halachah halachic halachos halachot halaesus halafian halagama halaguru halahala halakere halakhic halal-tv halalcor halamish halapada halapeno halapepe halarteh halasana halashby halastus halaszle halation halaveli halazone halbania halbarga halbblut halberds halberts halblech halbrook halbryce halbturn halbzeit halchita halcombe halcones halcurin halcydon halcyons haldanes haldavid haldeman halderze haldipur haldreka haldreyn haldwani halebank halebidu halebopp haleburg haleciid halecina halecium halecize halecoid halecret halehsam halehunt halekota halemweg haleness halenkov halensee halesite halesome halestan haleweyn halewijn halewood haleyuru halfpeso halfpike halfpint halfpipe halfrest halfseen halfsies halfslip halfsole halfstep halfterm halftime halftone halftrue halfturn halfwave halfways".upper().split()
    splitChars = ';:./,"@#$%^&*~()<>'
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
            if random.randint(1, 5) == 1 and flag:
                ind += 1
                but = d2[ind]
                if (k + len(but) <= width):
                    listOfButtons[y].append((but, ind))
                    flag = False
                elif (k + len(but) > width) and (y != height-1):    
                    listOfButtons[y].append((but[0:width - k],ind))
                    listOfButtons[y+1].append((but[width - k:len(but)], ind))
                    flag = False
                    break
                else:
                    ind1 = random.randint(0, len(splitChars)-1)
                    listOfButtons[y].append((splitChars[ind1], -ind1-1))
                    flag = True
            else:
                ind1 = random.randint(0, len(splitChars)-1)
                listOfButtons[y].append((splitChars[ind1], -ind1-1))
                flag = True
            k = len(''.join([i[0] for i in listOfButtons[y]]))


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
                                if (t[1] >= 0):
                                    action Notify(d2[t[1]])
                                else:
                                    action Notify(splitChars[abs(t[1])-1])
                            align (0.5, 0.5)
                            hovered Show("co", hov = t[1])
                            unhovered Show("co", hov = -100)
                            xpadding 0
                            top_padding 5
                            bottom_padding 0

                            text t[0]:
                                font font_hack
                                justify True
                                size 32
                                color "08a"
                                align (0.5, 0.5)



