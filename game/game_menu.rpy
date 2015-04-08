##############################################################################
# In-Game Menu
#
# Screen that pops up over the game screen when the user presses the right
# mouse button. Has basic links to several other menus.
screen game_menu:
    tag menu

    style_group "game_menu"

    frame:
        pos (0.5, 0.5)
        anchor (0.5, 0.5)

        # Allow for style modifications
        style_group "inGameMenu"

        has vbox
        textbutton _("Return") action Return()
        textbutton _("Skip") action Skip()
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Main Menu") action MainMenu()
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()

init -2:
    # Style the buttons in the in-game menu
    style inGameMenu_button:
        # Set buttons in in-game menu to fill the whole horizontal space
        size_group "gm_nav"
