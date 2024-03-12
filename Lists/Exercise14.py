def loop_list():
    a = [1, 2, 2, 3, 4, 5, 6, 7, 7, 8]
    new_list = []
    for num in a:
        if num not in new_list:
            new_list.append(num)
    print(new_list)

def set_list():
    a = [1, 2, 2, 3, 4, 5, 6, 7, 7, 8]
    print(set(a))

loop_list()
set_list()
    