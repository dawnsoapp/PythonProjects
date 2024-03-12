# Take two lists and write a program that returns a list that contains only 
# the elements that are common between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def commonNums (list1, list2):
    map = {}
    common_list = []
    # get map of key, values for list1
    for item in list1:
        if item not in map:
            map[item] = 1
        else:
            map[item] += 1
    # get map of values for list2
    for item in list2:
        if item not in map:
            map[item] = 1
        else:
            map[item] += 1
    #sort via dict for numbers then append in new list
    for key in map:
        if map[key] >=2:
            common_list.append(key)
    return common_list

result = commonNums(a, b)
print(result)

# another quick solution from online
new_list = [] 
for i in a:
    if i in b and i not in new_list:
        new_list.append(i)
print(new_list)

# and another
print (list(set(a) & set(b)))

