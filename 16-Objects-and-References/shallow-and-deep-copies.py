import copy

# a = [1, 2, 3]

# b = a[:] # Shadow Copy
# print(a == b)
# print(a is b)

# b = a.copy() # Shadow Copy
# print(a == b)
# print(a is b)

# d = copy.copy(a) # Shadow Copy
# print(a == d)
# print(a is d)

numbers = [2, 3, 4]
a = [1, numbers, 5]

b = a[:]
b = a.copy()
# b = copy.copy(a)
b = copy.deepcopy(a) # All Full objects are duplicated
print(a == b)
print(a is b)
print(a[1] is b[1]) # It's the same list / object

# a[1].append(200)
# print(b) # Prints [1, [2, 3, 4, 200], 5] because the list onindex 1 es the same object

a[1].append(100)
print(b)
print(a)

b[1].append(200)
print(b)
print(a)
