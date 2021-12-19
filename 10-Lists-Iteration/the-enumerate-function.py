errands = ["Go to gym", "Grab lunch", "Get promoted at work", "Sleep"]

print(enumerate(errands))

for index, errand in enumerate(errands, 1):
    print(f"{errand} is number {index} on my list to do today!")
