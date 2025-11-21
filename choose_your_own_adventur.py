print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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

player_decision = input("Which path will you take? Type 'Left' or 'Right' to continue.")
if player_decision == "Left":
    player_decision = input("You continue on your path, only to be stopped by a body of water. You could elect to swim "
                            "across it, or wait for enough debris to flow down into the water to negotiate it. "
                            "Choose 'Swim' or 'Wait' to continue.")
    if player_decision == "Wait":
        player_decision = input("Some time passes, and eventually, enough debris accumulates that you can use to cross "
                                "the water. You travel further and come across a stone wall lined with three of different"
                                " colors: Red, Yellow and Blue. Which door do you enter?")
        if player_decision == "Yellow":
            print("Victory is yours! You've found the treasure chest and claim your prize.")
        elif player_decision == "Red":
            print("How unlucky. Upon opening the door, you get sucked into a portal that transports you to Hell, where"
                  "you are forced to burn for all eternity. Game over.")
        elif player_decision == "Blue":
            print("Curiously, as you enter the door, it looks as though you've entered another forest, and the door"
                  "behind you has disappeared. You explore deeper into the forest, only to be set upon by a pack of"
                  "feral bears, where they tear you limb from limb and eat you alive. Game over.")
        else:
            print("You didn't make a valid choice. Game over.")
    else:
        print("You try to swim, and to your horror, realize that the water is infested with man eating piranhas. Game over.")
else:
    print("As you take your first step, you realize all too late that you've begun to fall into a bottomless chasm."
          "Game over.")
