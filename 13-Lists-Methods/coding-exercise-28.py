# Define a nested_sum function that accepts a list of lists of numbers
# The function should return the sum of the values
# The list may contain empty lists
#
# EXAMPLES
# nested_sum([[1, 2, 3], [4, 5]])            => 15
# nested_sum([[1, 2, 3], [], [], [4], [5]])  => 15
# nested_sum([[]])                           => 0
def nested_sum(lists_of_numbers):
    result = 0
    for lists in lists_of_numbers:
        if len(lists) == 0:
            continue
        for number in lists:
            result += number
    return result

print("nested_sum")
print(nested_sum([[1, 2, 3], [4, 5]]) == 15)
print(nested_sum([[1, 2, 3], [], [], [4], [5]]) == 15)
print(nested_sum([[]]) == 0)
print()

def nested_sum_solution(lists_of_numbers):
    result = 0
    for lists in lists_of_numbers:
        for number in lists:
            result += number
    return result

print("nested_sum_solution")
print(nested_sum_solution([[1, 2, 3], [4, 5]]) == 15)
print(nested_sum_solution([[1, 2, 3], [], [], [4], [5]]) == 15)
print(nested_sum_solution([[]]) == 0)
print()

# Define a fancy_concatenate function that accepts a list of lists of strings
# The function should return a concatenated string
# The strings in a list should only be concatenated if the length of the list is 3
#
# EXAMPLES
# fancy_concatenate([["A", "B", "C"]])                        => "ABC"
# fancy_concatenate([["A", "B", "C"], ["D", "E", "F"]])       => "ABCDEF"
# fancy_concatenate([["A", "B", "C"], ["D", "E", "F", "G"]])  => "ABC"
# fancy_concatenate([["A", "B", "C"], ["D", "E"]])            => "ABC"
# fancy_concatenate([["A", "B"], ["C", "D"]])                 => ""
def fancy_concatenate(lists_of_stings):
    result = ""
    for lists in lists_of_stings:
        if len(lists) == 3:
            for string in lists:
                result += string
    return result

print("fancy_concatenate")
print(fancy_concatenate([["A", "B", "C"]]) == "ABC")
print(fancy_concatenate([["A", "B", "C"], ["D", "E", "F"]]) == "ABCDEF")
print(fancy_concatenate([["A", "B", "C"], ["D", "E", "F", "G"]]) == "ABC")
print(fancy_concatenate([["A", "B", "C"], ["D", "E"]]) == "ABC")
print(fancy_concatenate([["A", "B"], ["C", "D"]]) == "")