# Run the declarations and code stored in the declarations directory
call image_declarations
call character_declarations
call heart_meter_declarations
call other_declarations

# Start of game code
label start:

    # Stop main menu music
    stop music

    # Start game from first scripting page
    jump dayOne

    return
