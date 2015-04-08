label heart_meter_declarations:
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

    return
