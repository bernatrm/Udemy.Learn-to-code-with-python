students = ["Bob", "Sally", "Sue"]
athletes = students
nerds = ["Bob", "Sally", "Sue"]

print(students == athletes) # Equality
print(students == nerds)

print(students is athletes) # Identity = True
print(students is nerds) # Identity = False

a = 1
b = 1
print(a == 1)
print(a is b)

a = 3.14
b = 3.14
print(a == b)
print(a is b)

a = "Hello"
b = "Hello"
print(a == b)
print(a is b)
