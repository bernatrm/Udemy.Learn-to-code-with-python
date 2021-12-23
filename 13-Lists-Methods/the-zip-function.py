breakfasts = ["Eggs", "Cereal", "Banana"]
lunches = ["Sushi", "Chicken Teriyaki", "Soup"]
diners = ["Steak", "Meatballs", "Pasta"]

# print(zip(breakfasts, lunches, diners))
# print(type(zip(breakfasts, lunches, diners)))
# print(list(zip(breakfasts, lunches, diners)))

for breakfast, lunch, diner in zip(breakfasts, lunches, diners):
    print(f"My meal for today was {breakfast} and {lunch} and {diner}.")