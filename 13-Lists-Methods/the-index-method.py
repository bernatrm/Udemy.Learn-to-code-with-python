pizzas = [
    "Mushroom",
    "Pepperoni",
    "Sausage",
    "Barbecue Chicken",
    "Pepperoni",
    "Sausage"
]

print(pizzas.index("Barbecue Chicken"))
print(pizzas.index("Pepperoni"))
print(pizzas.index("Sausage"))

if "Olives" in pizzas:
    print(pizzas.index("Olives")) # Seek for an element that is not in the list raise an error

print(pizzas.index("Pepperoni", 2)) # 2 Index from the begining
print(pizzas.index("Sausage", 3)) # Starting Index is Inclusing
print(pizzas.index("Sausage", 2)) # Starting Index is Inclusing
