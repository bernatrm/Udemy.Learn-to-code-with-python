first_name = input("What's your first name? ")
print("It's nice to meet you, ", first_name)

# Promt the user for two numbers, one at a time
# The numbers will be received as strrings
# Convert both numbers to integers
# Print a message that includes the sum of the two numbers
print("Let me help you add 2 numbers")
first_number = input("Which is the first number? ")
second_number = input("and the second one? ")
print("The total is", int(first_number) + int(second_number))

# Second implementation
print("Let me help you add 2 numbers")
first_number = int(input("Which is the first number? "))
second_number = int(input("and the second one? "))
print("The total is", first_number + second_number)

#Or
print("Let me help you add 2 numbers")
print("The total is", int(input("Which is the first number? ")) + int(input("and the second one? ")))
