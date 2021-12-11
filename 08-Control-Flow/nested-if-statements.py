ingredient1 = "Pasta"
# ingredient1 = "Pizza"
# ingridient2 = "Meatballs"
ingridient2 = "Sausage"

if ingredient1 == "Pasta":
    if ingridient2 == "Meatballs":
        print("I recommend making pasta and meatballs")
    else:
        print("I recommend making plain pasta")
else:
    print("I have not recommendations")

# Option 2
if ingredient1 == "Pasta" and ingridient2 == "Meatballs":
    print("I recommend making pasta and meatballs")
elif ingredient1 == "Pasta":
    print("I recommend making plain pasta")
else:
    print("I have not recommendations")
