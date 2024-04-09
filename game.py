import random
user_choice = input("Enter Your Choice: R for Rock, P for Paper, and S for Scissors")
computer_choice = random.randint(0,2)

if user_choice == computer_choice:
    print("It's a Diow")
elif user_choice == 0 and computer_choice == 2:
    print("You Win")
elif user_choice == 2 and computer_choice == 0:
    print("You lose")
elif user_choice < computer_choice:
    print("you lose")
elif user_choice > computer_choice:
    print("you win")
else:
    print("Please Enter Your Choice in 'R' 'P' 'S'")
