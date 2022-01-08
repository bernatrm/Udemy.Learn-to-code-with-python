class Example():
    data = "Class attribute!"


e1 = Example()
e2 = Example()
print(e1.data)
print(e2.data)

e1.data = "Instance attribute!"
print(e1.data) # prints instance attribute
print(e2.data) # prints class attribute

del e1.data # We remove instance attribute data, not class attribute
print(e1.data) # As we had removed instance attribte it returns class attribute
print(e2.data)

# print(e1.nonsense)