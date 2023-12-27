
init python:
    class HakingGame():
        def __init__(self, time = 100, num = 6, timer = False):
            self.hp = 5
            self.splitChars = ';:./,"@#$%!-+^&*~\\(<'
            self.height = 20
            self.width = 16
            self.logList = []
            self.d = self.GetWordsFile(num)
            self.d2 = self.d.copy()
            random.shuffle(self.d2)
            self.listOfButtons1, self.listOfButtons2 = self.DoList()
            self.listSing1, self.listSing2 = self.DoListSing()
            self.words = self.GetWords()
            self.word = random.choice(self.words)
            self.words.remove(self.word)
            self.game_win = False
            self.timer = timer
            self.time = time
            self.start = False
        
        def GetWordsFile(self, num):
            f = [i.replace('\n', '').upper() for i in open(os.path.join( renpy.config.gamedir, f"passwords/New{num}.txt"))]
            return f

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
                                self.LogAdd('> '+'Доступ разрешён')
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
                                if self.hp < 1:
                                    self.LogAdd('> '+'Отказано в доступе')
                            flagre = True
                            break
                    if flagre:
                        break
            id2 = -1000