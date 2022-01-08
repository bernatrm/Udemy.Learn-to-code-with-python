# Define a global "a" variable assigned to the value 1
a = 1

# Declare a "modify_a" function that accepts a single argument.
# It should overwrite the value of the a global variable with the argument
def modify_a(newvalue):
    global a
    a = newvalue

modify_a(10)
print(a)