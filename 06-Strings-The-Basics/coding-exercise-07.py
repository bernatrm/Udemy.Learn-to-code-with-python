# Define a first_three_characters function that accepts a string argument.
# The function should return the first 3 characters of the string.
#
# EXAMPLES:
# first_three_characters("dynasty")   => "dyn"
# first_three_characters("empire")    => "emp"
def first_three_characters(word: str) -> str:
    return word[:3]

print(first_three_characters("dynasty"))
print(first_three_characters("empire") )

# Define a last_five_characters function that accepts a string argument. 
# The function should return the last 5 characters of the string.
#
# EXAMPLES:
# last_five_characters("dynasty")   => "nasty"
# last_five_characters("empire")    => "mpire"
def last_five_characters(word: str) -> str:
    return word[-5:]

print(last_five_characters("dynasty"))
print(last_five_characters("empire"))

# Define a is_palindrome function that accepts a string argument. 
# The function should return True if the string is spelled 
# the same backwards as it is forwards. 
# Return False otherwise.
#
# EXAMPLES:
# is_palindrome("racecar")   => True
# is_palindrome("yummy")     => False
def is_palindrome(word: str) -> bool:
    return word == word[::-1]

print(is_palindrome("racecar"))
print(is_palindrome("yummy"))