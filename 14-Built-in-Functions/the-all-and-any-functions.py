print(all([True])) # Returns True if all of the elements are True or Blank
print(all([True, True, True]))
print(all([True, True, False]))
print(all([1, 2, 3]))
print(all([1, 2, 3, 0]))
print(all(["a", "b"]))
print(all(["a", "b", ""]))
print(all([]))

print(any([True, False])) # Returns True if any of the elements is True
print(any([False, False]))
print(any([0, 1]))
print(any([0]))
print(any([" ", ""]))
print(any([""]))
print(any([]))