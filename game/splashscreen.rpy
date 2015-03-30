#Scene/animation that is shown when the game is started
label splashscreen:

    #Studio Logo
    init:
        $ mid = Position(xpos=0.5, xanchor=0.5, ypos = 0.5, yanchor=0.5)

    image studio logo = im.Scale("images/misc/studio_logo.png", 500, 267)

    scene bg darkness
    with Pause(0.8)

    show studio logo at mid with dissolve
    with Pause(4.5)

    hide studio logo with dissolve
    with Pause(1)

    return
