# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Layton")
define d = Character("Dog")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene campground

    play music "/audio/datesimmenu.mp3" 

    e "Yo waddup gamers, it's your boy at it again with some hot tips."

    e "Naw just kidding, it's me your camp councerloronio here to help you get adjusted to your new life at Whimsy-High-College"

    e "First order of business is to get you adjusted to your new life here! We are going to meet several of your teachers and classmates."

    e "I hope you concentrate on your studies and don't try to ~romance~ any of those hot studs out there. We take things very serio-"
   
    play sound "audio/woof.mp3"
   
    d "WOOF!"
    
    e "Holy shit is that a dog??"

    show dog

    play sound "audio/woof.mp3"

    d "Woof!"

   

    e "Holy shit.. holy shit...! pet.. PET THE DOG!" 
    
    play music "/audio/battlemusic.mp3" fadein 3.0
    
    menu:

        "Pet the dog":
            jump pet

        "Do not pet the dog":
            jump nopet

label pet:
    
    play music "/audio/06-Victory Fanfare-FFVI OST.mp3"


    # I don't know how to get this to work, oops
    
    show dog at animated
    
    e "Holy shit you did it! You petted the dog!"

    e "You get a full scholarship and will be the talk of the town!"

    "G O O D    E N D"

    return

label nopet:
    stop music
    
    e "You... absolute monster. I'm having you expelled this instant and I never want to see you again"

    "B A D    E N D "
    return


transform animated:
  "dog.png"
  pause 0.3
  "dogflip.png"
  pause 0.3
  repeat