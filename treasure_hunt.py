#Treasure Island game.
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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to the treasure Island. Your mission is to find the treasure.")
print("You are at a cross road. Where do you want to go?")
print(' Type "left" or "right"')
dir = input()
if dir == "left" or dir == "Left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    print(' Type "wait" to wait for a boat. Type "swim" to swim across.')
    act = input()
    if act == "wait" or act == "Wait":
        print("You've come across the lake. There are some doors across the lake.")
        print(' Type "Red" to open red door. "Blue" to open blue door. "Yellow" to open yellow door')
        door = input()
        if door == "Yellow" or door == "yellow":
            print("You Win!")
        elif door == "Red" or door == "red":
            print("Game Over.")
        elif door == "Blue" or door == "blue":
            print("Game Over.")
        else:
            print("Invalid Input!")
    elif act == "swim" or act == "Swim":
        print("Game Over.")
    else:
        print("Invalid Input!")
elif dir == "right" or dir == "Right":
    print("Game Over.")
else:
    print("Invalid Input!")
