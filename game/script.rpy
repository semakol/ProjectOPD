﻿define I = Character('Игорь', color="#1d831d")
define D = Character('Давид', color="#b3e00f")
define aut = Character('', color='#c8ffc8')
define tel = Character('Телефон', color='#989c72')
define VP = Character('Виктор П.', color='#da3535')
define ved = Character('Ведущая', color='#383acc')
define cor = Character('Марина', color='#1c42f0')
define nei = Character('Неизвестный', color='#fefff1')
define O = Character('Ольга', color='#8a44e6')
define Al = Character('Александр', color='#5f05a8')
define M = Character('Михаил', color='#7933fc')
define S = Character('София', color='#8db913')



$ rascazal = False
$ Vzlomal = False

label start1:

    # call screen tutorial

    

    'Погнали'

    $ flag = True
    while flag:
        $ miniGame1 = HakingGame(5, 6)
        call screen miniGame(game = miniGame1)
        $ miniGame1 = None

        if _return:
            I 'Хорошо получилось'
        else:
            I 'Не получилось'
        menu:
            I ''
            
            'Попробовать ещё':

                pass

            'Закончить':

                $ flag = False

    return

label start: # старт

    show screen scene_num(1)
    
    scene menu_bg2 with fade
    
    aut 'Кибербург, 20** год. Технологии достигают своего совершенства. Люди все свои данные хранят в интернете, а за их безопасность отвечает федеральная компания “КиберЛок”'

    jump scene2

    return

label scene2: # Новости

    show screen scene_num(2)

    play sound 'audio/effects/news.mp3' fadein 0.5 volume 0.15 noloop

    scene studia with fade

    ved 'Доброе утро, Кибербург! Меня зовут Екатерина и я приветствую вас на ежедневном выпуске новостей!'

    ved 'Именно сегодня юбилей компании “Киберлок”!'

    ved 'Уже 20 лет они занимаются сохранностью наших данных, кроме того, компания известна своими вкладами в благотворительность, только за прошедший год компания пожертвовала в благотворительный фонд 500 миллионов рублей.'

    ved 'В честь такого знаменательного события наш корреспондент берёт интервью у главы отдела кибербезопасности. Передаю слово корреспонденту.'

    jump scene3

    return
        
label scene3: # Интерьвью

    show screen scene_num(3)

    scene enter_kyberlok with fade

    play ambient 'audio/effects/veter.mp3' fadein 2.0 volume 0.5

    cor 'Спасибо, Екатерина. Меня зовут Мария и прямо сейчас я с главой отдела кибербезопасности стоим у главного офиса компании “КиберЛок”.'

    cor 'Здравствуйте, Игорь Олегович! Для начала, хотим поздравить вас с этим знаменательным днём!'

    I 'Спасибо большое, Мария. Для меня большая честь работать в “КиберЛоке” и приносить пользу людям.'

    cor 'Нам известно, что в данный момент вы глава отдела кибербезопасности. Можете-ли вы немного рассказать с чего вы начинали свой путь в этой компании?'

    I 'Да, с удовольствием. Я начинал работать в “КиберЛоке” специалистом кибербезопасности.'

    $ flag = True
    while flag:
        menu:
            I ''
            'Одной из основных задач является защита информационных систем от кибератак, обеспечение безопасности сетей, а также анализ и минимизация рисков для компании в целом.':

                $ flag = False

            'Специалист кибербезопасности занимается созданием базовы алгоритмов и управлением шифрованием для защиты данных.':

                I 'Такой ответ вы услышали бы от непрофессионального специалиста кибербезопасности.'

    cor 'Спасибо, Игорь. Расскажите нам какие компетенции необходимы, чтобы успешно работать в области кибербезопасности?'

    $ flag = True
    while flag:
        menu:
            I ''
            'Важно иметь навыки хакерства, знание о механизмах взлома паролей, а также умение создавать и распространять вирусы для анализа безопасности информационных систем.':

                I 'Именно так ответил бы я вам, если бы любил врать. На самом деле…'

            'Важно иметь глубокое понимание сетевых протоколов, знание в области криптографии, умение работать с различными системами безопасности, а также навыки анализа уязвимостей.':

                $ flag = False

    cor 'Какие методы вы используете для предотвращения кибератак?'

    $ flag = True
    while flag:
        menu:
            I ''
            'Мы используем методы социальной инженерии, чтобы получить доступ к конфиденциальной информации. Также мы распространяем вредоносные программы, чтобы проверить, как системы справляются с угрозами.':

                I 'И это шутка! В действительности…'

            'Мы применяем многоуровневые защитные стратегии, использование современных антивирусов, брандмауэров, систем обнаружения вторжений, а также постоянно анализируем новые угрозы.':

                $ flag = False

    cor 'Каким образом происходит обнаружение и анализ возможных угроз в вашей работе?'

    $ flag = True
    while flag:
        menu:
            I ''
            'Мы используем специальные программные решения для мониторинга сетевого трафика, системы обнаружения вторжений, а также проводим аудит системы на предмет уязвимостей.':

                $ flag = False

            'В нашей работе мы редко сталкиваемся с угрозами, так как наши системы безопасности абсолютно непроницаемы для любых атак. Нам не требуется обнаружение или анализ угроз, так как мы всегда на шаг впереди.':

                I 'Ну, ясно, что это был не лучший ответ. Давайте поговорим о правильном подходе к этой задаче.'

    cor 'Каковы основные вызовы, с которыми вы сталкиваетесь в работе Специалиста кибербезопасности?'

    $ flag = True
    while flag:
        menu:
            I ''
            'Одним из основных вызовов является постоянно меняющаяся угрозная среда. Это требует постоянного обновления знаний и технических средств, чтобы оставаться впереди потенциальных атак.':

                $ flag = False

            'Главный вызов для нас - это не уснуть во время слежения за мониторами. Но мы стараемся держаться в форме, чтобы не упустить возможную угрозу.':

                I 'И это неправильный ответ. Иногда мы ошибаемся, и это нормально. Важно не стоять на месте и продолжать учиться из своих ошибок. Сейчас давайте рассмотрим правильный ответ.'

    cor 'Благодарю вас за интересный разговор и ценные ответы на вопросы! Я и наши телезрители узнали много нового!'

    stop ambient

    jump scene4
    
    return

label scene4: # Тренировка

    show screen scene_num(4)

    scene main_office with fade

    play ambient 'audio/effects/office.mp3' fadein 2.0 volume 0.1

    I 'Давид опять не пришёл вовремя. Пока его нет я могу потренироваться.'
    
    $ flag = True
    while flag:
        stop ambient fadeout 0.5
        $ miniGame1 = HakingGame(0, 6, True)
        call screen miniGame(game = miniGame1) with dissolve
        $ miniGame1 = None
        play ambient 'audio/effects/office.mp3' fadein 2.0 volume 0.1
        if _return:
            I 'Хорошо получилось'
        else:
            I 'Не получилось'

        menu:
            I ''
            'Попробовать ещё':

                pass

            'Закончить':

                $ flag = False

    show david with dissolve

    D 'Извини, опоздал'

    I 'Ну привет, Давид, опять опаздываешь. Почему не пришёл на интервью, мы должны были присутствовать оба?'

    D 'Извини, Игорь. Но мне срочно нужно было приехать в больницу к сестре.'

    I 'Ой, извини. Как её состояние?'

    D 'Нормально. Я не хочу сейчас об этом говорить.'

    I 'Пока тебя не было, я обнаружил несколько странных активностей в сети нашей компании. Проведенная нами проверка системы безопасности раскрыла некоторые подозрительные действия.'

    D 'Звучит серьёзно.'

    I 'Сначала нам нужно провести более глубокое исследование. Нужно проверить логи и журналы, чтобы вы могли анализировать данные на предмет несанкционированного доступа или подозрительной активности'

    menu:
        I ''
        'Я займусь анализом этих активностей.':
            D 'Понял, тогда я проверю логи и журналы.'
        
        'Приступим к работе, я займусь логами.':
            D 'Хорошо, приступаю к анализу.'
    
    $ flag = True
    while flag:
        stop ambient fadeout 0.5
        $ miniGame1 = HakingGame(120, 7)
        call screen miniGame(game = miniGame1) with dissolve
        $ miniGame1 = None
        play ambient 'audio/effects/office.mp3' fadein 2.0 volume 0.1
        if _return:
            I 'Хорошо получилось'
            $ flag = False
        else:
            I 'Не получилось'
            

    jump scene5

label scene5: # Нападение

    show screen scene_num(5)

    D 'Игорь! В системе найден скрипт удалённого доступа. Код красный, они положили антивирус и запустили ещё больше вредоносного ПО.'

    hide david

    show monitor with dissolve 

    I 'Да, вижу. Они слишком быстро входят в систему, нужно заняться обороной и контр-атакой. Если мы не поторопимся, у них будет полный контроль.'

    D 'Доверь оборону мне, а ты займись контр-атакой, постарайся вычислить их.'

    $ choices = ['Заняться восстановлением антивируса', 'Починить систему мониторинга сетевого трафика', 'Восстановить данные из резервных копий.']
    $ flag = 0
    while flag < 3:
        menu:
            I ''
            '[choices[0]]':
                if choices[0] == '(Выполнен)':
                    pass
                else:
                    D 'Антивирус повреждён, но не сильно. Его восстановление не должно занять много времени.'

                    D 'Готово, антивирус снова в норме.'

                    I 'Хорошая работа. Я запустил дополнительные слои шифрования и система блокировок снова работает.'

                    $ flag += 1
                    $ choices[0] = '(Выполнен)'
            '[choices[1]]':
                if choices[1] == '(Выполнен)':
                    pass
                else:
                    I 'Надо заняться системами мониторинга.'

                    I 'Я смог настроить брандмауэры и системы обнаружения вторжений для активного мониторинга и фильтрации сетевого трафика.'

                    D 'Отлично. Я изолировал атакованные сегменты сети, чтобы предотвратить распространение атаки на другие части системы.'

                    $ flag += 1
                    $ choices[1] = '(Выполнен)'
            '[choices[2]]':
                if choices[2] == '(Выполнен)':
                    pass
                else:
                    D 'Нужно восстановить данные из резервных копий, иначе мы рискуем их потерять.'

                    D 'Все данные в порядке.'

                    I 'Супер, что ещё нужно сделать?'

                    $ flag += 1
                    $ choices[2] = '(Выполнен)'
    
    D 'Фух, мы побеждаем. Они отступили, видимо, поняли, что мы почти их вычислили.'

    I 'С моей стороны тоже всё хорошо. Контроль хакеры не получили и данные не украли. А мы даже смогли перехватить один файл, но он зашифрован.'

    jump scene6

label scene6: # Расшифровка

    show screen scene_num(6)

    play sound 'audio/effects/shagi.ogg' noloop

    scene main_office with dissolve

    show david with dissolve

    I 'Я и забыл, сегодня же к нам приводят студентов. “КиберЛок” умеет привлекать новых людей, особенно в такие праздники.'

    I 'Мы должны провести им экскурсию и рассказать им про этот отдел.'

    D 'Насыщенный сегодня день. Я уже устал от сегодняшнего инцидента, а ещё нужно поработать экскурсоводом.'

    I 'Раз ты опоздал на интервью, то экскурсия на тебе.'

    D 'Вечно ты оставляешь всё самое сложное мне.'

    I 'Я верю в твоё красноречие, удачи. Я пока займусь расшифровкой файла.'

    hide david with dissolve

    I 'Надо изучить этот файл.'

    $ flag = True
    while flag:

        stop ambient fadeout 0.5
        $ miniGame1 = HakingGame(100, 8)
        call screen miniGame(game = miniGame1)
        $ miniGame1 = None
        play ambient 'audio/effects/office.mp3' fadein 2.0 volume 0.1

        if _return:
            I 'Хорошо получилось'
            $ flag = False
        else:
            I 'Не получилось'

            I 'Надо ещё раз'

    I 'Ну вот, файл расшифрован на 80\%. Дальше справится система.'

    I 'Надо посмотреть как идут дела у Давида.'

label scene7: # Студенты

    show screen scene_num(7)

    play ambient 'audio/effects/office.mp3' fadein 2.0 volume 0.01

    scene intervie with fade

    D 'Вот какие профессии занимаются в этом отделе. А сейчас расскажу вам про самую интересную, про мою.'

    D 'Я работаю Специалистом кибербезопасности, я занимаюсь защитой компьютерных систем, сетей и данных от хакерских атак и других киберугроз.'

    D 'Моя главная задача - обеспечить безопасность информационных технологий и минимизировать риски несанкционированного доступа, утечек данных и других киберпреступлений.'
    
    D 'Специалисты кибербезопасности проектируют, внедряют и поддерживают различные технические решения и меры защиты, такие как брандмауэры, системы обнаружения вторжений, шифрование данных и антивирусное программное обеспечение.'

    D 'Занимаются управлением рисками, анализом уязвимостей, реагирование на инциденты.'

    I 'Всё правильно. Наша специальность очень интересна и полезна. Поэтому мы с моим коллегой будем рады увидеть вас снова в нашем отделе, но уже как трудоустроенных.'

    jump scene8

    return

label scene8: # Осмотр файла

    show screen scene_num(8)

    scene main_office with fade

    show david

    D 'Хватит на сегодня экскурсиями. Что там с файлом?'

    I 'Сейчас посмотрю.'

    I '(думает) Боже, это же файл не про хакеров, а про “Киберлок”. Я думал они занимаются защитой данных.'

    I '(думает) Должен-ли я делиться с кем-нибудь этой информацией. Если *Главный Совет* компании узнает, что я расшифровал этот файл и поделился содержимым с кем-то ещё, то неприятности будут у меня и у всех, кто узнает.'

    I '(думает) Но с другой стороны, я не могу оставить это, сложа руки. И один остановить это я не смогу.'

    menu:
        I ''
        'Рассказать Давиду':
            I 'Давид… ты должен это увидеть, только тихо.'

            D 'Что? Что там?'

            I 'Видимо этот файл был целью кибер-атаки. Тут сказано про все данные, которые “Киберлок” продала на чёрном рынке.'

            I 'Не могу в это поверить. Мы должны остановить это. Мы можем раскрыть членов *Главного Совета* и слить файл в органы, тогда их посадят.'

            aut '*Лицо Давида побледнело и стало тревожным*'

            D 'Как такое возможно…'

            I 'Давид, если мы объединим свои силы, то сможем это остановить.'

            D 'Извини, Игорь, мне надо отлучиться.'

            $ rascazal = True
        'Не рассказывать Давиду':
            D 'Ты долго будешь всматриваться? Что там?'

            I 'Ничего особенно. Просто письмо от одного из пользователей в техподдержку.'

            D 'Тогда почему он зашифрован?'

            I 'Видимо из-за сбоя системы во время атаки. Направлю это письмо в техподдержку, пусть занимаются своей работой.'

            I '(думает) Молодец, Игорь, ничего лучше придумать не смог. Давид может точно что-то заподозрить.'

            I 'Ладно, я сохраню логи произошедшего сегодня домой, может, смогу ещё что-нибудь узнать.'

            D 'Да, я тоже. Хорошего вечера.'

            $ rascazal = False

    stop ambient

    jump scene9

label scene9: # Дом

    show screen scene_num(9)

    scene apartment with fade

    pause 1

    scene pc with dissolve

    I 'Хм, мало что можно узнать из имеющихся логов. Узнал только то, что хакеров было несколько, но эта информация мне ничего не даёт, видимо, работали профессионалы.'

    I 'Надо ещё раз проанализировать самое начало.'

    I 'Оставили, свою символику. Думают, что смогут всегда прятаться. Уверенности им не занимать, ещё бы чуть-чуть и мы бы их полностью вычислили.'

    scene black with fade

    pause 2.0

    jump scene10

label scene10: # Увольнение*

    play ambient 'audio/effects/office.mp3' fadein 2.0 volume 0.1

    show screen scene_num(10)

    scene office_cor with fade
    
    if rascazal:

        I '(думает) Никогда ещё не начинал свой день с такой напряжённой атмосферы в отделе.'

        I 'Доброе утро, Виктор Павлович.'

        VP 'Недоброе, ты уволен, собирай свои вещи и выметайся.'

        I 'Что?! Из-за чего? За последние полгода никаких сбоёв в системе. Вчера была кибер-атака, но я смог и её остановить, злоумышленники ничего не смогли сделать.'

        I 'Пожалуйста, Виктор Павлович. Я вас умоляю, мне нужна эта работы… Не для себя, для семьи.'

        VP 'Знаю, Игорь, но таковы правило. У тебя 15 минут, чтобы освободить рабочее место.'
    
    else:
        I '(думает) Странно, Давид так ещё не опаздывал, надеюсь, он сегодня придёт. Надо с ним связаться.'

        play sound 'audio/effects/zvonok.mp3' volume 0.5 noloop

        tel 'Звонок Давиду'

        I 'Придётся прикрыть его и сделать работу за него.'

        I 'Странный сегодня день. Наверное, я заработался, лучше уйду сегодня пораньше.'

    stop ambient fadeout 1.0
    
    jump scene11

label scene11: # Дом сгорел...

    play ambient 'audio/effects/ylica.mp3' fadein 2.0 volume 0.1

    show screen scene_num(11)

    scene dark_street with fade

    I 'Надо срочно связаться с Давидом.'

    I 'Надеюсь, он в порядке. Обычно он предупреждает, если не приходит на работу.'

    play sound 'audio/effects/zvonok.mp3' volume 0.5 noloop

    tel 'Звонок'

    I 'Ало.'

    nei 'Это Лавров Игорь Олегович, проживаете по адресу *****?'

    I 'Да.'

    nei 'Вынуждены сообщить, что в вашей квартире произошёл пожар, никаких вещей спасти не удалось. Сможете-ли вы подойти к адресу **** и подписать протокол?'

    I 'Да… конечно'

    tel 'Звонок завершён'

    I 'Отлично, просто супер! Хороший сегодня день!'

    I 'Мне срочно нужно немного снять напряжение, иначе к вечеру сойду с ума.'

    jump scene12

label scene12: # Бар
    
    show screen scene_num(12)

    scene bar with fade

    I '(думает) Единственное место поблизости, где можно расслабится и собраться с мыслями.'

    stop ambient fadeout 2.0

    # scene ,/,/

    I 'Бармен, колу.'

    I '(думает) Фух… И вправду расслабляет.'

    I 'Нужно решить что делать дальше. У меня нет дома, нет работы и нет денег. Самое важное: найти место, где я смогу переночевать. А Давид, как назло, не отвечает на звонки.'

    I 'Хм, знакомая символика… Где я видел эту эмблему???'

    I 'Точно! В логах хакерской атаки был этот знак.'

    I 'Я должен проследить за ним'

    I 'Вот 500 рублей, сдачи не надо.'

    jump scene13

label scene13: # Преследование

    show screen scene_num(13)

    play ambient 'audio/effects/ylica.mp3' fadein 2.0 volume 0.02

    scene logovo_outside with fade

    I '(думает) Куда же он направляется?'

    I 'Либо это его дом, либо его логово.'

    I 'В любом случае, я должен туда пробраться и узнать информацию.'

    I 'Нужно осмотреть здание и пробраться туда.'

    I 'Хм, есть три способа проникнуть внутрь.'

    jump scene14

label scene14: # Врыв

    show screen scene_num(14)

    scene logovo_outside

    stop ambient fadeout 1.0

    menu:
        I ''
        'Ворваться через главную дверь':

            scene door_hacers
            
            I 'Дверь выглядит ненадёжно, думаю, я смогу ворваться.'

            play sound 'audio/effects/door_sound.ogg' noloop

            scene logovo with dissolve

            I 'ВСЕМ СТОЯТЬ! СЮДА УЖЕ ЕДЕТ ПОЛИЦИЯ!'

            nei 'А вот и он. А полицией мог и не пугать, мы же видели, что ты никому не звонил.'

            nei 'Я заставлю его починить дверь обратно.'

        'Пролезть через вентиляцию':

            I 'Хм, вентиляция плохо закреплена, кажется, я смогу пролезть через неё.'
            
            scene vent with fade 

            play sound 'audio/effects/vent_sound.ogg' noloop

            nei 'Ну и где он?'

            nei 'Не знаю, я точно видела, что он шёл за мной. На камерах его тоже не видно?'

            nei 'Он пошёл за дом, но с другой стороны он не вышел.'

            I 'Видимо, я прямо над ними.'

            play sound 'audio/effects/padenie.ogg' noloop

            scene logovo with fade

            nei 'О ГОСПОДИ!'

            nei 'Фух, это он. Как-то смог пробраться через вентиляцию и сломал её.'

            nei 'То есть мы этого гения ждали?'

            nei 'Чёрт, теперь вентиляцию чинить.'

        'Перелезть через окно':

            I 'Они плохо закрыли окно. Я могу незаметно проникнуть к ним внутрь.'

            nei 'Всё идёт по плану. Он пролез внутрь.'

            nei 'Отлично, скоро он к нам придёт.'

            I 'Это точно их логово.'

            scene logovo with dissolve

            nei 'Добро пожаловать, Игорь!'
    
    jump scene15

label scene15: # Знакомство (Концовка 1)

    show screen scene_num(15)

    scene logovo

    I 'Вы заманили меня? Откуда вы знаете моё имя?'

    nei 'Позволь нам представиться, мы “Спектрум” и именно мы устроили атаку на “КиберЛок”.'

    O 'Я Ольга, глава нашей команды. Это Александр, он наши мозги, знает все способы проникновения в любую систему. А это Михаил, самые быстрые руки в Кибербурге, пишет более 100 строк кода в минуту.'

    I 'Ага, очень рад знакомству, теперь точно вызываю полицию.'

    Al 'Не сможешь, твой телефон уже взломан. А я думал Ольга нашла специалиста в безопасности.'

    O 'Да, он мастер в этой области.'

    O 'Вообщем, Игорь, мы хотим остановить “КиберЛок” за их “бизнес”, мы оставили для тебя файл во время атаки, чтоб ты тоже знал. И я предлагаю тебе присоединиться к нам для совместной борьбы, нам очень нужен такой человек как ты.'

    O 'Они забрали твою работу, забрали твой дом. Почему бы тебе не помочь нам остановить их?'

    # menu:
    #     I ''
    #     'Присоединиться к “Спектрум”':
            # I 'Да, я помогу вам. “КиберЛок” должен прекратить существование.'

        # 'Работать в одиночку':
        #     I 'Нет я работаю один.'

        #     aut 'Игорь пропал безвести'
            
        #     pause
            
        #     return

    jump scene16

label scene16: # Общение с командой

    show screen scene_num(16)

    scene logovo

    I 'Ладно, я решил. Я помогу вам остановить “КиберЛок”, но после я вас покину.'

    O 'Хорошо, я понимаю. У нас уже готов план и успех этой миссии зависит от тебя.'

    I 'Что мне нужно сделать?'

    O 'У нас есть флешка с вирусом “Аврора”, которая очистит сервера “КиберЛок”. Мы сделали для тебя фальшивый пропуск, который поможет тебе пробраться в серверную.'

    O 'Как только флешка сработает, мы запустим в эфир компромат, который уже готов, в сеть. “КиберЛок” будет полностью уничтожен.'

    O 'Звучит легко, но стоит понимать, что второго шанса у нас не будет.'

    M 'Вот флешка с вирусом, не потеряй.'

    I 'Понял, я не подведу. “Киберлок” заплатит за всё.'

    O 'Пока можешь отдохнуть и подготовиться к миссии.'

    $ flag1 = True
    $ flag2 = True
    $ choices = ['Поговорить с Михаилом', 'Поговорить с Александром']
    while flag1:
        menu:
            I ''
            'Пообщаться с командой':
                $ flag3 = True
                while choices[0] != 'Поговорил' or choices[1] != 'Поговорил' and flag3:
                    menu:
                        I ''
                        '[choices[0]]':
                            if choices[0] != 'Поговорил':
                                I 'Приятно познакомиться, я Игорь.'

                                M 'Да, я знаю.'

                                I 'Чем ты занимаешься в команде?'

                                M 'Ищу способы проникновения в систему и говорю что делать Саше.'

                                I 'Понял. Ты давно состоишь в “Спектрум”? И по какой причине?'

                                M 'Основали команду Саша и Ольга, вроде, с ними был ещё один человек, но он ушёл. Вскоре к ним присоединился я. Они нашли меня и предложили мне помогать людям, я согласился.'

                                M 'Мы не злая хакерская группировка. Мы взламываем только тех, кто это заслуживает. Например, “КиберЛок”.'

                                M 'Извини, но мне нужно работать дальше.'

                                I 'Понял, спасибо'

                                $ choices[0] = 'Поговорил'

                        '[choices[1]]':
                            if choices[1] != 'Поговорил':
                                I 'Привет, Александр, правда взломал мой телефон?'

                                Al 'Не бойся, Ольга уже позаботилась о том, что твой телефон теперь в безопасности.'

                                I 'Понял... Ты давно в этой команде?'

                                Al 'Да, я с Ольгой основал “Спектрум”'

                                I 'И с какой целью?'

                                Al 'Мы хотели заработать денег.'

                                Al 'И что за допрос? Хватит отвлекать меня от работы.'

                                $ choices[1] = 'Поговорил'

                        'Назад':
                            $ flag3 = False
                
                pass

            'Изучить вирус':
                if flag2:
                    I '(думает) Интересно как работает этот вирус. Проверю их мастерство.'

                    I 'Доступ зашифрован, неплохо, но я смогу получить доступ.'

                    $ flag = True
                    while flag:
                        $ miniGame1 = HakingGame(80, 8)
                        call screen miniGame(game = miniGame1)
                        $ miniGame1 = None

                        if _return:
                            I 'Хорошо получилось'
                            $ flag = False
                        else:
                            I 'Не получилось'

                    I 'И-и-и… Готово! Ну посмотрим что тут.'

                    I 'Интересно. Следуя коду, сначала данные с серверов не удаляются полностью, а большинство данных уходят к “Спектрум”.'

                    I 'Зачем им эти данные? Я могу попробовать исправить код, чтобы данные удалялись полностью.'

                    menu:
                        I ''
                        'Исправить вирус':
                            I 'Принцип работы вируса я понял. Исправить будет не сложно.'

                            $ flag = True
                            while flag:
                                $ miniGame1 = HakingGame(60, 8)
                                call screen miniGame(game = miniGame1)
                                $ miniGame1 = None

                                if _return:
                                    I 'Хорошо получилось'
                                    $ flag = False
                                else:
                                    I 'Не получилось'
                            
                            I 'Отлично, теперь когда вирус активируется, то абсолютно все данные исчезнут, включая данные про меня.'

                            $ Vzlomal = True
                        'Оставить как есть':
                            I 'Ладно, у меня нет сил на этот вирус. Мне нужно отдохнуть.'
                            $ Vzlomal = False

                    $ flag2 = False
                
                pass

            'Лечь спать':
                I 'Я слишком вымотался. Мне нужно передохнуть.'
                $ flag1 = False
    
    scene black with fade

    jump scene18

label scene18: # Сон

    show screen scene_num(18)

    play ambient 'audio/effects/office.mp3' fadein 2.0 volume 0.1 

    pause 2

    D 'Игорь… Просыпайся.'

    D 'Игорь!'

    scene main_office with fade

    show david with dissolve

    I 'А? Что?'

    D 'Эх, Игорь, нехорошо спать на рабочем месте.'

    I 'Ой, извини, не заметил, как задремал.'

    D 'Ничего, ты за последние дни много работал и не зря. Я только что был у начальства, он сказал, что повышает нас.'

    D 'Поздравляю, Игорь! С завтрашнего дня ты глава отдела, а я твой помощник!'

    I 'Ты серьёзно?! Это здорово!'

    D 'Даже больше, чем здорово. Нам нужно это отметить. Пойдём сегодня ко мне, моя сестрёнка приготовит нам шикарный ужин.'

    I 'Она здорова?!'

    D 'Ну да, она и не болела. Мы же недавно все вместе собирались.'

    I 'Супер, тогда после работы идём праздновать.'

    D 'Да, рабочий день как раз подходит к концу.'

    D 'Я жду тебя, Игорь.'

    hide david with dissolve

    scene black with fade

    stop ambient fadeout 0.5

    jump scene19

label scene19: # Планирование

    show screen scene_num(19)

    pause 2

    scene logovo with fade

    O 'Игорь… Просыпайся'

    I 'Так это был сон…'

    O 'Надеюсь, ты набрался сил. Сегодня важный день.'

    O 'Давай ещё раз пройдёмся по плану.'

    O 'Итак, шаг первый:'

    menu:
        I ''
        'Пробраться в “КиберЛок”':
            O 'Верно, ты должен  пробраться в “КиберЛок” по фальшивому пропуску.'
        
        'Добраться до дома':
            O 'Что? “КиберЛок” уничтожила твой дом. Ты должен будешь добраться до их офиса и проникнуть внутрь по фальшивому пропуску, который мы сделали для тебя.'
        
    O 'На втором шаге ты должен:'

    menu:
        I ''
        'Найти директоров “Киберлока”':
            O 'Нет. Ими займётся полиция, после успеха нашей миссии. Для этого ты должен будешь найти и пробраться в серверную'
        
        'Найти и пробраться в серверную':
            O 'Верно, ты много времени работал в “КиберЛок”. Ты ориентируешься в здании лучше, чем любой из нас.'
        
    O 'И после этого:'

    menu:
        I ''
        'Загрузить вирус “Аврора”':
            O 'Именно так. Флешка с “Авророй” уже у тебя. Тебе нужно будешь всего-лишь загрузить вирус в сервера.'
        
        'Сломать сервера вручную':
            O 'ломать сервера руками не стоит. Тебе нужно будешь всего-лишь загрузить вирус в сервера.'
        
    O 'После чего мы начнём транслировать уже готовый компромат на “КиберЛок” и им настанет конец.'

    O 'Ты же умеешь водить машину? Мы как раз приготовили одну для тебя, она на заднем дворе.'

    O 'Там в бардачке лежит твой новый пропуск, наушник для связи и транквилизаторный пистолет, прихвати его. Может пригодиться, если что-то пойдёт не так.'

    I 'Понял, за дело.'

    M 'Мы верим в тебя, Игорь!'

    Al 'Только не облажайся, второго шанса не будет.'

    I 'Я не подведу.'

    O 'Не забудь взять свой ноутбук.'
    
    jump scene20

label scene20: # Поиск серверной

    show screen scene_num(20)

    scene enter_kyberlok with fade

    pause 0.5

    scene office_cor with dissolve

    I 'Я внутри.'

    I 'Нужно вспомнить, где находится серверная'

    $ choices = ['Проверить в правом крыле', 'Проверить в левом крыле']
    while choices[0] != 'Проверил' or choices[1] != 'Проверил':
        menu:
            I ''
            '[choices[0]]':
                if choices[0] != 'Проверил':
                    I 'Вроде, комнаты по типу серверной должны находиться в правом крыле, сначала нужно проверить там.'

                    I 'Увы, но серверной там нет. Видимо, она в другом крыле.'
                    
                    $ choices[0] = 'Проверил'

            '[choices[1]]':
                if choices[1] != 'Проверил':
                    I 'Вероятность мала, но серверная может быть там. Нужно осмотреть все комнаты.'

                    I 'В левом крыле из интересного только столовая.'
        
                    $ choices[1] = 'Проверил'

    I 'Как я мог забыть.'

    I 'У “КиберЛок” же есть свой навигатор, чтоб лучше ориентироваться.'

    I 'И серверная находится этажом выше.'

    jump scene21

label scene21: # Серверная

    show screen scene_num(21)

    play ambient 'audio/effects/server.mp3' fadein 0.5 volume 0.1

    scene server_room with fade

    pause 0.5

    scene main_server with dissolve

    I 'Приём, я в серверной.'

    Al 'Отлично, мы уже готовы запускать компромат. Но сначала ты активируй “Аврору”.'

    I 'Это займёт некоторое время. Сервера закрыты паролем. Просто дайте мне время расшифровать пароль.'
    $ flag = True
    while flag:
        stop ambient
        $ miniGame1 = HakingGame(40, 8)
        call screen miniGame(game = miniGame1)
        $ miniGame1 = None

        play ambient 'audio/effects/server.mp3' fadein 0.5 volume 0.1

        if _return:
            I 'Хорошо получилось'
            $ flag = False
        else:
            I 'Не получилось'

            I 'Надо ещё раз'

    
    
    I 'Готово, я запускаю “Аврору”.'

    D 'Остановись, Игорь!'

    scene server_room with dissolve

    show david

    I 'Давид, что происходит?'

    D 'Игорь, я уговорил Главный Совет оставить тебя в живых и забыть о тебе. Ты мог найти новую работу, жить дальше в своей шикарной квартире, но ты всё равно лезешь в дела компании.'

    I 'Что? Что ты говоришь? Я не верю, что ты заодно с ними.'

    D 'Я даю тебе последний шанс, уничтожь флешку и расскажи о хакерах. Тогда мы позволим тебе исчезнуть из города. В противном случае я буду вынужден тебя устранить.'

    I 'Ты был мне братом, Давид. Почему ты решил связаться с ними?'

    D 'Всё ради Софии. Её лечение слишком дорого мне обходится. Все деньги уходят на лекарства и обследования. Они предложили мне работать на них за большую стоимость. Я не могу отказаться.'

    D 'Я не жду, что ты простишь меня… Но постарайся понять.'

    D 'Я неплохой человек, мне просто не повезло.'

    I 'Давид… Останься со мной. Вместе мы остановим “КиберЛок”.'

    D 'Я не могу оставить свою сестру без лечения, при всём желании помочь тебе.'

    I 'Я обещаю, мы найдём средства на помощь Софии.'

    D 'Ты должен остановиться.'

    D 'Ты думаешь твой вирус их остановит? Думаешь они не найдут тебя и не убьют? Да даже если их посадят, через неделю они уже будут на свободе.'

    menu:
        I ''
        'Активировать вирус "Аврора"':
            I 'Мне очень жаль, Давид.'

            I 'Но я не могу сдаться.'

            I '“Аврора” активирована.'

            O 'Да, Игорь! Мы в тебе не сомневались, компромат загружен в сеть!'

            D 'Что ты наделал, Игорь?!'

            D 'Извини… Но я должен…'

            D '… нет, я не могу'
            
            hide david

            play sound 'audio/effects/shumnyiy-odinochnyiy-vyistrel.ogg' volume 0.8 noloop

            queue sound 'audio/effects/shumnyiy-odinochnyiy-vyistrel.ogg' volume 0.8 noloop

            I 'Нет. ДАВИД!'

            VP 'Я знал, что от тебя мало толку, Давид.'

            I 'Я УБЬЮ ТЕБЯ!'

            if Vzlomal:

                pause 0.5

                play sound 'audio/effects/shumnyiy-odinochnyiy-vyistrel.ogg' volume 0.8 noloop

                queue sound 'audio/effects/pistolet-s-glushitelem.ogg' volume 1.3 noloop

                I 'А-р-г-х, чёрт… я ранен.'

                I 'Зато я в него тоже попал.'

                I 'Мне нужно срочно уезжать.'

                I 'Прощай, Давид, я позабочусь о твоей сестре.'

                I 'Главное… не потерять много крови…'

                I 'В глазах темнеет… голова кружится…'
                stop ambient fadeout 0.5

                jump scene22_1_1

            else:

                pause 0.

                play sound 'audio/effects/pistolet-s-glushitelem.ogg' noloop

                I 'За Давида.'

                I 'Я обязательно доберусь до тебя. Без разницы где ты будешь, в тюрьме или на воле.'

                I 'Вирус загружен, мне нужно срочно уходить, пока тут не появились ещё люди.'

                I 'Прощай, Давид, я позабочусь о твоей сестре.'

                stop ambient fadeout 0.5

                jump scene22_1_2

        'Уничтожить вирус “Аврора”':
            I 'Давид… Я так не могу.'

            I 'Я не могу пойти против тебя.'

            O 'Нет! Нет...'

            D 'Я понимаю, Игорь. Как бы мне не хотелось помочь тебе, я не могу. Ты знаешь, София моя единственная семья и я не переживу, если и она покинет меня.'

            D 'Мне жаль, но ты должен покинуть этот город, ради твоей же безопасности. Прямо сейчас, начни новую жизнь в другом городе и забудь про “КиберЛок”.'

            D 'Прощай, Игорь.'

            I 'Прощай, старый друг.'

            I 'Я уверен, мы ещё встретимся.'

            D 'Буду надеяться.'
            stop ambient fadeout 0.5

            jump scene22_2

    stop ambient fadeout 0.5

    jump scene22_1_1

label scene22_1_1:

    scene office_cor with fade

    pause 0.5

    scene menu_bg2 with fade

    O 'Не бойся, Игорь. Тебя никто не будет вспоминать. Но мы должны выразить тебе большую благодарность. Ты помог нам разбогатеть.'

    Al 'Вирус переслал все нужные файлы нам. Теперь мы будем контролировать всех, ведь у “КиберЛок” были данные про всех политиков, про каждого человека в этом городе.'

    I 'Вы думаете, что я настолько наивный? Что я буду доверять каждому встречному?'

    I 'Проверьте входящие файлы.'

    I 'Я изменил вирус.'

    play music 'audio/effects/1con-music.ogg'

    I '…'

    I 'Я прожил неплохую жизнь. Остановил злодейскую корпорацию, остановил злых хакеров.'

    window hide

    $ quick_menu = False

    pause 2

    call screen con

    stop music fadeout 1.0

    scene black

    pause 1

    return

label scene22_1_2:

    scene office_cor with fade

    O 'Хорошая работа, Игорь.'

    O 'Не думала, что ты настолько наивный. Теперь “КиберЛок” больше нет и мы займём их место. А всё благодаря тебе.'

    I 'Так вы соврали…'

    I 'Я не оставлю это безнаказанным.'

    scene menu_bg2 with fade

    I 'Осталось ещё одно дело.'

    I 'Всё время меня кто-то использовал…'

    I 'Сначала “КиберЛок”, потом “Спектрум”'

    play music 'audio/effects/2con-music.ogg'

    I '...'

    I 'Я всего-лишь мечтал сделать мир лучше хорошими поступками.'

    I 'Но этот мир слишком несправедлив. Каждый, кто получает власть в этом городе использует её в свою пользу'

    I 'И я не могу оставить это безнаказанным.'

    I 'Я больше не Игорь, отныне я их ночной кошмар и я доберусь до каждого, кто угрожает безопасности в этом городе.'

    window hide

    $ quick_menu = False

    pause 2

    call screen con

    stop music fadeout 1.0

    scene black

    pause 1

    return

label scene22_2:

    scene office_cor with fade

    I 'Ало.'

    S 'Это Игорь?'

    I 'Да.'

    I 'Погоди. София?! Я очень рад тебя слышать! Как ты? Ты уже выздоровела?'

    S 'Со мной всё хорошо, я тоже очень рада вновь услышать тебя… Но…'

    S 'Давид пропал… никто не видел его уже несколько дней.'

    I 'Что? Но он не мог оставить тебя'

    S 'Я узнала об этом сразу, как меня выписали. Я побежала к нему домой, но когда я зашла… В квартире был хаос.'

    S 'Всё было перевёрнуто. В его квартире как будто что-то искали. А в другой комнате следы драки.'

    S 'Среди разбросанной бумаги я нашла записку от Давида.'

    play music 'audio/effects/1con-music.ogg' fadein 1.0

    S  '“Если кто-то это читает, то вы должны узнать. В этой жизни я был не лучшим человеком, я не был оптимистом, не пытался сделать мир лучше… пока не познакомился со своим лучшим другом.'

    S 'Но всё равно последнее время я занимался ужасными вещами, у меня не было другого выбора. Я занимался грязными делами, работая на “КиберЛок”, но спустя время я осознал…'

    S 'я понял, что этот ужас не должен продолжаться вечно. Увы, я понял это слишком поздно, но всё равно попытался остановить “КиберЛок” в одиночку.'

    S 'Мне кажется, они уже всё поняли в ближайшее время меня попытаются убрать, как это было с другими…'

    S 'Пожалуйста, Игорь, если ты это читаешь, позаботься о Софии. И прощай. ”'

    S '...'

    window hide

    $ quick_menu = False

    pause 2

    call screen con

    stop music fadeout 1.0

    scene black

    pause 1

    return






                










