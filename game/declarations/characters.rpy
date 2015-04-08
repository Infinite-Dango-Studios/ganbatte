label character_declarations:
    ####################################
    # Character heart meters
    ####################################
    init python:
        heart_pos = Position(xpos=0.22, ypos=0.724)

        ###################
        # Kosuke
        ###################
        kosuke_points = 0
        kosuke_heart_levels = [2, 3]

        def heart_kosuke(event, interact=True, **kwargs):
            if not interact:
                return

            # Display heart image dependant on the character's heart level
            if event == "begin":
                # Only show Kosuke's heart meter if it is high enough
                if kosuke_points < kosuke_heart_levels[0]:
                    # Do nothing
                    return
                elif kosuke_points < kosuke_heart_levels[1]:
                    renpy.show(name="heart three", layer="icons", at_list=[heart_pos])

        ###################
        # Misaki
        ###################
        misaki_points = 0
        misaki_heart_levels = [1, 2, 3]

        def heart_misaki(event, interact=True, **kwargs):
            if not interact:
                return

            # Display heart image dependant on the character's heart level
            if event == "begin":
                if misaki_points < misaki_heart_levels[0]:
                    renpy.show(name="heart one", layer="icons", at_list=[heart_pos])
                elif misaki_points < misaki_heart_levels[1]:
                    renpy.show(name="heart two", layer="icons", at_list=[heart_pos])
                elif misaki_points < misaki_heart_levels[2]:
                    renpy.show(name="heart three", layer="icons", at_list=[heart_pos])

        ###################
        # Kokona
        ###################
        kokona_points = 0
        kokona_heart_levels = [1, 2, 3]

        def heart_kokona(event, interact=True, **kwargs):
            if not interact:
                return

            # Display heart image dependant on the character's heart level
            if event == "begin":
                if kokona_points < kokona_heart_levels[0]:
                    renpy.show(name="heart one", layer="icons", at_list=[heart_pos])
                elif kokona_points < kokona_heart_levels[1]:
                    renpy.show(name="heart two", layer="icons", at_list=[heart_pos])
                elif kokona_points < kokona_heart_levels[2]:
                    renpy.show(name="heart three", layer="icons", at_list=[heart_pos])

        ###################
        # Yuuki
        ###################
        yuuki_points = 0
        yuuki_heart_levels = [1, 2, 3]

        def heart_yuuki(event, interact=True, **kwargs):
            if not interact:
                return

            # Display heart image dependant on the character's heart level
            if event == "begin":
                if yuuki_points < yuuki_heart_levels[0]:
                    renpy.show(name="heart one", layer="icons", at_list=[heart_pos])
                elif yuuki_points < yuuki_heart_levels[1]:
                    renpy.show(name="heart two", layer="icons", at_list=[heart_pos])
                elif yuuki_points < yuuki_heart_levels[2]:
                    renpy.show(name="heart three", layer="icons", at_list=[heart_pos])

        ###################
        # Momoko
        ###################
        momoko_points = 0
        momoko_heart_levels = [1, 2, 3]

        def heart_momoko(event, interact=True, **kwargs):
            if not interact:
                return

            # Display heart image dependant on the character's heart level
            if event == "begin":
                if momoko_points < momoko_heart_levels[0]:
                    renpy.show(name="heart one", layer="icons", at_list=[heart_pos])
                elif momoko_points < momoko_heart_levels[1]:
                    renpy.show(name="heart two", layer="icons", at_list=[heart_pos])
                elif momoko_points < momoko_heart_levels[2]:
                    renpy.show(name="heart three", layer="icons", at_list=[heart_pos])

    ####################################
    # Character declarations
    ####################################
    define haruki = Character('Haruki', color="#00FF7F", ctc="ctc_animation", ctc_position="fixed", show_two_window="true")
    define kosuke = Character('Kosuke', color="#40E0D0", ctc="ctc_animation", ctc_position="fixed", show_two_window="true", callback=heart_kosuke)
    define misaki = Character('Misaki', color="#EE82EE", ctc="ctc_animation", ctc_position="fixed", show_two_window="true", callback=heart_misaki)
    define riku = Character('Riku', color="#2E8B57", ctc="ctc_animation", ctc_position="fixed", show_two_window="true")
    define sora = Character('Sora', color="#87CEEB", ctc="ctc_animation", ctc_position="fixed", show_two_window="true")
    define megumi = Character('Megumi', color="#FFC0CB", ctc="ctc_animation", ctc_position="fixed", show_two_window="true")
    define yuta = Character('Yuta', color="#FF0000", ctc="ctc_animation", ctc_position="fixed", show_two_window="true")
    define kokona = Character('Kokona', color="#FF00FF", ctc="ctc_animation", ctc_position="fixed", show_two_window="true", callback=heart_kokona)
    define msKasai = Character('Ms. Kasai', color="#5F9EA0", ctc="ctc_animation", ctc_position="fixed", show_two_window="true")
    define mrKasai = Character('Mr. Kasai', color="#5F9EA0", ctc="ctc_animation", ctc_position="fixed", show_two_window="true")

    # Characters that start out as "???"
    define yuuki = DynamicCharacter("yuuki_name", color="#FF8C00", show_two_window="true", callback=heart_yuuki)
    define momoko = DynamicCharacter("momoko_name", color="#FF69B4", show_two_window="true", callback=heart_momoko)

    # Narrator character
    define narrator = Character(None, ctc="ctc_animation", ctc_position="fixed")

    ####################################
    # NVL narrator code
    ####################################
    init:
        $ h = Character(None, kind=nvl) # NVL narrator character

    init python:
        config.empty_window = nvl_show_core
        config.window_hide_transition = dissolve
        config.window_show_transition = dissolve

    return
