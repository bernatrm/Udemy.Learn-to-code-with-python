# Declare a right_words function that accepts a list of words and a number.
# Return a new list with the words that have a length equal to the number.
# Do NOT use list comprehension.
#
# EXAMPLES:
# right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 3)     => ['cat', 'dog', 'ace']
# right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 5)     => ['heart']
# right_words([], 4)                                         => []
def right_words(words, word_length):
    return list(filter(lambda word: len(word) == word_length ,words))

print("right_words")
print(right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 3) == ['cat', 'dog', 'ace'])
print(right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 5) == ['heart'])
print(right_words([], 4) == [])
print()

# Declare an only_odds function.
# It should accept a list of whole numbers.
# It should return a list with only the odd numbers from the original list.
# Do NOT use list comprehension.
#
# EXAMPLES:
# only_odds([1, 3, 5, 6, 7, 8])      =>  [1, 3, 5, 7]
# only_odds([2, 4, 6, 8])            =>  []
def only_odds(numbers):
    return list(filter(lambda number: number % 2 == 1,numbers))

print("only_odd")
print(only_odds([1, 3, 5, 6, 7, 8]) == [1, 3, 5, 7])
print(only_odds([2, 4, 6, 8]) == [])
print()

# Declare a count_of_a function that accepts a list of strings.
# It should return a list with counts of how many “a” characters appear per string.
# Do NOT use list comprehension.
#
# EXAMPLES:
# count_of_a(["alligator", "aardvark", "albatross"])    => [2, 3, 2]
# count_of_a(["plywood"])                               => [0]
# count_of_a([])                                        => []
def count_of_a(strings):
    return list(map(lambda string: string.count("a"),strings))

print("count_of_a")
print(count_of_a(["alligator", "aardvark", "albatross"]) == [2, 3, 2])
print(count_of_a(["plywood"]) == [0])
print(count_of_a([]) == [])
print()