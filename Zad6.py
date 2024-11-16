def process_lists(lst1, lst2):
    result = list(set(lst1 + lst2))
    result = [x ** 3 for x in result]
    return result


list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

result = process_lists(list1, list2)
print(result)
