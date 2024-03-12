word = input("Please enter a word: ")

def palindrome(word):
    n = 0
    end = len(word) - 1
    while n <= end:
        if word[n] == word[end]:
            n += 1
            end -= 1
            continue 
        else:
            print("This word is not a palindrome.")
            return False
    print("This word is a palindrome!")
    return True

palindrome(word)

# another solution: reversal string
# using reverse = word[::-1] to create the reverse of the string entered 
# compare the word string and the reverse string if they are the same or not