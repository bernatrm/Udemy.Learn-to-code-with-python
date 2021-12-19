the_simpsons = ["Homer", "Marge", "Bart", "Lisa", "Maggie"]

for character in the_simpsons[::-1]:
    print(f"{character} has a total of {len(character)} characters.")

print(reversed(the_simpsons))
print(type(reversed(the_simpsons)))

# Creates a new type of object: list_reverseiterator that is more eficient on large sets that the before option
for character in reversed(the_simpsons):
    print(f"{character} has a total of {len(character)} characters.")
