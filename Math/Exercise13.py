def get_num():
    return int(input("Give me a number to do Fibonnaci sequence: "))

def fibonnaci():
    num = get_num()
    i = 1
    fib_list = []
    if num == 0:
        fib_list = []
    elif num == 1:
        fib_list = [1]
    elif num == 2:
        fib_list = [1, 1]
    elif num > 2:
        fib_list = [1, 1]
        while i < (num - 1):
            fib_list.append(fib_list[i] + fib_list[i - 1])
            i += 1
    print(fib_list)

fibonnaci()
