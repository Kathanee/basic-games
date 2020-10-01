import random
list=['s','w','g']
print("Welcome to the snake-water-gun Game")
comp_point=0
user_point=0
loop=0

while loop<6:
    user_choice = input("enter your choice \tEnter  s  for Snake\tEnter  w  for Water\tEnter  g  for Gun\n")
    comp_choice = random.choice(list)
    if user_choice==comp_choice:
        comp_point=comp_point=1
        user_point=user_point=1
        print("It's a Tie")
        loop+=1
    else:
        if comp_choice == 's' and user_choice == 'w':
            comp_point = comp_point + 1
            print("COMP WON!!")
        elif comp_choice == 'w' and user_choice == 's':
            user_point = user_point + 1
            print("YOU WON!!")
        elif comp_choice == 's' and user_choice == 'g':
            user_point = user_point + 1
            print("YOU WON!!")
        elif comp_choice == 'g' and user_choice == 's':
            comp_point = comp_point + 1
            print("COMP WON!!")
        elif comp_choice == 'w' and user_choice == 'g':
            comp_point = comp_point + 1
            print("COMP WON!!")
        elif comp_choice == 'g' and user_choice == 'w':
            user_point = user_point + 1
            print("YOU WON!!")
    loop+=1
print("computer point:" %(comp_point))
print("user point:" %(user_point))
if user_point>comp_point:
    print("CONGRATS!!YOU  ARE THE WINNER")
else:
    print("COMP WON!!")

