Guests = {
        "Margaret": 23,
        "Steven": 27,
        "Isabelle": 34,
        "Stanley": 52,
        "Rodger": 37
        }



user_input = input("Welcome to Hotel DeBour! Are you here to check in? Yes or No?\n")

if user_input == str.lower("Yes") or str.upper("Yes"):
    user_name = input("Wonderful! Can I get your name?\n")
    user_age = int(input("And how old are you?\n"))
    if user_age < 18:
        print("Sorry, but you need a parent or guardian to rent a room with.\n"
        "We are not allowed to accept guests under the age of 18 to rent\n"
        "a hotel room.")
    else:
        Guests[f"{user_name}"] = user_age
        print(Guests)
else:
    print("Oh, that's a shame. Have a nice day!")


