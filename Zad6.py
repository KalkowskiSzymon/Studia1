def process_lists(lst1, lst2):
    processed_result = list(set(lst1 + lst2))
    processed_result = [x**3 for x in processed_result]
    return processed_result


list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

result = process_lists(list1, list2)
print(result)
