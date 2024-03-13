import random
import string

def create_username():
    # have user input name for account
    print("Welcome to DawnChecks Create Account. Follow instructions below. \n")
    username = input("Please enter a user name: ")
    return username

def generate_password():
    # allow user to decide if they want a random password
    rand_password = ''
    character_limit = 1
    characters = string.ascii_letters + string.digits + string.punctuation
    stop = 1
    while character_limit <= 12:
        rand_password += ''.join(random.choice(characters))
        character_limit += 1
    return rand_password

def generate_pin(password):
    pin = random.randrange(1000, 9999)
    print(f"Your password: {password} is successful. \n"
            f"Should you ever need to change it, your PIN is: {pin}")
    return pin

def create_password():
    password = ''
    # prompt user a choice for random password or custom
    choice = int(input("Would you like to 1) Customize your password or 2) Generate a random password? \n"
                    "Please type in the number of the choice you would like to make: "))
    # custom
    if choice == 1:
        # prompt user for a password and save in variable
        check = False
        while not check:
            password = input("Please enter a password between 5-12 characters: ")
            if len(password) > 12:
                print("Password exceeds character limit. Please re-enter password.")
                continue
            elif len(password) < 5:
                print("Password does not meet character requirement. Please re-enter password.")
                continue
            else:
                check = True
    # random
    if choice == 2:
        password = generate_password()

    return password

def login_attempts(password):
    # retry opt for failed login attempt
    retry = 0
    request_new = False
    while retry <= 3:
        attempt = input("Please re-enter your password: ")
        if attempt != password:
            retry +=1
            print(f"Invalid input. You have used {retry}/3 attempts.\n")
            if retry == 3:
                break
            request = int(input("Would you like to reset your password? Enter the option number:\n"
                    "1. No, continue attempts\n"
                    "2. Yes\n"
                    ""))
            if request == 1:
                continue
            if request == 2:
                request_new = True
                break
        elif attempt == password:
            break
    print(retry, request_new)
    return [retry, request_new]


def enter_pin():
    return

def new_password(password, pin):
    # allow user to create a new password if they forgot 
    # special: prompt user for 4-digit code to change
    check_pin = int(input("Please provide PIN number here: "))
    attempt = 0 
    while attempt <= 3:
        if check_pin != pin:
            attempt += 1
            print(f"Invalid PIN. You have used {attempt}/3 attempts.")
            continue
        elif check_pin == pin:
            print("PIN successful. Transferring you to update new password.")
            password = create_password()
            break
    return password

def login(username, password, pin):
    # prompt user for username
    print("Welcome to DawnBanks Login. Please Login your credentials here. \n")
    validate_name = input("Username: ")
    print(validate_name)
    # prompt user for password
    validate_password = input("Password: ")
    # if password incorrect, give them option to change
    if validate_name == username and validate_password != password:
        print("Invalid input.\n")
        attempts = login_attempts(password)
        if attempts[0] >= 3:
            print("Sorry. You have exceeded the limit of tries. Please check back later.")
            return
        elif attempts[0] <=2 and attempts[1] == True:
            password = new_password(password, pin)
        elif attempts[0] < 3 and attempts[1] == False:
            print(f"Welcome back {username}!")
        # if password correct, give them a greeting message
    elif validate_name == username and validate_password == password:
            print(f"Welcome back {username}!")

def DawnBanks():   
    # set up menu 
    option = int(input("Welcome to DawnBanks.\n"
        "If you would like to create an account, please enter 1.\n"
        "If you are a returning guess, please enter 2 to sign in.\n"
        "If you wish to exit, please enter 3.\n"
        ""))
    if option == 1:
        username = create_username()
        password = create_password()
        pin = generate_pin(password)
        print("You are all set. Let's sign you in.")
        option = 2
    if option == 2:
        login(username, password)


    # TO-DO LIST
        # figure out how to connect the new password from pin to the official password
        # implement exit option
        # allow for sign outs and logins so option 2 can be used on opening
        
        
        
        
        
        
    
    return

login()
