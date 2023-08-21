print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
decision1 = input("You stand in front of two roads, would you go left or right? (L/R) ")
if decision1 == "L" or decision1 == "l":
    decision2 = input("At the end of the road you found a lake and across it there's a huge golden door, would you swim or wait? (S/W) ")
    if decision2 == "W" or decision2 == "w":
        decision3 = input("After a few seconds of waiting a wall to your left opened up, when you went inside you found 3 doors: Red, Blue, and Yellow, which would you choose? (R/B/Y) ")
        if decision3 == 'R' or decision3 =='r':
            print("As you entered the room the door closed behind you and flames began to rise from every corner, you were burnt. GAME OVER. ")
        elif decision3 == "B" or decision3 == 'b':
            print("You entered the room and started hearing weird voices'Grrr! Grrr!' getting closer, as you lit your torch you found yourself surrounded by beasts, you were eaten. GAME OVER.")
        elif decision3 == "Y" or decision3 == 'y':
            print("There was something glowing brightly in the center of the room, you kept approaching slowly until you found a box made of gold, it was the treasure filled with jewelry. Congrats, You WIN!!.")
        else:
            print("You didn't choose any of the rooms and kept standing until the snakes surrounded your legs and they attacked you, you died. GAME OVER. (Honestly though, what were you thinking just roaming around?)")
    elif decision2 == "S" or decision2 == 's':
        print("As soon as you jumped into the lake you saw a swarm of pirhanas rushing towards you, you were eaten. GAME OVER.")
    else:
        print("You stayed still until a venomous snake bit your leg, you lost control, and fell into the lake. GAME OVER. (Just give a real choice ok?)")
elif decision1 == "R" or decision1 == 'r':
    print("There was a hole at the end of the road, you fell and died. GAME OVER.")
else:
    print("You stood there taking so long to think what to choose until a crocodile appeared from behind and attacked you, you died. GAME OVER. (Umm, Why?)")

input(" ")
