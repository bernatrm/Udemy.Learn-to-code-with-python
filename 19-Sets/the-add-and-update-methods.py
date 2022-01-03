disney_characters = {
    "Mickey Mouse",
    "Minnie Mouse",
    "Elsa"
}

disney_characters.add("Ariel")
print(disney_characters)

disney_characters.add("Elsa")
print(disney_characters)

disney_characters.update(["Donald Duck", "Goofy"])
# disney_characters.add(["Donald Duck", "Goofy"]) # Raise an error
print(disney_characters)

disney_characters.update(("Simba", "Pluto", "Mickey Mouse")) # Any kind of iterable object
print(disney_characters)