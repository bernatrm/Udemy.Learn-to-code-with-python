# Declare a length_match function that accepts a list of strings and an integer.
# It should return a count of the number of strings whose length is equal to the number.
#
# EXAMPLES
# length_match(["cat", "dog", "kangaroo", "mouse"], 3))  => 2
# length_match(["cat", "dog", "kangaroo", "mouse"], 5))  => 1
# length_match(["cat", "dog", "kangaroo", "mouse"], 4))  => 0
# length_match([], 5))                                   => 0
def length_match(elements, length) -> int:
    total = 0
    for element in elements:
        if len(element) == length:
            total += 1
    return total


print("length_match.py")
print(length_match(["cat", "dog", "kangaroo", "mouse"], 3) == 2)
print(length_match(["cat", "dog", "kangaroo", "mouse"], 5) == 1)
print(length_match(["cat", "dog", "kangaroo", "mouse"], 4) == 0)
print(length_match([], 5) == 0)
print()

# Declare a sum_from function that accepts two numbers as arguments.
# The second number will always be greater than the first number.
# The function should return the sum of all numbers from the first number to the second number (inclusive).
#
# EXAMPLES
# sum_from(1, 2)   # 1 + 2                  => 3
# sum_from(1, 5)   # 1 + 2 + 3 + 4 + 5      => 15
# sum_from(3, 8)   # 3 + 4 + 5 + 6 + 7 + 8  => 33
# sum_from(9, 12)  # 9 + 10 + 11 + 12       => 42


def sum_from(start, end) -> int:
    total = 0
    while start <= end:
        total += start
        start += 1
    return total


print("sum_from.py")
print(sum_from(1, 2) == 3)
print(sum_from(1, 5) == 15)
print(sum_from(3, 8) == 33)
print(sum_from(9, 12) == 42)
print()

def sum_from_solution(start, end) -> int:
    total = 0
    for number in range(start, end + 1):
        total += number
    return total


print("sum_from_solution.py")
print(sum_from_solution(1, 2) == 3)
print(sum_from_solution(1, 5) == 15)
print(sum_from_solution(3, 8) == 33)
print(sum_from_solution(9, 12) == 42)
print()

# Declare a same_index_values function that accepts two lists.
# The function should return a list of the index positions in which the two lists have equal elements
#
# EXAMPLES
# same_index_values([1, 2, 3], [3, 2, 1])                         => [1]
# same_index_values(["a", "b", "c", "d"], ["c", "b", "a", "d"])   => [1, 3]
def same_index_values(left_elements, right_elements) -> list:
    if len(left_elements) < len(right_elements):
        number_of_values = len(left_elements)
    else:
        number_of_values = len(right_elements)
    index_values = []
    index = 0
    while index < number_of_values:
        if left_elements[index] == right_elements[index]:
            index_values.append(index)
        index += 1
    return index_values

print("same_index_values.py")
print(same_index_values([1, 2, 3], [3, 2, 1]) == [1])
print(same_index_values(["a", "b", "c", "d"], ["c", "b", "a", "d"]) == [1, 3])
print()

def same_index_values_solution(left_elements, right_elements) -> list:
    index_values = []
    for index, value in enumerate(left_elements):
        if value == right_elements[index]:
            index_values.append(index)
    return index_values

print("same_index_values_solution.py")
print(same_index_values_solution([1, 2, 3], [3, 2, 1]) == [1])
print(same_index_values_solution(["a", "b", "c", "d"], ["c", "b", "a", "d"]) == [1, 3])
print()