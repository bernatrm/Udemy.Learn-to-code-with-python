def product(a, b):
    return a * b

# print(product(3, 5))

numbers = [3, 5]
numbers = (3, 5)

print(product(*numbers)) # Expand the values of the tuple / list

print(dir([3, 5]))