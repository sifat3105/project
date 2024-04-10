import pyfiglet
import random

while True:
    user_choice = input("Enter Your Choice: Rock, Paper, and Scissors :")
    computer_choice = random.randint(0,2)
    choice_list = ['Rock', 'Paper', 'Scissors']
    # print computer choice
    print_computer_choice = choice_list[computer_choice]
    big_text = pyfiglet.figlet_format(print_computer_choice, font="big")
    print("{:*^40}".format(" " + "Computer choice" + " "))
    print(big_text)
    
    # convert str to number
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
    
    # print user choice
    print_user_choice = choice_list[user_choice]
    big_text = pyfiglet.figlet_format(print_user_choice, font="big")
    print("{:*^40}".format(" " + "User choice" + " "))
    print(big_text)

    # get result
    if user_choice == computer_choice:
        result ="It's    a    Drow"
    elif user_choice == 0 and computer_choice == 2:
        result = "You    Win"
    elif user_choice == 2 and computer_choice == 0:
        result = "You    lose"
    elif user_choice < computer_choice:
        result = "You    lose"
    elif user_choice > computer_choice:
        result = "You    Win"
    # print result  
    big_text = pyfiglet.figlet_format(result, font="big")
    print("=" *40)
    print(big_text)
    
    #asking for play again
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again == 'no':
        print("Exiting the game.")
        break
    
