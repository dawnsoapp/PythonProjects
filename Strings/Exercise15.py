def backwards():
    user_string = input("Type in a sentence: ")
    split = user_string.split()
    reverse = split[::-1]
    new_string = ' '.join(map(str, reverse))
    print(new_string)

backwards()