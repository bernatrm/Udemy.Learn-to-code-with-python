birthday = (4, 12, 1991)

# print(len(birthday))

# print(birthday[0])
# print(birthday[1])
# print(birthday[2])

# # print(birthday[15]) # Index Error

# print(birthday[-1])
# print(birthday[-1])
# print(birthday[-2])
# print(birthday[-4]) # Index Error

# birthday[1] = 13 # Error Type a tuple is immutable
# however we can change ineternal elements
addresses = (
    ['Hudson Stret', 'New York', 'NY'],
    ['Franklin Stret', 'San Francisco', 'CA']
)

# addresses[1] = ["Something else"] # We can't change the list it selves
addresses[1][0] = "Polk Street" # but we can change the content of the lists
print(addresses)

print(dir(birthday))