foods = "Shushi", "Steak", "Guacamole"
foods = ("Shushi", "Steak", "Guacamole") # Best practice but both are tuples

print(type(foods))

empty = () # Empty tuple
print(type(empty))

mystery = (1)
print(type(mystery))

mystery = (1, ) # Tuple with only one element
print(type(mystery))

print(tuple(["Shushi", "Steak", "Guacamole"]))
print(type(tuple(["Shushi", "Steak", "Guacamole"])))

print(tuple("abc"))
print(tuple(["abc"]))