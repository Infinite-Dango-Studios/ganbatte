# Create menu used in the game

label in_game_menu:
    python:
        # Import navigation buttons from options file
        layout.navigation("in_game_menu")
        ui.interact()

screen game_menu:
    tag menu

    style_group "game_menu"

    vbox:
        pos (0.5, 0.5)
        anchor (0.5, 0.5)
        textbutton _("Continue") action Return()
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Main Menu") action MainMenu()
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()
