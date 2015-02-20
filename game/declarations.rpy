label run_declarations:
    # Images

    #Character images

    #Background images
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

    #Misc images
    image heart one = "images/misc/heart_grey.png"
    image heart two = "images/misc/heart_blue.png"
    image heart three = "images/misc/heart_purple.png"
    
    # Character heart meters
    init python:
        heart_pos = Position(xpos=0.1375, ypos=0.795)

        # Kosuke
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
    
        # Misaki
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
    
    # Character declarations
    define haruki = Character('Haruki', color="#00FF7F")
    define kosuke = Character('Kosuke', color="#40E0D0", callback=heart_kosuke)
    define misaki = Character('Misaki', color="#EE82EE", callback=heart_misaki)
    define riku = Character('Riku', color="#2E8B57")
    define sora = Character('Sora', color="#87CEEB")
    define megumi = Character('Megumi', color="#FFC0CB")
    define yuta = Character('Yuta', color="#FF0000")
    define msKasai = Character('Ms. Kasai', color="#5F9EA0")
    define mrKasai = Character('Mr. Kasai', color="#5F9EA0")
    
    # NVL narrator code
    init:
        $ h = Character(None, kind=nvl) #NVL narrator character
    
    init python:
        config.empty_window = nvl_show_core
        config.window_hide_transition = dissolve
        config.window_show_transition = dissolve
