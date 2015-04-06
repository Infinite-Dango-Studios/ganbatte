# Run the declarations and code stored in "declarations.rpy"
call run_declarations

# Start of game code
label start:

    # Stop main menu music
    stop music

    jump dayOne

    return
