def list_ends(a):
    new_list = []
    new_list.append(a[0])
    new_list.append(a[-1])
    return new_list

a = [5, 10, 15 , 20]
print(list_ends(a))