label endCredits:

    scene bg darkness

    # Prepair the credits
    init python:
        # Variables to control and setup the credits text
        credits_duration = 16.0
        credits_text = ""

        # Function to add a line to the credits
        def addLine(credits_text, line):
            # Add the line to the credits
            credits_text += line + "\n\n"

            return credits_text

        # Function to add a section to the credits
        def addSection(credits_text, title, names):
            # Add the section title to the credits
            credits_text += title + "\n\n"
            # Add all of the names in the section to the credits
            for name in names:
                credits_text += name + "\n"
            # Add some extra newlines to the credits
            credits_text += "\n\n"

            return credits_text

        # Text for artists credits
        artists = ["juanitaylor", "ChocoTacoKitty", "boxesofflowers"]
        credits_text = addSection(credits_text, "Artists", artists)

        # Text for coders credits
        coders = ["Christopher Wells [ExcaliburZero]"]
        credits_text = addSection(credits_text, "Coders", coders)

        # Text for writers credits
        writers = ["Stephen Sesonske [Sabre-Heacte]"]
        credits_text = addSection(credits_text, "Writers", writers)

        # Text for resource credits
        resources = ["Jeremy Winter (Music)"]
        credits_text = addSection(credits_text, "Resources", resources)

        # Add note to Ren'Py
        credits_text = addLine(credits_text, "This game was created with the Ren'Py engine.")

    # Image that is used to display the credits
    image creditscroll:
        Text(credits_text, style="endCreditsText")
        anchor (0.5, 0.0)
        pos (0.5, 1.0)
        linear credits_duration ypos 0.0 yanchor 1.0

    # Set the styling of the credits text
    style endCreditsText is text:
        size 20
        color "#FFF"

    # Run the credits
    show creditscroll
    $ renpy.pause(credits_duration, hard=True)
    hide creditscroll

    # Go to the development end screen
    jump devEnd

    return
