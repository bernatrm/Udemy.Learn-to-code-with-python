# Define an only_evens function that accepts a list of numbers. 
# It should return a new list consisting of only the even numbers from the original list.
#
# EXAMPLES
# only_evens([4, 8, 15, 16, 23, 42]) => [4, 8, 16, 42]
# only_evens([1, 3, 5])              => []
# only_evens([])                     => []
def only_evens(numbers) -> list:
    evens = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return evens

print("only_evens.py")
print(only_evens([4, 8, 15, 16, 23, 42]) == [4, 8, 16, 42])
print(only_evens([1, 3, 5]) == [])
print(only_evens([]) == [])
print()

# Define a long_strings function that accepts a list of strings. 
# It should return a new list consisting of only the strings that have 5 characters or more.
#
# EXAMPLES
# long_strings(["Hello", "Goodbye", "Sam"])  => ["Hello", "Goodbye"]
# long_strings(["Ace", "Cat", "Job"])        => []
# long_strings([])                           => []
def long_strings(strings) -> list:
    five_or_more = []
    for string in strings:
        if len(string) >= 5:
            five_or_more.append(string)
    return five_or_more

print("long_strings.py")
print(long_strings(["Hello", "Goodbye", "Sam"]) == ["Hello", "Goodbye"])
print(long_strings(["Ace", "Cat", "Job"]) == [])
print(long_strings([]) == [])
print()