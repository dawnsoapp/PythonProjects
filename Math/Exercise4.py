num = int(input("Pick a number: "))

def findDivisions(num):
    num_list = []
    num_range = range(1, num + 1)
    for item in num_range:
        if num % item == 0:
            num_list.append(item)
    return num_list

result = findDivisions(num)
print(result)
