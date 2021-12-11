# Declare a negative_energy function that accepts a numeric argument and returns its absolute value. 
# The absolute value is the number's distance from zero.
# 
# negative_energy(5)    => 5
# negative_energy(10)   => 10
# negative_energy(-5)   => 5
# negative_energy(-8)   => 8
# negative_energy(0)    => 0
def negative_energy(number):
    if number > 0:
        return number
    elif number < 0:
        return -1 * number
    else:
        return 0

print(negative_energy(5))
print(negative_energy(10))
print(negative_energy(-5))
print(negative_energy(-8))
print(negative_energy(0))
print()

def negative_energy_option(number):
    if number >= 0:
        return number
    return -1 * number

print(negative_energy_option(5))
print(negative_energy_option(10))
print(negative_energy_option(-5))
print(negative_energy_option(-8))
print(negative_energy_option(0))