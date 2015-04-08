label character_declarations:
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
