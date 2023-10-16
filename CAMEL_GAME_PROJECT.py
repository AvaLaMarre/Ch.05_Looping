'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
# PRE GAME KNOWLEDGE
print("Camel")
print("Welcome to Camel. The Object is to travel 200 Miles across the Great Gobi Dessert.")
print("A tribe of jhuihiujhuhu will be chasing you.")
print("You will be asked for commands every so often")
print()
print()
print("C  O  M  M  A  N  D  S:")
print("A. DRINK from your canteen")
print("B. MODERATE SPEED ahead")
print("C. FULL SPEED ahead")
print("D. STOP for the night")
print("E. STATUS check")
print("Q. QUIT")
print()
print()
print("You will have 1 quart of water which will last you six drinks.")
print("You may renew your water supply completely at an oases.")
print("Good Luck and good cameling!!")
# end of pre game

done = False
miles_travelled = 0
thirst = 0
camel_tire = 0
canteen = 6
behind = -20

while done == False:
    print("You are in the middle of the desert at an oasis.")
    print()
    print("You have travelled ", miles_travelled, " miles all together")
    print("A:DRINK B:MODERATE SPEED C:FULL SPEED D:STOP E:STATUS Q:QUIT")
    command = input("What is your command: ")
    print()

    if command.lower() == "a":
        print("You took a drink of water")
    elif command.lower() == "b":
        print("You moved ahead at moderate speed")
    elif command.lower() == "c":
        print(" You moved ahead at full speed")
    elif command.lower() == "d":
        print("You stopped for the night")
    elif command.lower() == "e":
        print("Status")
    elif command.lower() == "q":
        done = True
        print("You Quit")
        print()

    if miles_travelled == behind:
        pass

    #End screens
    print()
    print()
    print("Want to try your luck again?")
    replay = input("1 To Replay | 2 To Stay Dead: ")
    if replay == "1":
            done = False
    else:
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
print("Was that fun?")
