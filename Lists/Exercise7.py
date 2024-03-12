# work on list comprehension
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even_result = [item for item in a if item % 2 == 0]
odd_result = [item for item in a if item %2 != 0]
print(even_result)
print(odd_result)