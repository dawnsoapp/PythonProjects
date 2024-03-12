def ListSorter(list, new_list, checker):
    # n = 0
    new_list = [] 
    # while n < (len(list) - 1):
        # if list[n] <= checker:
            # new_list.append(list[n])
        # n += 1
    for item in list:
        if item <= checker:
            new_list.append(item)
    print(new_list)
    return new_list

ListSorter([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], [], 5)
ListSorter([5, 10, 15, 20, 25, 30], [], 20)
