set() # Only way to create an empty set
print(set([1, 2, 3, 3, 2, 1]))

print(set((1, 2, 1, 2, 1)))

print(set("abc"))
print(set("aabbcc"))
print(set("abc") == set("aabbcc"))

print(set({ "key": "value"})) # Takes the keys

# Use case: to eliminate duplicates in a list, if you don't care order

philosophers = ["Plato", "Socrates", "Aristotle", "Pythagoras", "Socrates", "Plato"]
philosophers_set = set(philosophers)
philosophers = list(philosophers_set)
print(philosophers)