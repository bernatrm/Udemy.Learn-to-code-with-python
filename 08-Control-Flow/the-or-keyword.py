if 5 > 8 or 7 < 11:
    print("At least one of the conditions is True!")

# If First condition it's True then the second will not be evaluated, becuase the statement it is already True
if "cat" == "cat" or "dog" == "donkey":
    print("At least one of the conditions is True!")

if "cat" == "cat" or "dog" == "dog":
    print("At least one of the conditions is True!")

if "apple" == "banana" or "orange" == "pear":
    print("Will this print? Nope!")
    