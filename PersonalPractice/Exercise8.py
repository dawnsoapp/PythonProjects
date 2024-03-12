import random

def Game():
    while True:
        user = input("rock, paper or scissors? ")
        computer = random.randint(1,3)
        if user == "scissors" and computer == 1:
            print("I had rock! You lose.")
        elif computer == 2:
            print("I had paper. You win!")
        elif computer == 3:
            print("It's a tie! Let's go again!")
            continue
        if user == "paper" and computer == 1:
            print("I had rock. You win!")
        elif computer == 2:
            print("It's a tie! Let's go again!")
            continue
        elif computer == 3:
            print("I had scissors! You lose.")
        if user == "rock" and computer == 2:
            print("I had paper! You lose.")
        elif computer == 1:
            print("It's a tie! Let's go again!")
            continue
        elif computer == 3:
            print("I had scissors. You win!")

        choice = input("Do you want to play again? ")
        if choice == "yes":
            continue
        else:
            print("Thanks for playing!")
            return False 

Game()

