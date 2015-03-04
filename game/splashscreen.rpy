#Scene/animation that is shown when the game is started
label splashscreen:

    #Title text
    $ middle = Position(xpos=0.5, xanchor=0.5, ypos = 0.5, yanchor=0.5)
    image title text = Text("Ganbatte", style="title_text")

    scene bg darkness
    with Pause(0.8)

    show title text at middle with dissolve
    with Pause(3)

    hide text with dissolve
    with Pause(1)

    return
