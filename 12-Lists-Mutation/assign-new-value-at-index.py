crayons = ["Macaroni and Cheese", "Maximum Yellow Red", "Jazzberry Jam"]
print(crayons)

crayons[1] = "Cotton Candy"
print(crayons)

crayons[0] = "Blizzard Blue"
print(crayons)

crayons[-1] = "Aquamarine"
print(crayons)

# Will produce an Index Error, we only can modify actual indexes, but not add new ones
# crayons[3] = "Aztec Gold" 