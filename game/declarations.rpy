label run_declarations:
    ####################################
    # Images
    ####################################

    ###################
    # Character images
    ###################

    #Kosuke
    image kosuke angry = "images/characters/dummy.png"
    image kosuke confused = "images/characters/dummy.png"
    image kosuke blush = "images/characters/dummy.png"       
    image kosuke happy = "images/characters/dummy.png"
    image kosuke horrified = "images/characters/dummy.png"
    image kosuke innocent = "images/characters/dummy.png"
    image kosuke normal = "images/characters/dummy.png"
    image kosuke smirk = "images/characters/dummy.png"
    image kosuke surprised = "images/characters/dummy.png"
    image kosuke tired = "images/characters/dummy.png"
    image kosuke victory = "images/characters/dummy.png"
    image kosuke upset = "images/characters/dummy.png"

    image kosuke uniform angry = "images/characters/dummy.png"
    image kosuke uniform confused = "images/characters/dummy.png"
    image kosuke uniform blush = "images/characters/dummy.png"
    image kosuke uniform happy = "images/characters/dummy.png"
    image kosuke uniform jealous = "images/characters/dummy.png"
    image kosuke uniform puppyEyes = "images/characters/dummy.png"
    image kosuke uniform normal = "images/characters/dummy.png"
    image kosuke uniform salute = "images/characters/dummy.png"
    image kosuke uniform shocked = "images/characters/dummy.png"
    image kosuke uniform smirk = "images/characters/dummy.png"
    image kosuke uniform upset = "images/characters/dummy.png"

    #Misaki
    image misaki angry = "images/characters/dummy.png"
    image misaki annoyed = "images/characters/dummy.png"
    image misaki blush = "images/characters/dummy.png"
    image misaki yandere = "images/characters/dummy.png"
    image misaki happy = "images/characters/dummy.png"
    image misaki horrified = "images/characters/dummy.png"
    image misaki normal = "images/characters/dummy.png"
    image misaki smirk = "images/characters/dummy.png"
    image misaki upset = "images/characters/dummy.png"

    image misaki uniform angry = "images/characters/dummy.png"
    image misaki uniform blush = "images/characters/dummy.png"
    image misaki uniform embarrassed = "images/characters/dummy.png"
    image misaki uniform happy = "images/characters/dummy.png"
    image misaki uniform normal = "images/characters/dummy.png"
    image misaki uniform smirk = "images/characters/dummy.png"
    image misaki uniform upset = "images/characters/dummy.png"

    #Ms. Kasai
    image msKasai happy = "images/characters/dummy.png"
    image msKasai horrified = "images/characters/dummy.png"
    image msKasai normal = "images/characters/dummy.png"

    #Mr. Kasai
    image mrKasai happy = "images/characters/dummy.png"
    image mrKasai horrified = "images/characters/dummy.png"
    image mrKasai normal = "images/characters/dummy.png"

    #Riku
    image riku annoyed = "images/characters/dummy.png"
    image riku defeated = "images/characters/dummy.png"
    image riku upset = "images/characters/dummy.png"
    image riku happy = "images/characters/dummy.png"
    image riku ill = "images/characters/dummy.png"
    image riku normal = "images/characters/dummy.png"
    image riku smirk = "images/characters/dummy.png"
    image riku surprised = "images/characters/dummy.png"
    image riku wondering = "images/characters/dummy.png"

    #Megumi
    image megumi uniform happy = "images/characters/dummy.png"
    image megumi uniform realization = "images/characters/dummy.png"

    #Yuta
    image yuta uniform normal = "images/characters/dummy.png"
    image yuta uniform realization = "images/characters/dummy.png"
    image yuta uniform sadisticExcitement = "images/characters/dummy.png"

    #Sora
    image sora uniform happy = "images/characters/dummy.png"
    image sora uniform mischievous = "images/characters/dummy.png"

    ###################
    # Background images
    ###################
    image bg darkness = "images/backgrounds/darkness.png"
    image bg field = "images/backgrounds/dummy.png"

    image bg kasai house outside = "images/backgrounds/dummy.png"
    image bg kasai house inside = "images/backgrounds/dummy.png"
    image bg kasai house hallway = "images/backgrounds/dummy.png"
    image bg kasai house hallway night = "images/backgrounds/dummy.png"
    image bg misaki room = "images/backgrounds/dummy.png"
    image bg misaki room night = "images/backgrounds/dummy.png"
    image bg kosuke room = "images/backgrounds/dummy.png"
    image bg kosuke room night = "images/backgrounds/dummy.png"
    image bg haruki room = "images/backgrounds/dummy.png"
    image bg haruki room night = "images/backgrounds/dummy.png"

    image bg commercialCenter = "images/backgrounds/dummy.png"
    image bg cafe outside = "images/backgrounds/dummy.png"
    image bg cafe inside = "images/backgrounds/dummy.png"
    image bg cafe closet = "images/backgrounds/dummy.png"

    ###################
    # Misc images
    ###################
    image heart one = "images/misc/heart_grey.png"
    image heart two = "images/misc/heart_blue.png"
    image heart three = "images/misc/heart_purple.png"
    
    ####################################
    # Character heart meters
    ####################################
    init python:
        heart_pos = Position(xpos=0.1375, ypos=0.795)

        ###################
        # Kosuke
        ###################
        kosuke_points = 0
    
        def heart_kosuke(event, interact=True, **kwargs):
            if not interact:
                return

            #Display heart image dependant on the character's heart level
            # Only show Kosuke's heart meter if it is high enough
            if event == "begin":
                if kosuke_points < 2:
                    #Do nothing
                    return
                elif kosuke_points < 3:
                    renpy.show(name="heart three", layer="overlay", at_list=[heart_pos])
    
        ###################
        # Misaki
        ###################
        misaki_points = 0
    
        def heart_misaki(event, interact=True, **kwargs):
            if not interact:
                return

            #Display heart image dependant on the character's heart level
            if event == "begin":
                if misaki_points < 1:
                    renpy.show(name="heart one", layer="overlay", at_list=[heart_pos])
                elif misaki_points < 2:
                    renpy.show(name="heart two", layer="overlay", at_list=[heart_pos])
                elif misaki_points < 3:
                    renpy.show(name="heart three", layer="overlay", at_list=[heart_pos])
    
    ####################################
    # Character declarations
    ####################################
    define haruki = Character('Haruki', color="#00FF7F")
    define kosuke = Character('Kosuke', color="#40E0D0", callback=heart_kosuke)
    define misaki = Character('Misaki', color="#EE82EE", callback=heart_misaki)
    define riku = Character('Riku', color="#2E8B57")
    define sora = Character('Sora', color="#87CEEB")
    define megumi = Character('Megumi', color="#FFC0CB")
    define yuta = Character('Yuta', color="#FF0000")
    define msKasai = Character('Ms. Kasai', color="#5F9EA0")
    define mrKasai = Character('Mr. Kasai', color="#5F9EA0")
    
    ####################################
    # NVL narrator code
    ####################################
    init:
        $ h = Character(None, kind=nvl) #NVL narrator character
    
    init python:
        config.empty_window = nvl_show_core
        config.window_hide_transition = dissolve
        config.window_show_transition = dissolve
    
    ####################################
    # Screen positions
    ####################################

    init:
        $ char_left = Position(xpos=0.15, xanchor="left")
        $ char_right = Position(xpos=0.85, xanchor="right")
