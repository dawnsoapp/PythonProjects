def get_num():
    return int(input("Type in a number: "))

def calculator(num):
    divisor_list = []
    num_range = list(range(1, num + 1))
    for n in num_range:
        if num % n == 0:
            divisor_list.append(num)
    if len(divisor_list) == 2:
        return True
    else:
        return False

def guess_prime():
    num = get_num()
    check = calculator(num)
    if check == True:
        print("This is a prime number!")
    else:
        print("This is not a prime number!")

guess_prime()
