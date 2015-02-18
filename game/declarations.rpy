label run_declarations:
    # Declare images below this line, using the image statement.
    # eg. image eileen happy = "eileen_happy.png"
    image heart grey = "images/heart_grey.png"
    image heart blue = "images/heart_blue.png"
    image heart purple = "images/heart_purple.png"
    
    # Character heart meters
    init python:
        heart_pos = Position(xpos=0.1375, ypos=0.795)
    
        # Misaki
        misaki_points = 0
    
        def heart_misaki(event, interact=True, **kwargs):
            if not interact:
                return
    
            if event == "begin":
                if misaki_points < 1:
                    renpy.show(name="heart grey", layer="overlay", at_list=[heart_pos])
                elif misaki_points < 2:
                    renpy.show(name="heart blue", layer="overlay", at_list=[heart_pos])
                elif misaki_points < 3:
                    renpy.show(name="heart purple", layer="overlay", at_list=[heart_pos])
    
    # Character declarations
    define haruki = Character('Haruki', color="#00FF7F")
    define kosuke = Character('Kosuke', color="#40E0D0")
    define misaki = Character('Misaki', color="#EE82EE", callback=heart_misaki)
    define riku = Character('Riku', color="#5F9EA0")
    define sora = Character('Sora', color="#5F9EA0")
    define megumi = Character('Megumi', color="#5F9EA0")
    define yuta = Character('Yuta', color="#5F9EA0")
    define msKasai = Character('Ms. Kasai', color="#5F9EA0")
    define mrKasai = Character('Mr. Kasai', color="#5F9EA0")
    
    # NVL narrator code
    init:
        $ h = Character(None, kind=nvl) #NVL narrator character
    
    init python:
        config.empty_window = nvl_show_core
        config.window_hide_transition = dissolve
        config.window_show_transition = dissolve
