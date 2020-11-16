stick_num = int(input("How many sticks to start with? (10-100)? "))
while stick_num <10:
    print("Sorry, that's too few sticks. Try again.")
    print()
    stick_num = int(input("How many sticks to start with? (10-100)? "))

while stick_num >100:
    print("Sorry, that's too many sticks. Try again.")
    print()
    stick_num = int(input("How many sticks to start with? (10-100)? "))

else:
    print("Great, let's play . . .")
    print()

a = "Player 1"
b = "Player 2"
player = a
    
while stick_num >0:
    print("Turn:",player)
    print("There are",stick_num,"on the table.")
    take = int(input("How many sticks do you want to take (1, 2 or 3)? "))
    while take<1 or take>3:
        print("Sorry, that's not a valid number.")
        print()
        print("Turn:",player)
        print("There are",stick_num,"on the table.")
        take = int(input("How many sticks do you want to take (1, 2 or 3)? "))
    while stick_num < take:
        print("Sorry, that's not a valid number.")
        print()
        print("Turn:",player)
        print("There are",stick_num,"on the table.")
        take = int(input("How many sticks do you want to take (1, 2 or 3)? "))
    if player == a:
        player = b
    elif player ==b:
        player = a
    print()
    stick_num -= take
   
        
if stick_num==0:
        print()
        print("There are no sticks left on the table. Game over.")
        print(player,"wins!")
    
