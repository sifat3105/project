import random
while True:
    user_choice = input("Enter Your Choice: Rock, Paper, and Scissors :")
    computer_choice = random.randint(0,2)
    computer_choice_list = ['Rock', 'Paper', 'Scissors']
    print(f"Computer Choice : {computer_choice_list[computer_choice]}")
    if user_choice[0] == 'R' or user_choice[0] == 'r':
        user_choice = 0
    elif user_choice[0] == 'P' or user_choice[0] == 'p':
        user_choice = 1
    elif user_choice[0] == 'S' or user_choice[0] == 's':
        user_choice = 2
    elif user_choice == 'exit':
        print("Exiting the game.")
        break
    else:
        print("your Choice is Wrong")
        continue    

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
    
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again == 'no':
        print("Exiting the game.")
        break
    
