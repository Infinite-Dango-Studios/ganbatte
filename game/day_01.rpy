label dayOne:

    window show

    h "I’ll never forget that summer."

    #music pensive

    h "The summer that I spent in Maura. The summer that I met her. That summer, when I met all of them."

    h "So many regrets, but also so many things I don’t regret...so many things that I wouldn’t trade for the world."

    h "The people I met, the things I experienced..."

    h "It all started when I went to live with Kosuke Kasai, my friend from grade school, and his twin sister, Misaki."

    h "I needed a change of pace before moving on to college and the next stage of my life, and they were happy to provide it."

    #scene field

    h "It was sunny the day that I arrived, and the sun felt warm on my face. As the warm summer breeze enveloped me, I could already tell that this trip would be exactly what I need."

    h "They were waiting for me, looking just as I remembered them, only a little older."

    window hide
    nvl clear

    #show kosuke happy
    #show misaki
    #music happy

    kosuke "HI HARUKI-KUN~! HOW ARE YOU? I HAVEN’T SEEN YOU IN AGES! You still look as handsome as ever, though, wouldn’t you say so, Misaki-chan?"

    #show misaki embarrassed

    misaki "Why would you ask me that!?!"

    #show kosuke smirk

    kosuke "I DON’T KNOW, MAYBE ALL OF THOSE DIARY--!"

    #show misaki angry

    misaki "SHUT UP! THERE ARE NO DIARY ENTRIES."

    "She seems pretty upset by her brother’s accusation, so maybe it’s a little more accurate than she wants to admit."

    #show kosuke happy
    #play laugh

    kosuke "She’s TOTALLY in love with you, Haruki-kun. What do you say, will you marry my darling sister?"

    menu:
        "W-where’s this coming from?":
            jump introWhere
        "NO! NEVER! WHY WOULD YOU EVEN...?":
            jump introNo
        "T-this is all very sudden...but...I’d be willing to try...":
            jump introWilling

    return

#Scene where Haruki answers "W-where’s this coming from?"
label introWhere:

    #Character points
    $ kosuke_points += 1
    $ misaki_points += 1

    kosuke "Geez, you’re turning pretty red!"

    "I feel a blush beginning to burn on my cheeks, and I know that he is telling the truth."

    haruki "W-well, I, um, I mean!"

    kosuke "Wow, you’re really flustered...You’re worse than me with girls!"

    misaki "Says the man who almost wet himself the last time he talked to a cute girl. My brother the charming lady’s man!"

    "Misaki’s laughing now, but Kosuke looks like he wants to evaporate like a water droplet on hot pavement."

    haruki "You still do that?"

    #show kosuke embarrassed

    kosuke "N-no!"

    #show misaki smirk

    misaki "Yes he does~! I have to take all the female customers at the café."

    jump kasaiHouse

    return

#Scene where Haruki answers "NO! NEVER! WHY WOULD YOU EVEN...?"
label introNo:

    #Character points
    $ misaki_points -= 1

    #show misaki angry

    misaki "NO? NEVER? WHAT THE HELL!?!"

    haruki "N-no...! I didn’t mean it like that, I meant..."

    #sound slap

    misaki "That was really rude, Haruki-kun."

    kosuke "Wow sis, you’re pretty offended...."

    haruki "I’m so sorry!"

    "I bow, although she still seems upset."

    misaki "Whatever."

    jump kasaiHouse

    return

#Scene where Haruki answers "T-this is all very sudden...but...I’d be willing to try..."
label introWilling:

    #Character points
    $ misaki_points += 1

    #show kosuke surprised

    kosuke "WHAT!?!!"

    #show misaki embarrassed

    misaki "I-IDIOT!"

    "And then, she said quieter"

    misaki "Did you really mean it?"

    haruki "Well, I, uh, I mean..."

    "I fumble for words, unsure what I should say. Luckily, Kosuke intervenes."

    kosuke "It was a joke! But I guess it wasn’t very funny..."

    jump kasaiHouse

    return

#Scene where Haruki goes to the Kasai house
label kasaiHouse:

    "A long moment of silence fell between the three of us before Kosuke speaks up again."

    kosuke "Annnnnnnyways~!"

    kosuke "So, Haurki-kun, you haven’t found anywhere to stay yet, have you?"

    "I look down at my feet, it’s true, I haven’t. And without a job, I can’t even afford to rent a place for myself. I sigh and remain silent."

    misaki "Maybe you should stay with us, Haruki-kun~!"

    haruki "Stay with you?"

    #show kosuke smirk

    kosuke "Wow sis, that’s pretty bold. He might see all the pictures you ha—"

    #show misaki embarrassed

    misaki "THERE ARE NO PICTURES!"

    misaki "DON’T LISTEN TO HIM HARUKI-KUN, HE’S JUST KIDDING. ONLY AN IDIOT WOULD BELIEVE HIM."

    "She seems pretty flustered. I wonder what pictures she has. Are they of me?"

    kosuke "Geez, I’m just kidding, sis."

    #show kosuke normal
    #show misaki normal

    kosuke "Anyway, want to stay with us?"

    "I don’t really have a choice."

    haruki "Sure, that would be nice."

    "It would be. It will be more fun living with them than on my own. And, now I’m curious about all of Misaki’s diary entries and pictures. This is going to be fun."

    kosuke "Awesome! This is great! We have a spare room, so you can probably stay there, if my parents say it’s ok."

    "Then, an odd smirk crossed his face."

    #show kosuke smirk

    kosuke "Or, you could stay in Misaki’s room!"

    #show misaki embarrassed

    misaki "STOP STAYING THINGS LIKE THAT, KOSUKE-KUN!"

    "They’re just as weird as I remember them."

    #show kosuke normal

    kosuke "Geez, sis, just kidding. Anyways, our house isn’t far from here. Just follow us Haruki-kun! We’ll be your guide to Maura and all its secrets!"

    haruki "Secrets?"

    "He says nothing in response, but merely smirks and gestures for me to join him and Misaki as they walk up the road into Maura."

    #hide kosuke
    #hide misaki

    window show

    h "I wonder what secrets he could be talking about. As far as I know, this is just a quiet place to raise a family. I suppose it has its fair share of interesting people, what place doesn’t? But secrets? That I doubt."

    h "Kosuke and Misaki are all the way up the hill now, and they’ve turned back to look at me. I had better follow them."

    h "I smile slightly and I walk with the breeze at my back, this summer is already turning out better than expected."

    #scene kasai house outside

    h "Kosuke and Misaki live in a cluster of houses a short walk from Maura’s main commercial center."

    h "I suppose that would be a good place to find a job, but I can think more about that later."

    h "The Kasai house is decently sized for a place such as this, with two floors and green shingles on the roof. A small sign reading “Kasai” sits at the end of a small stone path leading to a bright green door."

    h "Kosuke and Misaki are already standing on the porch and gesture for me to join them. "

    window hide
    nvl clear

    #show kasai house inside
    #show kosuke normal
    #show misaki normal

    "They slip on their house slippers, and I slip off my shoes."

    kosuke "There are some guest slippers, you can wear those!"

    haruki "Thank you!"

    misaki "MOM~! DAD~! WE’RE HOME~!"

    #hide kosuke
    #hide misaki
    #show msKasai happy
    #show mrKasai normal

    msKasai "Oh, Haruchan, is that you? You’ve grown up so much since the last time we saw you!"

    mrKasai "Well, it has been several years since we last saw him, honey!"

    msKasai "It has been a while, hasn’t it? How is your mother?"

    "I think back to all the times Ms. Kasai brought Kosuke and Misaki to my house to play when we were younger. She must be just as good friends with my mother as I am with Kosuke."

    haruki "She’s good!"

    "It’s a simplistic answer, but I don’t particularly feel like going into detail. It’s not like anything major has happened. No death or mysterious illness. Nothing out of the ordinary. Almost like the past couple of years did not even happen."

    msKasai "That’s good to hear! You’re staying in Maura for the summer, right?"

    "I open my mouth to answer, but Kosuke cuts me off before I can even get out a syllable."

    #hide mrKasai
    #show kosuke normal

    kosuke "Yeah, he is! But he doesn’t have anywhere to stay, so can he stay here?"

    msKasai "I don’t see why not! We’d love to host you, Haruchan!"

    "I feel relieved. I don’t think I realized until now how stressed out I was about not finding a place to stay."

    #hide msKasai
    #hide kosuke
    #show misaki normal
    #show mrKasai normal

    mrKasai "I was just about to start making dinner, you should probably unpack until it’s ready."

    #show misaki excited

    misaki "OOH, DAD! I WANT TO MAKE DINNER FOR HARUKI-KUN!"

    #show mrKosuke horrified

    mrKasai "ABSOLUTELY NOT! YOU ALMOST BURNED THE HOUSE DOWN LAST TIME!"

    #show misaki upset

    misaki "But I’ve been practicing since then! Just ask mom!"

    mrKasai "Fine, you can help."

    #show misaki excited

    misaki "Yay! It’s going to taste really good, Haruki-kun, I promise!"

    "And then she muttered something to herself that I couldn’t quite make out. I’m fairly certain that I heard the word “wife”. Oh well, I must have been just hearing things. A moment later, Misaki and Mr. Kasai disappear into the kitchen."

    #hide misaki
    #hide mrKasai
    #show msKasai normal
    #show kosuke normal

    msKasai "Kosuchan, can you help Haruchan unpack?"

    #show kosuke happy

    kosuke "Sure! Right this way, Haruki-kun!"

    #hide kosuke
    #hide msKasai

    #show hallway

    window show

    h "Kosuke leads me down the hallway, and we enter the second room to the left."

    #show haruki's room

    h "It is a small room, decorated comfortably but not particularly uniquely."

    h "There is a single window with flowered drapes, and the orangey light of the incoming sunset was seeping through it. A small wooden bookshelf sits in the corner to the left of the door, and a simple dark-wooden desk sits next to it."

    h "The bed sits beside the window, simple and twin-size, covered by pale blue sheets. A nightstand sits beside the bed, and like the bookshelf and desk it is empty."

    h "It is a plain room, and yet I cannot help but feel at home in it."

    h "Once I unpack everything, it will probably feel just like home."

    h "I place my bags on the bed and open them. Kosuke silently helps me unpack my clothes. They end up filling around half the closet, I do not really enjoy shopping for clothes."

    h "My clothes unpacked, we move on to my second bag, which is filled with various personal effects. I decide to fill the bookshelves first."

    window hide
    nvl clear

    #show kosuke excited

    kosuke "WHOA, NO WAY! YOU READ THIS TOO?"

    "He is holding my copy of Tokyo Ghoul volume one. I only really started the series a month ago, and I have not had much time to read it, but I enjoy it."

    haruki "Yeah! I’m only almost through it, and it’s been good so far."

    "I arrange my copies of Tokyo Ghoul on the bookshelf and I unload various other manga and light novels."

    kosuke "Hey, can I borrow these?"

    "He is holding my stack of No. 6. I’ve already read all of them, so I don’t see the harm."

    haruki "Sure, you’re living just upstairs, so I can find you if you try to steal them from me."

    #show kosuke innocent

    kosuke "You know I wouldn’t do that!"

    "Once we are finished stocking the bookshelf, I place my journal and handheld gaming device on the desk. My bags are empty now, so I place them in the closet."

    haruki "Do you suppose dinner is ready yet?"

    kosuke "Probably not. We didn’t take very long to unpack...Want to go to my room to play some video games while we wait?"

    haruki "Sure!"

    #hide kosuke
    #scene kasai house inside
    #show misaki happy

    misaki "Dinner time, Haruki-kun~!!!!"

    "When Kosuke and I arrived in the dining room, the table had been set with plates of Chirashizushi, Tempura and Dango. All of my favorites. I guess Misaki must have remembered, we did eat a lot together as children."

    misaki "Do you like it, Haruki-kun? I made it special for you!"

    haruki "Yeah, it’s all my favorites! Thank you."

    #show kosuke normal

    kosuke "Um, hey sis, I’m here too."

    #show misaki annoyed

    misaki "HARUKI-KUN IS THE GUEST!"

    #show kosuke smug

    kosuke "Well, you may have made him dinner, but I played video games with him and he let me borrow all his copies of No. 6."

    misaki "Really? Well maybe I have some books that he wants. Hey Haruki-kun, want to come to my room after dinner and check out my light novels and manga? I have, um, Spice and Wolf, and Black Bullet and Durarara!! and—"

    #show kosuke angry

    kosuke "HEY! HARUKI-KUN PROMISED TO PLAY MORE SMASH BROS AFTER DINNER WITH ME!"

    "They’re practically screaming at each other now, and I feel a blush burn on my cheeks."

    #show misaki angry

    misaki "YOU’VE HAD HIM THE ENTIRE TIME HE’S BEEN HERE!"

    kosuke "YOU DO REALIZE THAT IT’S ONLY BEEN, LIKE, AN HOUR, RIGHT? AND BESIDES, HE’S MY BEST FRIEND!"

    "I smile awkwardly. Are they fighting over me? Living here is certainly going to be interesting."

    haruki "Um....I’m kinda hungry, maybe we can just have dinner? I can decide what I want to do later."

    "They seem to remember that I’m there, and they both blush."

    #show kosuke embarrassed
    #show misaki embarrassed

    kosuke "Oh, haha, sorry, Haruki-kun, I sort of forgot that you were there for a minute."

    misaki "Sorry that my brother’s such an idiot, Haruki-kun!"

    #hide kosuke
    #hide misaki

    "I’m not really sure how to respond to the two of them so I just laugh and we all sit down at the table."

    "For a few minutes, the only noises are the cacophony of noises which typically accompany eating. Both Kosuke and Misaki are eating quietly and won’t make eye contact to me. I suppose that they’re guilty about fighting over me. Finally, Mr. Kasai speaks up."

    #show mrKasai normal
    #show msKasai normal

    mrKasai "So, Haruchan, what are your plans for this summer?"

    "I sit silently for a few moments, taking another bite of Chirashizushi. I realize now just how poorly planned this trip is. I guess I just decided to come to Maura to see Kosuke and Misaki. But now the question’s been asked and he’s waiting for a response. If I don’t speak up now, he could kick me out! It could ruin the entire trip. Possibly."

    haruki "Um....I guess I want to meet some interesting people? And I should probably get a job."

    msKasai "Do you have any ideas for employment?"

    "I think it over for a moment before shaking my head. I don’t really know who’s hiring in Maura at the moment."

    #hide mrKasai
    #hide msKasai
    #show kosuke normal
    #show misaki excited

    misaki "YOU SHOULD COME WORK AT THE CAFÉ!"

    "She practically jumps out of her seat as she says it. These guys sure are eager to spend time with me."

    haruki "What café?"

    #show kosuke confused

    kosuke "I never told you, Haruki-kun? Misaki and I work at a little café in town. The coworkers are all pretty great. You’ll love Kokona-chan, she’s super sweet. The customers are all really interesting too. Plus, our boss, Riku-san is totally cool. He’ll probably hire you without too much convincing."

    haruki "Ehh, I don’t know..."

    "It sounds like a good job, to be honest. It sounds like I’ll meet some interesting people, and I’ll be able to get the job without much of a struggle. That’s always a bonus. And yet, at the same time, I’ve never really pictured myself working at a café. It doesn’t really seem like my sort of thing."

    #show kosuke upset

    kosuke "Aww, C’mon! It could be a lot of fun..."

    #show misaki smirk

    misaki "Plus you’ll get to see me in my cute uniform~! Every day! What else could you possibly want?"

    "I feel a deep blush erupt on my cheeks, and I try not to look Misaki directly in the eye. I see Mr. and Ms. Kasai looking back and forth between me and Misaki, and I can tell that they are reconsidering allowing us to sleep in the same house."

    haruki "Haha, well...when you put it like that!"

    #show kosuke beaming

    kosuke "GREAT! Misaki and I have work tomorrow, so I can introduce you to Riku-san then!"

    "I nod my agreement, it sounds good. In truth, I was hoping for a little time to relax before getting too busy, but this job sounds fun at least."

    "Dinner is over not long after that, and both Kosuke and Misaki look at me expectantly after all the dishes have been cleared. It suddenly dawns on me that I can’t put off the decision any longer. I’ll have to either go to Misaki’s room or to Kosuke’s. But which one should I choose?"

    kosuke "So, Haruki-kun, what’s happening now?"

    misaki "Yeah, Haruki-kun, did you decide where you want to go?"

    menu:
        "I think it would be fun to hang out with you, Misaki-chan!":
            jump misakaRoom
        "I think I’d like to play more video games with Kosuke-kun!":
            jump kosukeRoom
        "Actually, I’m kinda tired. And tomorrow’s going to be busy. I’m just going to go to bed.":
            jump harukiRoom

    return


#Scene where Haruki answers "I think it would be fun to hang out with you, Misaki-chan!"
label misakaRoom:

    #Character points
    $ misaki_points += 1

    #show kosuke normal
    #show misaki normal

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

    h "A loose paper is sticking out and I glance at it. It’s a sketch in pencil of a man. Upon further inspection, he is completely naked with the exception of a single, strategically placed heart. My eyes widen as I recognize the face...I’m fairly certain that it’s mine."

    window hide
    nvl clear

    haruki "Uh...you...uh...drew this?"

    #show misaki embarrassed

    "I’ve never seen a face go so red so quickly."

    misaki "N-NO! I-I MEAN, THAT’S NOTHING! ER, I MEAN...DON’T LOOK AT OTHER PEOPLE’S PERSONAL STUFF, IDIOT! ER...UH...HEY, LOOK MY BOOKSHELF, UH, LET’S LOOK AT BOOKS!"

    "Her face is the deepest shade of scarlet I have ever seen as she quickly pushes the sketch back into the depths of the notebook. I feel myself blushing a little too, this is kind of awkward."

    #show misaki normal (???)

    misaki "So...Haruki-kun, um, what kind of books do you like?"

    haruki "Um, a lot of things...most recently I’ve been reading Tokyo Ghoul."

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

    haruki "That sounds fun...but we can’t play Fruits Basket now...it requires a large group! Even if we could get Kosuke and your parents, we still wouldn’t have enough people for a proper game of it. Maybe in the future, when I have some more friends."

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

    jump dayTwo

    return

#Scene where Haruki answers "I think I’d like to play more video games with Kosuke-kun!"
label kosukeRoom:

    #Character points
    $ kosuke_points += 1

    #show misaki angry

    misaki "WHAT AN IDIOTIC CHOICE, HARUKI-KUN!"

    #show kosuke smug

    kosuke "Ha! You’re just mad because he chose me. You made the right choice Haruki-kun~!"

    "Misaki seems too upset to respond, and she storms off muttering something about ‘when a cute girl invites you into her bedroom you shouldn’t say no’."

    #hide misaki
    #show kosuke smirk

    kosuke "Wow, Misaki-chan’s pretty crazy, right? I wasn’t kidding about those diary entries and pictures you know~!"

    haruki "Err...right."

    #show kosuke happy

    kosuke "Or maybe I am joking? Haha, you’ll never know I guess~!"

    #show kosuke normal

    kosuke "But we’re wasting time, let’s go play!"

    "Kosuke runs off in the direction of his room, leaving me to wonder if I should have gone with Misaki. Does she really have pictures and diary entries!?"

    #show kosuke happy

    kosuke "Hey, Haruki-kun, what are you waiting for!?"

    "Shaking out of my pensive daze, I follow after him. We return to his room, and he walks over to his game shelf."

    #scene kosuke's room

    kosuke "What do you want to play?"

    haruki "Hmmm, not sure..."

    #show kosuke fakeserious

    kosuke "This is serious business, Haruchan. If we play the wrong thing, it could ruin our friendship. FOREVER."

    haruki "So it’s a no to Mario Party, then?"

    #show kosuke happy

    kosuke "THAT’S THE SPIRIT, HARUCHAN~!"

    "He looks through his game shelf, pulling out several cases and putting them back. He continues silently in this way for several minutes before finally speaking up."

    kosuke "OK, HARUCHAN! I HAVE THE GAME FOR US! WE’RE GOING TO PLAY...DANCE. DANCE. REVOLUTION. X!!!!"

    "He pulls the game off his shelf with a flourishing gesture, and shoves it in my face."

    kosuke "AND YOU CAN BET THAT WE’RE GOING TO PLAY KOKO SOKO AND SUKI MELO~! YOU’D BETTER SING ALONG, HARUCHAN, I KNOW THAT YOU KNOW THE WORDS!"

    "Without waiting for my response, Kosuke puts the disc into his game console and pulls out the two DDR mats. Flashing me a bright smile, he turns on the game console and gestures for me to take my place beside him."

    #wait a few seconds

    kosuke "YOU CAN DO BETTER THAN THAT, HARUCHAN!"

    haruki "I’m...trying! This song is fast, I haven’t played in forever!"

    kosuke "Yeah, but if I totally beat you it’s not as fun as if it’s super close! Plus you aren’t even singing along!"

    haruki "I’m....TRYING~!"

    #wait a few seconds

    kosuke "Wow, you just missed ten steps in a row!"

    #sound stepsMissed

    haruki "SHOULDN’T YOU BE FOCUSING ON YOUR OWN DANCE MOVES!?!"

    #show kosuke smirk

    kosuke "I don’t need to! At this rate, I could beat you with my eyes closed!"

    haruki "So do it!"

    #show kosuke surprised

    kosuke "WHAT!?"

    haruki "If you’re so confident that you could beat me with your eyes closed, do it!"

    #show kosuke victory

    kosuke "CHALLENGE ACCEPTED!"

    #show kosuke victoryEyesClosed

    #wai a few seconds

    #sound stepsMissed

    #show kosuke smirk

    kosuke "You still lost that round."

    haruki "Yeah, well...IT WAS A LOT CLOSER THAT TIME!"

    #show kosuke smile???

    kosuke "I had my eyes closed."

    haruki "FINE! LET’S GO AGAIN! EYES OPEN, AND I’M GOING TO BEAT YOU!"

    #show kosuke happy

    kosuke "YOU’D BETTER SING ALONG THIS TIME, HARUCHAN!"

    #wait a few seconds

    #sound musicSounds

    #scene kosuke's room night

    "We play DDR for hours, until we are both out of breath and sweating through our clothes. Kosuke makes me play Suki Melo over twenty times in a row until I finally sang along. By the end, we are both dancing around and acting like pop stars, screaming lyrics in falsetto at the top of our lungs. When Kosuke finally turns off the console, I collapse on his floor."

    #show kosuke tired

    kosuke "Wow...we sure played for a long time..."

    #sound yawn

    haruki "Yeah...I’m out of breath and pretty tired..."

    "I glance over at Kosuke’s digital clock. It reads 12:30 AM. How did it get so late!?!"

    kosuke "Wow...Haru-chan, is that the time!?! We should really go to bed, we have to get up early for work tomorrow..."

    "I stand up, yawning."

    haruki "Thanks again for helping me get this job!"

    #show kosuke happy

    kosuke "Yeah, anything for you Haru-chan~! I really, really want to work with you, so it’s not like I’m not getting anything out of it!"

    "He gently punches me in the arm, and I laugh. Then I yawn again. I’m so tired that I can barely stand, and I feel my center of balance shifting ever so slightly from side to side."

    haruki "Goodnight, Kosuke!"

    kosuke "Goodnight, Haru-chan~!"

    "He pauses before adding"

    kosuke "Hey, thanks for choosing me over Misaki tonight..."

    "This addition surprises me. I know that he and Misaki have some sort of sibling rivalry over me, but it sounds like he would have been legitimately hurt if I had chosen Misaki over him. However, all I can manage in response is"

    kosuke "Huh?"

    #show kosuke embarrassed

    kosuke "Oh, no, it’s nothing. Night, Haru-chan."

    "He waves off my inquiry with a dismissive wave of his hand and suddenly I get the overbearing feeling that I have just missed my chance to hear something important."

    #hide kosuke
    #show hallway

    "Giving a warm smile which Kosuke returns, I leave his room. I look back at Misaki’s room, hoping to say a quick goodnight to her before going to bed, but I find her room to be dark. She must be asleep already."

    #show haruki's room

    "Returning to my room, I find a stack of Fruits Basket manga on my bedside table. There’s a handwritten note attached to the top book in the stack and I pull it off."

    window show

    h "Hey, Haruki-kun, I know you haven’t read this before. Remember when we used to play fruits basket in elementary school? It was a lot of fun."

    h "Sorry that I couldn’t spend time with you tonight, but I figured that you would like this."

    h "See you bright and early tomorrow~!"

    h "~Misaki"

    window hide
    nvl clear

    "I guess Misaki left these here for me to read. I’ve been wanting to read this series, I wonder how she knew."

    "I yawn yet again. Turning off the light, I fall asleep the second my head hits the pillow."

    jump dayTwo

    return

#Scene where Haruki answers "Actually, I’m kinda tired. And tomorrow’s going to be busy. I’m just going to go to bed."
label harukiRoom:

    #show misaki horrified

    misaki "WHAT!?!"

    #show kosuke horrified

    kosuke "Are...are you serious!?!"

    "They both seem pretty upset. I had planned to upset neither of them with this neutral response. I guess that kinda backfired."

    haruki "Uh...yeah...I’m tired and I’m going to start working tomorrow..."

    kosuke "Aww, but it’s still early..."

    misaki "Yeah...you promised to hang out with us..."

    kosuke "The café isn’t even hard work. You can get by on maybe two hours of sleep, three tops!"

    "I feel pretty awkward now. I had hoped it would be an easy out. I guess I did not think through this very well."

    haruki "Well, I mean...I was travelling all day. I’m just, tired, that’s all. I promise I’ll spend time with you guys tomorrow, it’s just that..."

    "I trail off, I do not really have anything else to say to validate my choice. Now I feel a blush creeping its way onto my cheeks, and the tips of my ears feel hot."

    #hide misaki
    #hide kosuke

    #show mrKasai normal
    #show msKasai normal

    msKasai "It’s perfectly fine, Haru-chan!"

    mrKasai "It’s perfectly natural to get tired after extended traveling."

    msKasai "You shouldn’t feel guilty for needing sleep, Haru-chan, Kosuke and Misaki can wait until tomorrow to catch up with you."

    mrKasai "It’s admirable that you want to be well-rested to make a good impression on Riku-san tomorrow."

    haruki "Thank you, Mr. Kasai..."

    #show mrKasai happy

    mrKasai "Of course. Goodnight!"

    msKasai "Goodnight, Haru-chan!"

    haruki "Goodnight."

    #hide mrKasai
    #hide msKasai

    #show misaki upset
    #show kosuke upset

    kosuke "Sorry about making you feel bad...but we have to hang out tomorrow, OK?"

    haruki "Haha, it’s a deal!"

    #show misaki smirk

    misaki "Not if I get to him first tomorrow!"

    haruki "I’ll see you two in the morning~!"

    "I smile and wave as I walk away back to my room, and they wave back and exchange a competitive glare with each other."

    #hide kosuke
    #hide misaki

    #scene haruki's room

    window show

    h "Admittedly, I had lied about being tired."

    h "I just really did not want to choose between them."

    h "I look over at my bed. I don’t feel even remotely interested in sleeping just yet. The sun still paints the sky violet outside my window, it isn’t even fully dark yet."

    h "I turn off my light; I need to give at least the illusion that I am sleeping."

    h "Moving silently over to my desk, I grab my gaming device and my headphones. Putting the headphones on my ears I move over to my bed and get under the covers."

    h "I silently laugh at myself, I am like a child staying up past their bedtime and trying to hide it from their parents."

    nvl clear

    h "I don’t know how much time elapses while I play video games."

    h "I once again complete the story mode of Kid Icarus Uprising before playing at least an hour of Light vs. Dark wifi battles."

    #show haruki's room night

    h "When I finally emerge from the covers, it is pitch black out my window."

    h "I take off my headphones and listen. The house is silent, everyone else must be asleep."

    h "I yawn. I guess I’m starting to get tired too. I check the clock on my handheld and it reads 1:01 AM. So much for going to bed early."

    h "Turning off my handheld and silently returning it to its place on my desk, I return to my bed."

    h "It takes me a few minutes to fall asleep, but then I am out cold. "

    window hide
    nvl clear

    jump dayTwo

    return
