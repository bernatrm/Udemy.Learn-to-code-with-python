a = 3 # immutable object
b = a

a = 5
print(a) # prints 5
print(b) # still prints 3 because reference an immutable object

a = [1, 2, 3]
b = a
a.append(4)
print(a) 
print(b) # Reference the same object [1, 2, 3, 4]

b.append(5)
print(a)
print(b)