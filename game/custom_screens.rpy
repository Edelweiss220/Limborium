label splashscreen:

    #scene black
    #show Solid("#282d30")

    $ renpy.movie_cutscene("videos/studio_logo2.webm")

#    pause 1.0

    return


#screen example():
#    text "Пример экрана"
image gameMenu = "images/gameMenu.png"
init python:
    trait_descriptions = {
        "SELF": "Ты ставишь свои границы превыше всего.",
        "MEANING": "Ты пытаешься найти логику даже в хаосе.",
        "ESCAPE": "Ты всё чаще ищешь не решение, а выход из ситуации."
    }


# Функция определния отпечатка

    def get_imprint(self, meaning, escape):
        if self >= 3 and meaning >= 3 and escape <= 4:
            return "Собирающая себя"
        elif self >= 3 and escape >= 5:
            return "Противоречивая"
        elif self <= -2 and meaning < 3:
            return "Растворяющаяся"
        elif escape >= 5 and self < 3:
            return "Бегущая от жизни"
        elif meaning >= 3 and self >= 2 and escape <= 4:
            return "Наблюдающая"
        elif meaning >= 3 and self < 3 and escape < 5:
            return "Ищущая смысл"
        elif self >= 3:
            return "Сопротивляющаяся"
        else:
            return "Неопределившаяся"

# Функция подбора контента для отпечатка
    imprint_data = {
    "Бегущая от жизни": {
        "image": "imprints/runningAway.png",
        "whatMonsterFeels": "Убегающий Безлик",
        "whatMonsterIs": 
            "Существо, которое появляется там, где человек больше всего хочет исчезнуть. "
            "Оно предлагает дорогу прочь, но постепенно стирает желание вернуться.",

        "whatNikolFeel":
            "Усталость, тревогу, желание исчезнуть из ситуации.",

        "whatDoesItMean":
            "Уход кажется спасением от боли.",

        "whatKaelSays":
            "Иногда уйти действительно нужно. "
            "Но не принимай бегство за решение. "
            "Сначала пойми, от чего именно ты хочешь уйти.",
        "secondLayerImprint": "Я слишком хорошо научилась уходить от того, чего боюсь, чтобы признаться себе, что иногда бегу даже от того, чего хочу.",
        "secondLayerMonster": "Похоже, Лимбориум уже почувствовал, как сильно мне хочется исчезнуть, и знает, что предложить мне самый лёгкий путь.",
    },


    "Сопротивляющаяся": {
        "image": "imprints/resisting.png",
        "whatMonsterFeels": "Краг",
        "whatMonsterIs":
            "Существо, которое питается сопротивлением "
            "и превращает любую ситуацию в конфликт.",

        "whatNikolFeel":
            "Злость, напряжение, желание отстоять себя.",

        "whatDoesItMean":
            "Николь перестаёт позволять другим решать за неё, "
            "но рискует превратить всё вокруг в борьбу.",

        "whatKaelSays":
            "Уметь сказать «нет» — хорошо. "
            "Только не превращай каждую дверь в стену. "
            "Иногда сильнее тот, кто знает, где стоит остановиться.",
        "secondLayerImprint": "Я научилась защищать себя, но иногда уже не понимаю, от чего именно защищаюсь — от других или от собственного страха снова уступить.",
        "secondLayerMonster": "Моё сопротивление словно зовёт тех, кто превращает любую попытку защититься в ещё одну борьбу.",
    },


    "Ищущая смысл": {
        "image": "imprints/searchingForMeaning.png",
        "whatMonsterFeels": "Эллиар",
        "whatMonsterIs":
            "Существо, которое даёт ответы, "
            "но каждый ответ порождает новый вопрос.",

        "whatNikolFeel":
            "Растерянность, любопытство, тревога "
            "и потребность понять происходящее.",

        "whatDoesItMean":
            "Понимание становится для Николь способом "
            "вернуть контроль.",

        "whatKaelSays":
            "Не всякий вопрос требует немедленного ответа. "
            "Иногда достаточно продолжать идти. "
            "Главное — не переставай спрашивать себя, зачем ты идёшь.",
        "secondLayerImprint": "Мне кажется, что если я найду правильный ответ, всё наконец встанет на свои места. Но чем больше я понимаю, тем больше вопросов появляется.",
        "secondLayerMonster": "Кажется, здесь уже заметили, насколько сильно мне нужны ответы, и готовы давать их один за другим — лишь бы я продолжала спрашивать.",
    },


    "Наблюдающая": {
        "image": "imprints/observer.png",
        "whatMonsterFeels": "Моррак",
        "whatMonsterIs":
            "Тварь искажений и наблюдения. "
            "Она меняет детали пространства, пока человек сам "
            "не перестаёт доверять собственным глазам.",

        "whatNikolFeel":
            "Осторожность, напряжение, внимательность.",

        "whatDoesItMean":
            "Она начинает доверять собственным наблюдениям "
            "больше, чем чужим словам.",

        "whatKaelSays":
            "Смотреть — полезно. Замечать — ещё полезнее. "
            "Только помни: однажды наблюдение заканчивается, "
            "и тебе всё равно придётся выбирать.",
        "secondLayerImprint": "Я стала замечать гораздо больше, чем раньше, но иногда думаю, не мешает ли мне это просто сделать шаг и довериться собственному выбору.",
        "secondLayerMonster": "Чем внимательнее я смотрю на этот мир, тем сильнее он будто начинает смотреть в ответ.",
    },


    "Растворяющаяся": {
        "image": "imprints/dissolving.png",
        "whatMonsterFeels": "Шепчущий",
        "whatMonsterIs":
            "Существо без собственного голоса. "
            "Оно собирает чужие слова и возвращает их человеку "
            "так, чтобы они стали похожи на его собственные мысли.",

        "whatNikolFeel":
            "Стыд, неуверенность, бессилие; "
            "чужие голоса становятся убедительнее собственного.",

        "whatDoesItMean":
            "Чужое мнение начинает подменять "
            "её собственное представление о себе.",

        "whatKaelSays":
            "Чужой голос может звучать очень убедительно. "
            "Но если ты слишком долго слушаешь других, "
            "однажды можешь забыть, как звучишь сама.",
        "secondLayerImprint": "Иногда мне кажется, что я становлюсь тише с каждым днём, будто постепенно исчезаю среди чужих ожиданий и собственных сомнений.",
        "secondLayerMonster": "Здесь уже есть кто-то, кто умеет говорить моим голосом, и страшнее всего то, что иногда я не сразу понимаю разницу.",
    },


    "Собирающая себя": {
        "image": "imprints/reassembling.png",
        "whatMonsterFeels": "Ворн",
        "whatMonsterIs":
            "Хищник, который пытается найти трещину "
            "в только что возникшей внутренней опоре.",

        "whatNikolFeel":
            "Осторожная уверенность, облегчение и надежда; "
            "одновременно боль от прошлого.",

        "whatDoesItMean":
            "Она начинает понимать, что несовершенство "
            "не делает её ничтожной.",

        "whatKaelSays":
            "Тебе не обязательно быть лучше всех. "
            "Тебе нужно знать, кто ты, когда рядом никого нет. "
            "Не отдавай другим право решать это за тебя.",
        "secondLayerImprint": "Я всё ещё чувствую трещины внутри себя, но впервые начинаю понимать, что их наличие не означает, что я сломана.",
        "secondLayerMonster": "Моя внутренняя опора ещё слишком новая, и кажется, этот мир уже ищет место, где её можно сломать.",
    },


    "Противоречивая": {
        "image": "imprints/contradictory.png",
        "whatMonsterFeels": "Двуликий",
        "whatMonsterIs":
            "Существо с двумя несовместимыми проявлениями. "
            "Оно постоянно заставляет человека выбирать "
            "между противоположными желаниями.",

        "whatNikolFeel":
            "Одновременно злость, сила, усталость "
            "и желание сбежать.",

        "whatDoesItMean":
            "Она хочет изменить свою жизнь, "
            "но пока не знает, куда направить свою силу.",

        "whatKaelSays":
            "Ты уже научилась говорить «нет». "
            "Теперь попробуй понять, чему ты хочешь сказать «да». "
            "Иногда направление важнее силы.",
        "secondLayerImprint": "Я научилась говорить «нет», но пока не понимаю, чему именно я хочу сказать «да».",
        "secondLayerMonster": "Похоже, Лимбориум почувствовал, как внутри меня сталкиваются два разных желания, и теперь хочет заставить меня выбрать одно из них.",
    },


    "Неопределившаяся": {
        "image": "imprints/undefined.png",
        "whatMonsterFeels": "Масочник",
        "whatMonsterIs":
            "Существо, которое каждый раз принимает другую форму "
            "в зависимости от того, кем человек боится "
            "или хочет стать.",

        "whatNikolFeel":
            "Смешанные чувства, тревога и надежда; "
            "она ещё не знает, как реагировать на мир.",

        "whatDoesItMean":
            "Ни одна стратегия пока не стала главной — "
            "личность ещё формируется.",

        "whatKaelSays":
            "Не знать, куда идти, — нормально. "
            "Плохо только продолжать идти чужой дорогой. "
            "Иногда первый выбор — решить, "
            "что выбирать будешь ты сама.",
        "secondLayerImprint": "Я пока не знаю, кем хочу стать. Наверное, впервые мне придётся не найти готовый ответ, а самой решить, каким он будет.",
        "secondLayerMonster": "Я ещё сама не знаю, кем становлюсь, а этот мир уже словно примеряет на меня разные лица, пытаясь решить за меня.",
    }
}

# вызов функуий
#$ imprint = get_imprint(p_SELF, p_MEANING, p_ESCAPE)
#$ imprint_info = imprint_data[imprint]


init:
    style centered_text is default:
        xalign 0.5
        yalign 0.5

screen intParameters():
    vbox:
        xysize(200,200)
        box_wrap True #перенос объектов в новый столбец
        align (0.01,0.01)
        spacing 1 #расстояние между объектами
        
        #style param_style = Style(style.default)
        #param_style.outlines = [(2, "#220000")]  # тонкая тёмная обводка
        
        
        text "Self [p_SELF]" color "#ffffff"
        text "Meaning [p_MEANING]" color "#ffffff"
        text "Escape [p_ESCAPE]" color "#ffffff"
        
'''screen separateScreen():
    $ imprint = get_imprint(p_SELF, p_MEANING, p_ESCAPE)
    $ imprint_info = imprint_data[imprint]
    key "y" action ToggleScreen("separateScreen")
    zorder 100
    modal True
    add Solid("#000000")
    
    add imprint_info["image"]:
        xpos 40
        ypos 40
        xsize 300
        ysize 300
    
    
    grid 1 4:
        xfill True
        yfill True
        spacing 2
        
        # Блок 1: Внутреннее состояние
        frame:
            background "#000000"
            xalign 0.5
            yalign 0.5
            vbox:
                xalign 0.5
                spacing 50
                text _("============================") color "#ffffff"
                text _("Отпечаток:") color "#ffffff"
                text _("============================") color "#ffffff"
                #$ imprint = get_imprint(p_SELF, p_MEANING, p_ESCAPE)
                #$ imprint_info = imprint_data[imprint]
                text "[imprint]" color "#ffffff"
                text "[imprint_info['whatDoesItMean']]" color "#ffffff"
                grid 2 3:
                    xalign 0.5
                    spacing 20
                #hbox:

                    text _("SELF") color "#ffffff" xsize 50
                    bar value AnimatedValue(value=p_SELF, range=10, delay=1.0):
                        left_bar Solid("#777777")
                        right_bar Solid("#222222")
                        xsize 400
                    #text _("[p_SELF]") color "#ffffff"
                #hbox:
                    text _("MEANING") color "#ffffff"  xsize 50
                    bar value AnimatedValue(value=p_MEANING, range=10, delay=1.0):
                        left_bar Solid("#777777")
                        right_bar Solid("#222222")
                        xsize 400
                   # text _("[p_MEANING]") color "#ffffff"
                #hbox:
                    text _("ESCAPE") color "#ffffff"  xsize 50
                    bar value AnimatedValue(value=p_ESCAPE, range=10, delay=1.0):
                        left_bar Solid("#777777")
                        right_bar Solid("#222222")
                        xsize 400
                    #text _("[p_ESCAPE]") color "#ffffff"

        # Блок 1.2 : Что чувсвует николь
        frame:
            background "#000000"
            xalign 0.5
            yalign 0.5
            vbox:
                xalign 0.5
                text _("Что я чувствую:") color "#ffffff"
                text "[imprint_info['whatNikolFeel']]"

        # Блок 2: Текущее состояние
        frame:
            background "#000000"
            xalign 0.5
            yalign 0.5
            vbox:
                xalign 0.5
                text _("Тебя чувсвует моснтр: [imprint_info['whatMonsterFeels']]") color "#ffffff" 
                #text "[imprint_info['whatMonsterFeels']]"
                text "[imprint_info['whatMonsterIs']]"
                #$ stats = {"SELF": p_SELF, "MEANING": p_MEANING, "ESCAPE": p_ESCAPE}
                #$ dominant_trait = max(stats, key=stats.get)
                #$ desc = trait_descriptions[dominant_trait]
                #text "[dominant_trait]" #style "big_bold"
                #text "[desc]" #style "desc_text"
                  
        # Блок 3: Важное
        frame:
            background "#000000"
            xalign 0.5
            yalign 0.5
            vbox:
                xalign 0.5
                text _("Слова Каэля:") color "#ffffff"
                text "[imprint_info['whatKaelSays']]"
    
    
    
    #add Solid("#000000") xfill True yfill True
    #add "#000000"
    #text "Отпечаток:"
    #frame:
    #    xfill True
    #    yfill True
    #    background "#FFFFFF"
    #zorder 100
    #modal True
    #add Solid("#000000")
    #vbox:
    #    xfill True
    #    yfill False
    #    #xysize (1.0, 1.0)
    #    spacing 5
    #    frame:
    #        xfill True
    #        #yfill True
    #        #xysize (1.0, 0.3)
    #        #yexpand True
    #        background "#FF0000"
    #       
    ##       text _("Ваш первый отпечаток"):
    #           align (0.5, 0.5) 
    #            size 24
    #    frame:
    #        xfill True
    #        #yfill True
    #        #yexpand True
    #        #xysize (1.0, 0.3)
    #        background "#00FF00"
    #        text _("Ваш второй отпечаток"):
    #            align (0.5, 0.5) 
    #            size 24           
    #    frame:
    #        xfill True
    #        #yfill True
    #        #yexpand True
    #       #xysize (1.0, 0.3)
    #        background "#0000FF"
    #        text _("Ваш Третий отпечаток"): 
    #            align (0.5, 0.5) 
    #            size 24          
'''            
            
screen key_catcher():
    key "y" action Show("separateScreenV2")
    
    
    
    
screen separateScreenV2():
    #key "y" action Hide("separateScreenV2")
    #key "y" action [Hide("separateScreenV2"), Jump("prologue_end")]
    key "y" action Return()
    zorder 100
    modal True
    $ SW = config.screen_width
    $ SH = config.screen_height
    
    $ imprint = get_imprint(p_SELF, p_MEANING, p_ESCAPE)
    $ imprint_info = imprint_data[imprint]
    
    
    add "images/interface/separateScreenV2.png":
        xsize int(SW*1.2)
        ysize int(SH*1.2)
        xalign 0.5
        yalign 0.5

    add Solid("#00000055")
    
    #add Solid("#000000")
    # Левая колонка — 35%
    vbox:
        xpos int(SW * 0.03)
        ypos int(SH * 0.05)
        xsize int(SW * 0.32)
        
        spacing int(SH * 0.02)
        
        #text "ЛЕВАЯ КОЛОНКА":
        #    color "#ffffff"
        #    size int(SH * 0.025)
            
        text "ОТПЕЧАТОК":
            color "#ffffff"
            size int(SH * 0.022)
        
        add imprint_info["image"]:
            xsize int(SW * 0.25)
            ysize int(SW * 0.25)

        text "[imprint]":
            color "#ffffff"
            size int(SH * 0.028)

        text "[imprint_info['whatDoesItMean']]":
            color "#dddddd"
            size int(SH * 0.018)
            
            
    # Правая колонка — 55%
    vbox:
        xpos int(SW * 0.40)
        ypos int(SH * 0.05)
        xsize int(SW * 0.55)

        spacing int(SH * 0.02)

        text "ОСНОВНЫЕ ПОКАЗАТЕЛИ":
            color "#ffffff"
            size int(SH * 0.022)


        hbox:
            spacing int(SW * 0.015)

            text "SELF":
                color "#ffffff"
                size int(SH * 0.018)
                xsize int(SW * 0.08)

            bar value AnimatedValue(
                value=p_SELF,
                range=10,
                delay=1.0
            ):
                left_bar Solid("#777777")
                right_bar Solid("#222222")
                xsize int(SW * 0.30)
                ysize int(SH * 0.018)

            text "[p_SELF]":
                color "#ffffff"
                size int(SH * 0.018)


        hbox:
            spacing int(SW * 0.015)

            text "MEANING":
                color "#ffffff"
                size int(SH * 0.018)
                xsize int(SW * 0.08)

            bar value AnimatedValue(
                value=p_MEANING,
                range=10,
                delay=1.0
            ):
                left_bar Solid("#777777")
                right_bar Solid("#222222")
                xsize int(SW * 0.30)
                ysize int(SH * 0.018)

            text "[p_MEANING]":
                color "#ffffff"
                size int(SH * 0.018)


        hbox:
            spacing int(SW * 0.015)

            text "ESCAPE":
                color "#ffffff"
                size int(SH * 0.018)
                xsize int(SW * 0.08)

            bar value AnimatedValue(
                value=p_ESCAPE,
                range=10,
                delay=1.0
            ):
                left_bar Solid("#777777")
                right_bar Solid("#222222")
                xsize int(SW * 0.30)
                ysize int(SH * 0.018)

            text "[p_ESCAPE]":
                color "#ffffff"
                size int(SH * 0.018)
                
                
        # Второй слой 
        text "ВТОРОЙ СЛОЙ":
            color "#ffffff"
            size int(SH * 0.022)


        $ self_text = ""
        if p_SELF <= 2:
            $ self_text = "Я всё чаще сомневаюсь в том, чего хочу сама, и начинаю прислушиваться к чужим голосам."
        elif p_SELF <= 5:
            $ self_text = "Я всё ещё понимаю, чего хочу сама, но иногда начинаю сомневаться в собственных решениях."
        else:
            $ self_text = "Я всё чаще позволяю себе решать самой, даже если знаю, что другим это может не понравиться."


        
        
        $ meaning_text = ""

        if p_MEANING <= 2:
            $ meaning_text = "Иногда мне кажется, что всё это вообще не имеет смысла, и сколько бы я ни старалась, ничего не изменится."
        elif p_MEANING <= 5:
            $ meaning_text = "Я пытаюсь понять, почему всё происходит именно так, но пока у меня больше вопросов, чем ответов."
        else:
            $ meaning_text = "Мне всё важнее понять, зачем всё это происходит, потому что без ответа я будто теряю направление."


        
        $ escape_text = ""

        if p_ESCAPE <= 2:
            $ escape_text = "Даже когда мне страшно или больно, я всё чаще остаюсь лицом к тому, от чего раньше хотелось отвернуться."
        elif p_ESCAPE <= 5:
            $ escape_text = "Когда становится слишком тяжело, я уже думаю о том, чтобы уйти, но какая-то часть меня всё ещё пытается остаться."
        else:
            $ escape_text = "А когда становится совсем невыносимо, единственное, чего мне хочется, — исчезнуть и больше ничего не чувствовать."


        
        $ second_layer_text = (
            self_text + " " +
            meaning_text + " " +
            escape_text + " " +
            imprint_info['secondLayerImprint'] + " " +
            imprint_info['secondLayerMonster']
        )


        text "[second_layer_text]":
            color "#dddddd"
            size int(SH * 0.018)
            xsize int(SW * 0.50)
        
        
        
        
        
        
        
        # следующий блок
        text "ЧТО Я ЧУВСТВУЮ":
            color "#ffffff"
            size int(SH * 0.022)

        text "[imprint_info['whatNikolFeel']]":
            color "#dddddd"
            size int(SH * 0.018)
            xsize int(SW * 0.50)
            
        text "КТО МОЙ МОНСТР":
            color "#ffffff"
            size int(SH * 0.022)

        text "[imprint_info['whatMonsterFeels']]":
            color "#ffffff"
            size int(SH * 0.020)

        text "[imprint_info['whatMonsterIs']]":
            color "#dddddd"
            size int(SH * 0.018)
            xsize int(SW * 0.50)
        # блок про каэля
        text "СЛОВА КАЭЛЯ":
            color "#ffffff"
            size int(SH * 0.022)

        text "«[imprint_info['whatKaelSays']]»":
            color "#dddddd"
            size int(SH * 0.018)
            xsize int(SW * 0.50)        
            
            
            
# Сцена 1: Пролог.  Краски высохли    

screen prologue_intro():


    if prologue_video_started:
        add Transform(
        Movie(play="animations/school_intro.webm", loop=False),
        xpos=0,
        ypos=0,
        xsize=config.screen_width,
        ysize=config.screen_height,
        fit="cover"
        )
        
    if prologue_video_fade:
        add Solid("#000000") at prologue_video_fade_animation 
        
        
        
    if prologue_quote_visible:
        text "«Самые страшные голоса —\nте, что звучат твоим собственным голосом.»":
            align (0.5, 0.58)
            text_align 0.5
            size 38
            color "#FFFFFF"
            slow_cps 8
            at prologue_quote
        
    if prologue_title_visible:
        text "ЛИМБОРИУМ":
            align (0.5, 0.43)
            size 56
            color "#FFFFFF"
            at prologue_main_title
            
    if prologue_chapter_visible:
        text "П Р О Л О Г":
            align (0.5, 0.49)
            size 28
            color "#FFFFFF"
            at prologue_chapter
              
            
transform prologue_chapter:
    alpha 0.0
    linear 0.6 alpha 1.0
    pause 0.8
    linear 0.7 alpha 0.0            

transform prologue_main_title:
    alpha 0.0
    linear 0.8 alpha 1.0
    pause 1.0
    linear 0.8 alpha 0.0

transform prologue_quote:
    alpha 0.0
    linear 1.0 alpha 1.0
    pause 8
    linear 1.8 alpha 0.0

transform prologue_title_animation:
    alpha 0.0
    linear 0.8 alpha 1.0
    pause 4.2
    linear 1.0 alpha 0.0          
            
transform prologue_video_fade_animation:
    alpha 0.0
    linear 2.0 alpha 1.0           
            