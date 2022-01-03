agents = { "Mulder", "Scully", "Doggett", "Reyes"}

# agents.remove("Doggett")
# print(agents)

# agents.remove("Skinner") # Raiser a KeyError

agents.discard("Doggett")
print(agents)

agents.discard("Skinner") # Doesn't raise an error. If it doesn't exist, no error is raised
print(agents)

pages = { 10, 20, 30 }
element = pages.remove(30)
print(element)