# In this exercise, we'll be modelling a routine for proper dental health,
# which includes brushing our teeth, flossing, and using mouthwash.
# The order of these three varies from person to person.

# Declare a DentalHealthItem class. Its initialization should set a "price"
# attribute.
class DentalHealthItem():
    def __init__(self, price):
        self.price = price

# Declare a Toothbrush subclass that inherits from DentalHealthItem.
# On it, define a "use" instance method that returns "Brushing the teeth"
class Toothbrush(DentalHealthItem):
    def use(self):
        return "Brushing the teeth"

# Declare a Floss subclass that inherits from DentalHealthItem.
# On it, define a "use" instance method that returns "Flossing the teeth"
class Floss(DentalHealthItem):
    def use(self):
        return "Flossing the teeth"

# Declare a Mouthwash subclass that inherits from DentalHealthItem.
# On it, define a "use" instance method that returns "Washing the teeth"
class Mouthwash(DentalHealthItem):
    def use(self):
        return "Washing the teeth"

# Instantiate an instance of a Toothbrush and assign it a "toothbrush" variable.
# Instantiate an instance of a Floss and assign it a "floss" variable.
# Instantiate an instance of a Mouthwash and assign it a "mouthwash" variable.
toothbrush = Toothbrush(5)
floss = Floss(4)
mouthwash =Mouthwash(6)

# Declare a "dental_health_kit" variable. It should be a list that stores the three objects.
dental_health_kit = [toothbrush, floss, mouthwash]

# Import the "random" module (see last lesson for reference). 
# Invoke the "shuffle" function from the module, passing in the dental_health_kit list. 
# This will mutate the list, randomizing the order of its elements.
import random
random.shuffle(dental_health_kit)

# Use list comprehension to invoke the "use" method on all three objects in "dental_health_kit".
# Assign the resulting list of strings to an "actions" variable.

# actions = []
# for item in dental_health_kit:
#     actions.append(item.use())

actions = [item.use() for item in dental_health_kit]

print(actions)