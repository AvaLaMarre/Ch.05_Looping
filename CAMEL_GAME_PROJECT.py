'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book
'''

import random

# PRE GAME KNOWLEDGE
print("~|~Space~|~")
print("Welcome To Space,")
print("While Being Chassed By An Enemy Species Of Aliens You Crash Land On A Dessert Planet.")
print("Over In The Horizon You See A Ally Military Base,")
print("The Objective Is To Travel 200 Miles Across The Planet To Reach The Base.")
print("The Group Of Aliens Will Give Chase.")
print()
print("    You Know What Awaits You If Caught...")
print("                  ___----___ ")
print("                /    \  /    \ ")
print("       ________|     i  i     |________ ")
print("     (_____     ----______----    ______) ")
print("            --------------------- ")
'end Pre game knowledge'

'instructions'
ready = input("Are You Ready? YES|NO ")
ready = ready.lower()
if ready == "yes":
    print("Great, Here We Go,")
    print()
else:
    print("To Bad, Here We Go,")
    print()

print("You Will Be Asked For Commands Every So Often")
print("C  O  M  M  A  N  D  S:")
print("A. DRINK from your canteen")
print("B. MODERATE SPEED ahead")
print("C. FULL SPEED ahead")
print("D. STOP for the night")
print("E. STATUS check")
print("Q. QUIT")

print("You Find A Strange Creature That Reminds You Of A Camel")
print("                                            |\------____  ")
print("                                            |     i      | ")
print("                                            |    ___----  ")
print("                                            |     | ")
print("         _____       _____       _____     |      | ")
print("       /       \___/       \___/       \__/      |  ")
print("Make Sure It Doesnt Die Of Exhaustion, ")
print("You will have 1 quart of water which will last you six drinks.")
print("You may renew your water supply completely at an oases.")
# end of instructions

# start values
done = False
dead = False
win = False

miles_travelled = 0
thirst = 0
camel_tire = 0
canteen = 6
behind = -20
days = 0

# Game
print("You are in the middle of the desert at an oasis.")
while not done:
    if not dead:
        'Delete Later'
        print("M", miles_travelled, "B", behind, "t", thirst, "Can", canteen, "CT", camel_tire, "D", days)
        '-----'
        print()
        oasis = random.randrange(1, 21)
        if oasis == 9:
            print("You Found An Oasis, You Fill Up Your Canteen And Your Camel Like Creature Rest")
            canteen = 6
            camel_tire = 0
            thirst = 0
            print()

        print("You have travelled ", miles_travelled, " miles all together")
        print("A:DRINK B:MODERATE SPEED C:FULL SPEED D:STOP E:STATUS Q:QUIT")
        command = input("What is your command: ")
        print()

        if command.lower() == "a":
            if canteen >= 6:
                print("You Took A Drink Of Water")
                canteen -= 1
                thirst = 0
            else:
                print("You Have No More Water Left, Find An Oasis")
        elif command.lower() == "b":
            print("You Moved Ahead At Moderate Speed")
            miles_travelled += random.randrange(7, 16)
            behind += random.randrange(10, 16)
            camel_tire += 1
            days += 1
        elif command.lower() == "c":
            print(" You Moved Ahead At Full Speed")
            miles_travelled += random.randrange(12, 21)
            behind += random.randrange(10, 16)
            camel_tire += random.randrange(1, 4)
            days += 1
        elif command.lower() == "d":
            print("You Stopped For The Night")
            miles_travelled += 0
            behind += random.randrange(10, 16)
            camel_tire = 0
            days += 1
        elif command.lower() == "e":
            print("Status:")
            print("Miles Traveled: ", miles_travelled)
            print("")
        elif command.lower() == "q":
            dead = True
            print("You Quit")
            print()

        if miles_travelled == behind:
            print("They Have Caught Up To You,")
            print("You Weren't Fast Enough, Your Bones Now Are Scatted Across The Dessert")
            dead = True
        elif abs(miles_travelled - behind) <= 15:
            print("The Aliens Are Close Behind")
        if camel_tire >= 10:
            print("Your Camel Died Of Exhaustion,")
            print("They Find You, And Now Yours and Your Camels Bones Are Scatted Across The Desert")
            dead = True
        elif thirst >= 3:
            print("You Died Of Thirst,")
            print("Your Body Lays In The Sand, Your Body Now Belongs To The Dessert")
            dead = True
        elif miles_travelled >= 200:
            win = True
            print("You Have Traveled 200 Miles")
            print("You Have Reached The Base ")
    '''If Win'''
    if win:
        print()
        print(",")
        print("Want To Try Your Luck Again?")
        replay1 = input("1 To Replay | 2 To Quit")
        if replay1 == "1":
            print()
            print("You've Chosen To Play Again")
            print("Good Luck")
            print()
            dead = False
            miles_travelled = 0
            thirst = 0
            camel_tire = 0
            canteen = 6
            behind = -20
        elif replay1 == "2":
            done = True
            print()
            print()

    '''If Dead'''
    if dead:
        'End screens'
        print()
        print("Want To Try Your Luck Again?")
        replay = input("1 To Replay | 2 To Stay Dead: ")
        if replay == "1":
            print()
            print("You've Chosen To Play Again")
            print("Better Luck This Time")
            print()
            dead = False
            miles_travelled = 0
            thirst = 0
            camel_tire = 0
            canteen = 6
            behind = -20
        elif replay == "2":
            done = True
            print("<-_------______------______-----__->")
            print(" >  HERE LIES A FOOLISH TRAVELER   <")
            print("<__-----________----________---____>")
            print("             _______")
            print("            |       |")
            print("            |  RIP  |")
            print("            |       |")
            print("          ''''''''''''' ")
    print()
print("The Game Is Over")
print("Was That Fun?")
