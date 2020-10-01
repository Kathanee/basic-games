print("Want to know which profession is suitable for you?")
print("Answe few questions to know the best profession for you")
list=['a','b']

user_choice=input("What do you like the most\n a.Staing at home \t b.Staying outside\n")
if user_choice=='a':
    user_choice_a = input("Are you more on to\n a.Playing mobile games\t b.Programming\n")
    if user_choice_a=='a':
        user_choice_a_a=input("How do you choose a game\n a.By seeing the animation\t b.By seeing the complexcity\n")
        if user_choice_a_a=='a':
            print("You should be a Animator")
        elif user_choice_a_a=='b':
            print("You should be a Game developer")
        else:print("Invalid choice!Try again\n Enter either 'a' or 'b' ")
    elif user_choice_a=='b':
        user_choice_a_b=input("What kind of programs do you like\n a.program for solving problem\t b.Program for designing\n")
        if user_choice_a_b=='a':
            print("You should be a Software developer")
        elif user_choice_a_b=='b':
            print("You should be a Web designer")
        else: print("Invalid choice!Try again\n Enter either 'a' or 'b' ")
    else:print("Invalid choice!Try again\n Enter either 'a' or 'b' ")
elif user_choice=='b':
    user_choice_b=input("Are you more on to\n a.Sports\t b.Travelling\n")
    if user_choice_b=='a':
        user_choice_b_a=input("What do you enjoy the most between\n a.Playing sports b.Exercising in a Gym\n")
        if user_choice_b_a=='a':
            print("You should be a Sportsperson")
        elif user_choice_b_a=='b':
            print("You should be a Bodybuilder")
        else:print("Invalid choice!Try again\n Enter either 'a' or 'b' ")
    elif user_choice_b=='b':
        user_choice_b_b=input("Whilst travelling do you like to\n a.Explore different Culture or b.Helping out people\n")
        if user_choice_b_b=='a':
            print("You should be a Travel blogger")
        elif user_choice_b_b=='b':
            print("You should be a Social worker")
        else:print("Invalid choice!Try again\n Enter either 'a' or 'b' ")
else:print("Invalid choice!Try again\n Enter either 'a' or 'b' ")