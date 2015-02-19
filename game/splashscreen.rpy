#Scene/animation that is shown when the game is started
label splashscreen:

    scene bg darkness
    with Pause(0.8)

    show text "Ganbatte" with dissolve
    with Pause(3)

    hide text with dissolve
    with Pause(1)

    return
