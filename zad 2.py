# A
def display_names(names):
    for name in names:
        print(name)


display_names(["Anna", "Piotr", "Kasia", "Marek", "Tomek"])


# B
def multiply_by_two_loop(numbers):
    result = []
    for num in numbers:
        result.append(num * 2)
    return result


print(multiply_by_two_loop([1, 2, 3, 4, 5]))


def multiply_by_two_comprehension(numbers):
    return [num * 2 for num in numbers]


print(multiply_by_two_comprehension([1, 2, 3, 4, 5]))


# C
def display_even_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(number)


display_even_numbers(range(10))

# D


def display_every_second(numbers):
    for i in range(0, len(numbers), 2):
        print(numbers[i])


display_every_second(range(10))
