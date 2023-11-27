
init python:
    class HakingGame():
        def __init__(self, time = 100):
            self.hp = 5
            self.splitChars = ';:./,"@#$%!-+^&*~\\(<'
            self.height = 20
            self.width = 16
            self.logList = []
            self.d = 'saaransh saarathi saarbahn saarburg saaremaa saarinen saaristo saarland saarrthi saas-fee saaskula saasveld saathire saathiya saatkamp saavedra sabaayad sababurg sabadell sabadine sabadini sabaeans sabaeism sabalito sabalote sabalpur sabandan sabaneta sabantuy sabaoani sabareni sabariya sabarros sabatham sabatier sabatine sabatini sabatino sabatons sabaudia sabazios sabbarin sabbaths sabbatia sabbatic sabbaton sabbical sabburah sabeline sabellae sabellic sabellid sabercat sabering saberleg sabersaw sabethes sabieite sabinada sabinane sabinene sabinian sabiroba sabitzer sablayan sableize sabliere sabljari saboeiro saboraic saborios saborsko sabotage saboteur sabotier sabounee sabourin sabraogo sabratha sabrecat sabredav sabrejet sabreman sabrenet sabreurs sabreuse sabrinus sabritas sabrosky sabtenga sabucina sabudana sabuline sabulite sabulose sabulous sabunchi saburral sabzabad sabzawar sabzazar sabzevar sabzewar sabzvari sac-back sacabaya sacacoyo sacajewa sacalait sacaline sacaseni sacatons sacavemt sacbrood saccaded saccades saccadic saccardo saccated saccaton sacchar- sacchari hailfrom hailhail hailhale haililie hailings haillely haillike hailmary hailsham hailshot hailuoto haimhald hainbach hainberg hainburg hainfeld hainford haingura hainisch hainrode hainteny hainting haiphong hair-gel hair-lip hair-pin hairatan hairaway hairball hairband hairbell hairbird hairbows haircalf haircare haircell hairclip haircomb haircut1 haircuts hairdome hairdyes hairenik hairgate hairgels hairgrip hairiest hairkutt hairlace hairless hairlike hairline hairloss hairnets hairough hairpick hairpins hairseal hairsets hairslip hairston'.upper().split()
            self.d2 = self.d.copy()
            random.shuffle(self.d2)
            self.listOfButtons1, self.listOfButtons2 = self.DoList()
            self.listSing1, self.listSing2 = self.DoListSing()
            self.words = self.GetWords()
            self.word = random.choice(self.words)
            self.words.remove(self.word)
            self.game_win = False
            self.timer = False
            self.time = time
            
        def DoList(self):
            listOfButtons, ind, id = DoButtons(self.height, self.width, self.d2, self.splitChars, 0, 1)
            listOfButtons2, ind, id = DoButtons(self.height, self.width, self.d2, self.splitChars, ind, id)
            return listOfButtons, listOfButtons2

        def DoListSing(self):
            sing = random.randint(4096,65000)
            listSing1 = []
            listSing2 = []
            for i in range(self.height):
                listSing1.append(hex(sing))
                sing += 1
            for i in range(self.height):
                listSing2.append(hex(sing))
                sing += 1
            return listSing1, listSing2

        def GetWords(self):
            words = []
            for d in self.listOfButtons1 + self.listOfButtons2:
                for h in d:
                    if h[1] >= 0:
                        words.append((h[0],h[2]))
            return words

        def LogAdd(self, text):
            self.logList.append(text)
            if len(self.logList) > 8:
                self.logList.pop(0)

        def ClickCheck(self, id2):
            if id2 != -1000:
                flagre = False
                for d in [[[1,2,-1000]]] + self.listOfButtons1 + self.listOfButtons2:
                    for h in d:
                        if h[2] == id2:
                            if h[0] == self.word[0]:
                                self.LogAdd('> '+'Победа')
                                self.game_win = True
                            elif h[1] == -99:
                                if random.randint(1,5) == 1:
                                    self.hp = 5
                                    self.LogAdd('> '+'Попытки востановлены')
                                else:
                                    if len(self.words) != 0:
                                        f = random.choice(self.words)
                                        self.words.remove(f)
                                        for c1 in self.listOfButtons1 + self.listOfButtons2:
                                            for c2 in c1:
                                                if c2[2] == f[1]:
                                                    c2[0] = '.' * len(c2[0])
                                                    c2[1] = -1
                                        self.LogAdd('> '+'Обманка убрана')
                                h[1] = -1
                                h[0] = '.' * len(h[0]) 
                            elif h[1] == -1:
                                pass
                            elif h[1] != -1:
                                self.LogAdd('> '+h[0] + ' ' + str(check(h[0], self.word[0])))
                                for l in range(len(self.words)):
                                    if self.words[l][0] == h[0]:
                                        self.words.pop(l)
                                        break
                                h[0] = '.' * len(h[0])
                                h[1] = -1
                                self.hp -= 1
                            flagre = True
                            break
                    if flagre:
                        break
            id2 = -1000