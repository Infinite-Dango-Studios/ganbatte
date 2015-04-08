# Create menu used in the game
screen game_menu:
    tag menu

    style_group "game_menu"

    vbox:
        pos (0.5, 0.5)
        anchor (0.5, 0.5)
        textbutton _("Return") action Return()
        textbutton _("Skip") action Skip()
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Main Menu") action MainMenu()
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()

init -2:
    style game_menu_vbox:
        xalign 0.5
        yalign 0.5
