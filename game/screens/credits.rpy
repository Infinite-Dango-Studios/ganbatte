##############################################################################
# Credits
#
# A screen that's used to display basic information about the game and its makers
screen credits():

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the menu.
    window:
        style "gm_root"

        use navigation

    grid 1 1:
        style_group "creditsBox"

        # The left column.
        vbox:
            frame:
                has vbox
                style_group "staffList"
                xfill True
                yfill True

                label _("Credits")

                frame:
                    has vbox
                    xfill True

                    style_group "creditsStudioLogo"
                    imagebutton idle im.Scale("images/misc/studio_logo.png", 428, 228) hover im.Scale(im.Grayscale("images/misc/studio_logo.png"), 428, 228) action OpenURL("https://infinite-dango-studios.github.io/")

                frame:
                    has vbox
                    xfill True

                    grid 2 1:
                        vbox:
                            style_group "staffListHeading"
                            text "Coders"
                        vbox:
                            style_group "staffListItems"
                            text ""
                            text "ExcaliburZero   "

                frame:
                    has vbox
                    xfill True

                    grid 2 1:
                        vbox:
                            style_group "staffListHeading"
                            text "Writers"
                        vbox:
                            style_group "staffListItems"
                            text ""
                            text "Sabre-Hecate   "

                frame:
                    has vbox
                    xfill True

                    grid 2 1:
                        vbox:
                            style_group "staffListHeading"
                            text "Artists"
                        vbox:
                            style_group "staffListItems"
                            text ""
                            text "juanitaylor"
                            text "ChocoTacoKitty"
                            text "boxesofflowers"

                frame:
                    has vbox
                    xfill True

                    grid 2 1:
                        vbox:
                            style_group "staffListHeading"
                            text "Helpers"
                        vbox:
                            style_group "staffListItems"
                            text ""
                            text "TheStoryLord   "

init -2:
    style creditsBox_frame:
        top_margin 50
        bottom_margin 50
        left_margin 50
        right_margin 200

    style staffList_frame:
        top_margin 5
        bottom_margin 5
        left_margin 50
        right_margin 50

    style staffListHeading_text:
        size 20

    style staffListHeading_vbox:
        left_margin 200

    style staffListItems_text:
        size 16
        left_margin 200
