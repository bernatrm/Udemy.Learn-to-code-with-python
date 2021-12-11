# Define a even_or_odd function that accepts a single integer.
# If the integer is even, the function should return the string “even”.
# If the integer is odd, the function should return the string “odd”.
#
# even_or_odd(2)    => "even"
# even_or_odd(0)    => "even"
# even_or_odd(13)   => "odd"
# even_or_odd(9)    => "odd"
def even_or_odd(number: int) -> bool:
    if number % 2 == 0:
        return "even"
    return "odd"

print(even_or_odd(2)) 
print(even_or_odd(0)) 
print(even_or_odd(13))
print(even_or_odd(9)) 
print()

# Define a truthy_or_falsy function that accepts a single argument.
# The function should return a string that reads "The value _____ is ______" 
# where the first space is the argument and the second space 
# is either 'truthy' or 'falsy'. See the sample invocations below.
# 
# truthy_or_falsy(0)        => "The value 0 is falsy"
# truthy_or_falsy(5)        => "The value 5 is truthy"
# truthy_or_falsy("Hello")  => "The value Hello is truthy"
# truthy_or_falsy("")       => "The value  is falsy"
def truthy_or_falsy(argument) -> str:
    if bool(argument):
        is_truthy_or_falsy = "truthy"
    else:
        is_truthy_or_falsy = "falsy"
    return f"The value {argument} is {is_truthy_or_falsy}"


print(truthy_or_falsy(0))
print(truthy_or_falsy(5))
print(truthy_or_falsy("Hello"))
print(truthy_or_falsy(""))
print()

#this is another solution
def truthy_or_falsy_other_solution(argument) -> str:
    if bool(argument):
        return f"The value {argument} is truthy"
    return f"The value {argument} is falsy"

print(truthy_or_falsy_other_solution(0))
print(truthy_or_falsy_other_solution(5))
print(truthy_or_falsy_other_solution("Hello"))
print(truthy_or_falsy_other_solution(""))