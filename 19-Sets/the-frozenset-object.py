# frozenset: immutable set
mr_freeze = frozenset([1, 2, 3, 2])
print(mr_freeze)

# mr_freeze.add(4) # Raise an error
regular_set = { 1, 2, 3 }
# print({regular_set: "Some value"}) # Raise TypeError

print({mr_freeze: "Some value"}) # Generates a dictionary