units = ["meter", "kilogram", "second", "ampere", "kelvin", "candela", "mole"]

more_units = units.copy() # Creates new object, only works with simple objects

print(units)
print(more_units) # It's a new object not a pointer, total separate objects

same_units = units # Two pointers to the same object
units.remove("kelvin")
print(units)
print(more_units)
print(same_units)

even_more_units = units[:] # same operation than list.copy()
print(even_more_units)