# Declare an invert function that accepts a dictionary object. 
# The function should return a new dictionary where the keys and values from the original dictionary are inverted. 
# Each key should now be a value, and each value should be a key. 
# Assume both the keys and values of the dictionary are immutable.
#
# EXAMPLE:
# my_dict = {
#   "A": "B", 
#   "C": "D",
#   "E": "F"
# }
#
# invert(my_dict) => {'B': 'A', 'D': 'C', 'F': 'E'}
def invert(elements):
    inverted = {}
    for key, value in elements.items():
        inverted[value] = key
    return inverted

print("invert")
my_dict = {
  "A": "B", 
  "C": "D",
  "E": "F"
}
print(invert(my_dict) == {'B': 'A', 'D': 'C', 'F': 'E'})
print()

# Declare a count_of_value function that accepts a dictionary and an integer.
# It should return a count of the number of times the integer appears 
# as a value among the dictionary’s values.
#
# EXAMPLE:
# my_dict = { "a" : 5, "b" : 3, "c" : 5 }
#
# count_of_value(my_dict, 5) => 2
# count_of_value(my_dict, 3) => 1
def count_of_value(dictionary, value):
    count = 0
    for _, element in dictionary.items():
        if element == value:
            count +=1
    return count

print("count_of_value")
my_dict = { "a" : 5, "b" : 3, "c" : 5 }

print(count_of_value(my_dict, 5) == 2)
print(count_of_value(my_dict, 3) == 1)
print()

# Declare a sum_of_values function that accepts a dictionary and a list of strings.
# The dictionary will have keys of strings and values of numbers.
#
# The function should return the sum of values for dictionary 
# keys that are also found in the list.
#
# NOTE: sum is a reserved keyword in Python. Don’t use it as a variable name.
#
# EXAMPLES:
# my_dict = { "a": 5, "b": 3, "c": 10 }
#
# sum_of_values(my_dict, ["a"])            => 5
# sum_of_values(my_dict, ["a", "c"])       => 15
# sum_of_values(my_dict, ["a", "c", "b"])  => 18
# sum_of_values(my_dict, ["z"])            => 0
def sum_of_values(dictionary, elements):
    result = 0
    for element in elements:
        if dictionary.get(element):
            result += dictionary[element]
    return result

print("sum_of_values")
my_dict = { "a": 5, "b": 3, "c": 10 }

print(sum_of_values(my_dict, ["a"]) == 5)
print(sum_of_values(my_dict, ["a", "c"]) == 15)
print(sum_of_values(my_dict, ["a", "c", "b"]) == 18)
print(sum_of_values(my_dict, ["z"]) == 0)
print()