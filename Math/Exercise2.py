# Exercise 1
num = int(input("What number is divisible by 2? "))

def divideNum(num):
    if (num % 4 == 0):
        print("This number is also divisible by 4!")
    if (num % 2 == 0):
        total = (num / 2)
        return total
    else:
        return print("That number is odd!")
new_num = divideNum(num)
if new_num == None:
    print("That would make a whacky decimal.")
else:
    print(new_num)

num2 = int(input("Now select another number "))
check = int(input("And another to divide it by! "))

def customDivide(num2, check):
    total = num2 / check
    return total
result = customDivide(num2, check)
print(result)