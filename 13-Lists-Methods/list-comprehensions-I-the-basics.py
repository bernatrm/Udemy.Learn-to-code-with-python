numbers = [3, 4, 5, 6, 7]
# squares = []

# for number in numbers:
#     squares.append(number ** 2)

# print(squares)
# print(number) # The scope es all function

squares = [number ** 2 for number in numbers]
print(squares)
# print(number) # The scope is only running line

rivers = ["Amazon", "Nile", "Yangtze" ]
print([len(river) for river in rivers])

expressions = ["lol", "rofl", "lmao"]
print([experssion.upper() for experssion in expressions])

decimals = [4.95, 3.28, 1.08]
print([int(decimal) for decimal in decimals])