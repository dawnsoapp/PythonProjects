import random

def QuitGame(user_input):
    if user_input == "exit":
            print("Thanks for playing!")
            return False

def GuessLoop(user_num, num, counter):
    while user_num != num:
        if user_num > num:
            counter += 1
            user_input = input("Too high! Try again: ")
            user_num = int(user_input)
        elif user_num < num:
            counter += 1
            user_input = input("Too low! Try again: ")
            user_num = int(user_input)
        elif user_input == "exit":
            QuitGame(user_input)
    return user_num, counter
        

def GuessingGame():
    while True:
        user_input = input("Guess a number between 1-9!\n" 
                            "If you want to quit at any time, type 'exit.'\n"
                            "Alright, I have my number! Guess what it is: ")
        num = random.randint(1, 9)
        counter = 0
        if user_input != "exit":
            user_num = int(user_input)
        else:
            QuitGame(user_input)
            break
        num_count = GuessLoop(user_num, num, counter)
        user_num = num_count[0]
        counter = num_count[1]
        if user_num == num:
            repeat = input(f"You got it! It took {counter} tries! Want to play again?\n"
                        "Type yes if so, or exit if you wish to stop: ")
            if repeat == "yes":
                continue
            else:
                QuitGame(repeat)
                break

GuessingGame()