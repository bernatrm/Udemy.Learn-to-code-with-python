# Declare a Musical class that accepts a name parameter. 
# In the initialization process for an object, assign the
# name parameter to a name attribute on the object.
#
# Instantiate a Musical object with the name “Rent” 
# and assign it to an “rent" variable.
#
# Instantiate a second Musical object with the name “Book of Mormon" 
# and assign it to a “mormon” variable.
#
# Instantiate a third object from the class with the name “Chicago" 
# and assign it to a “chicago” variable.
class Musical():
    def __init__(self, name):
        self.name = name

rent = Musical("Rent")
mormon = Musical("Book of Mormon")
chicago = Musical("Chicago")

print(rent.name)
print(mormon.name)
print(chicago.name)

# Declare a Shape class that accepts a sides parameter. 
class Shape():

# In the initialization process for an object, assign the sides parameter to a sides attribute on the object.
    def __init__(self, sides):
        self.sides = sides

# Instantiate a Shape object with 3 sides and assign it to a “triangle" variable.
triangle = Shape(3)
# Instantiate a Shape object with 4 sides and assign it to a “square" variable.
square = Shape(4)
# Instantiate a Shape object with 10 sides and assign it to a “decagon" variable.
decagon = Shape(10)

print(triangle.sides)
print(square.sides)
print(decagon.sides)


# Declare a Skyscraper class that accepts name and year parameters. 
class Skyscraper():
    def __init__(self, name, year):
# In the initialization process for an object, assign the name parameter to a name attribute 
# and the year parameter to a year attribute.
        self.name = name
        self.year = year
# Instantiate a Skyscraper object with the name “Empire State Building”  and the year 1931. 
# Assign it to a “empire" variable.
empire = Skyscraper("Empire State Building", 1931)
# Instantiate a Skyscraper object with the name “One World Trade Center” and the year 2014. 
# Assign it to a “wtc" variable.
wtc = Skyscraper(name = "One World Trade Center", year = 2014)

print(empire.name == "Empire State Building" and empire.year == 1931)
print(wtc.name == "One World Trade Center" and wtc.year == 2014)