temperature = [40, 28, 52, 66, 35]
temperature.sort()
print(temperature)
temperature.reverse()
print(temperature)

coffees = ["Latte", "Espresso", "Macchiato", "Frappucino"]
coffees.sort(reverse=True)
# coffees.reverse()
print(coffees)

coffees = ["Latte", "espresso", "macchiato", "Frappucino"]
coffees.sort() # Capital letter order first
print(coffees)

coffees = ["Latte", "Espresso", "Macchiato", "Frappucino"]
print(sorted(coffees)) #returns a new list, not mutated one
print(coffees)