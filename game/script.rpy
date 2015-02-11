# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Character declarations
define haruki = Character('Haruki', color="#c8ffc8")
define kosuke = Character('Kosuke', color="#c8ffc8")
define misaki = Character('Misaki', color="#c8ffc8")
define msKasai = Character('Ms. Kasai', color="#c8ffc8")
define mrKasai = Character('Mr. Kasai', color="#c8ffc8")

#NVL narrator code
init:
    $ h = Character(None, kind=nvl) #NVL narrator character

init python:
    config.empty_window = nvl_show_core
    config.window_hide_transition = dissolve
    config.window_show_transition = dissolve


# Start of game code
label start:

    #scene hallway / room
    #show kosuke
    #show misaki

    kosuke "Oh....OK, Haruki-kun. Uh...have fun."

    misaki "YAY! YOU MADE THE RIGHT CHOICE, HARUKI-KUN! THIS’LL BE REALLY FUN!"

    haruki "Oh...haha, you seem pretty excited..."

    misaki "I AM! RIGHT THIS WAY, HARUKI-KUN!"

    window show

    h "Misaki grabs my wrist and pulls me away from the dining room at a run. I’m happy to be spending this time with her, but she practically drags me across the carpet as we tear through the halls. She pulls me up the stairs, and we enter the first room on the left."

    #hide kosuke
    #hide misaki
    #scene misaki's room

    h "Her room is nice, if a little messy. It’s a lot like my room, although more personalized. Her bed is covered in bright purple sheets, and a little stuffed turtle sits atop them. Pictures cover her walls, mostly of her, Kosuke and her parents. A few pictures depict me and Misaki and a few others are just me."

    h "In truth, I do not remember when a few of them were taken, and I am not looking at the camera in them. On her desk sits a little pink book that I assume is the infamous diary, and I cautiously walk over to it."

    h "A loose paper is sticking out and I glance at it. It’s a sketch in pencil of a man. Upon further inspection, he is completely naked with the exception of a single, strategically placed heart. My eyes widen as I recognize the face…I’m fairly certain that it’s mine."

    window hide
    nvl clear

    haruki "Uh...you...uh...drew this?"

    #show misaki embarrassed

    "I’ve never seen a face go so red so quickly."

    misaki "N-NO! I-I MEAN, THAT’S NOTHING! ER, I MEAN...DON’T LOOK AT OTHER PEOPLE’S PERSONAL STUFF, IDIOT! ER...UH...HEY, LOOK MY BOOKSHELF, UH, LET’S LOOK AT BOOKS!"

    "Her face is the deepest shade of scarlet I have ever seen as she quickly pushes the sketch back into the depths of the notebook. I feel myself blushing a little too, this is kind of awkward."

    #show misaki normal (???)

    misaki "So...Haruki-kun, um, what kind of books do you like?"

    haruki "Um, a lot of things…most recently I’ve been reading Tokyo Ghoul."

    #show misaki excited

    misaki "Ooh, I have all of that, do you need the next book?"

    haruki "No, I’m on book 13 and I already have the 14th."

    #show misaki normal

    misaki "Oh, ok. Have you read Ouran High School Host Club? Elfen Lied? Watamote?"

    "She pulls the first book in each of these series’ out as she says their names. And then, she gets a devious grin."

    #show misaki evil

    misaki "Or maybe, you’re more into this, Haruki-kun?"

    "She pulls out two more books."

    misaki "Want to borrow my Sakura Trick or Girl Friends? Or maybe..."

    window show

    h "She drops all the books she is holding and moves quickly over to her bed."

    h "She pulls out a pink glittery box that says “Misaki’s childhood stuff”."

    h "When she lifts off the lid and removes the false bottom, I gasp. In her box are piles and piles of hentai and erotic dojinshi. She looks up at me with a mischievous glint in her eyes."

    window hide
    nvl clear

    misaki "Is this what you want, Haruki-kun?"

    haruki "I...er...wow, you sure have a wide range of genres..."

    #show misaki smirk

    misaki "You look kind of uncomfortable, Haruki-kun."

    "She puts the lid back on the hentai box and slides it under her bed."

    misaki "Don’t be an idiot, I’m just holding onto those for my friend."

    haruki "Mhm...suuuuure."

    #show misaki embarrassed

    misaki "L-LIKE YOU DON’T HAVE SECRET HENTAI. I’M GOING TO COME INTO YOUR ROOM WHEN YOU’RE SLEEPING AND SEARCH IT!"

    haruki "Wow, that sounds a little creepy."

    #sound slap

    misaki "SHUT UP, HARUKI-KUN!"

    "I laugh, despite the pain in my cheek. She’s acting just like we used to. We walk over to her bookshelf once more and I grab her copy of Fruits Basket."

    haruki "Can I take this?"

    #show misaki normal

    misaki "Fruits Basket? You haven’t read that yet? Sure, go ahead!"

    haruki "Thanks!"

    "I grab her copies of Fruits Basket, and I stack them up in my arms."

    #show misaki happy

    misaki "Hey, Haruki-kun, remember when we used to play Fruits Basket together in grade school? WE SHOULD PLAY IT AGAIN RIGHT NOW!"

    "I smile, remembering my childhood school days with Kosuke and Misaki. We did used to play Fruits Basket a lot. Although I haven’t played it since I moved away."

    haruki "That sounds fun…but we can’t play Fruits Basket now...it requires a large group! Even if we could get Kosuke and your parents, we still wouldn’t have enough people for a proper game of it. Maybe in the future, when I have some more friends."

    #show misaki excited

    misaki "TOTALLY! We could probably get Riku-senpai and Kokona-chan from work to play! Ooh, and Sora-kun and Yuta-kun and Megumi-chan!"

    "I recognize many of the names from elementary school."

    haruki "The same ones who went to our school? They all work there?"

    misaki "Yup! They sure do! Riku-senpai went there too, but you probably don’t remember him because he was three years ahead of us."

    haruki "Yeah..."

    "I’ve grown tired of carrying all these books, they’re getting heavy."

    haruki "I guess I should probably go back to my room now."

    misaki "No you don’t!"

    #sound door close

    "She moves across the room and closes the door."

    misaki "C’mon, you promised to have fun with me all night, you can’t go to bed now! It’s way too early!"

    haruki "Well, I mean, Fruits Basket is 23 books, that’s enough for now, I don’t need anything else to read."

    misaki "So let’s do something else fun! Like a dramatic reading or something! YEAH, LET’S DO THAT!"

    "She moves over to her bookshelf and begins looking through all her options."

    haruki "Haha, OK, but nothing from the hentai box, OK?"

    #show misaki smirk

    misaki "Are you sureeeeeee?"

    haruki "Yes!"

    #show misaki happy

    window show

    h "She laughs, and so do I. In the end, we read various scenes from Black Butler."

    h "She plays Sebastian and has me play Ciel. It’s pretty fun, and we make it through the first ten books, each of us taking on more and more characters as the series goes on."

    h "She takes Finny, I take Meyrin and Baldo. She gets Madam Red and Lau, I get Grell. In the end, it’s a lot of fun."

    h "Soon, it is pitch black outside her window."

    h "I am reading for the Undertaker when a knock on the door silences my speech."

    window hide
    nvl clear

    #show misaki normal
    #show msKasai horrified

    msKasai "Do either of you have any idea what time it is!? I thought Haruki went back to his room hours ago!"

    haruki "W-what time is it!?"

    msKasai "Ten minutes to midnight!"

    #show misaki horrified

    misaki "WHAT!?"

    #show msKasai normal

    msKasai "You should go to sleep, Misaki-chan. You too, Haruchan. In separate bedrooms."

    "She smiles slightly, and exits the room with a polite nod."

    #show misaki embarrassed

    misaki "HOW DID YOU LET IT GET SO LATE, IDIOT?"

    "I don’t see why she’s so angry at me. She is the one who kept me here for our theatrical reading of Black Butler."

    haruki "Well, I’m going to be going now. This was fun, though!"

    "I pick up my copies of Fruits Basket, and I quickly exit the room, closing her door behind me."

    #hide misaki
    #hide msKasai
    #sound door close

    #scene hallway

    "When I pass Kosuke’s room on the way back to my own, it is dark. I’d planned to say hello to him, but it appears that he is already asleep."

    #scene haruki's room

    "In my room, I place my newly acquired books on the bedside table. I yawn, and decide that it is too late to start the series tonight. Turning off the light, I climb into bed and fall asleep."

    return
