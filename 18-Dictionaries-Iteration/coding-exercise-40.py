# Declare a plenty_of_arguments function that accepts two parameters (a and b)
# and an additional **kwargs parameter.
#
# The function should return True if the sum of a, b, and the values of 
# **kwargs is greater than 100. It should return False otherwise.
#
# EXAMPLES:
# plenty_of_arguments(20, 30)                          => False
# plenty_of_arguments(a = 50, b = 75)                  => True
# plenty_of_arguments(a = 50, b = 25, c = 50)          => True
# plenty_of_arguments(a = 25, b = 25, c = 25, d = 25)  => False
# plenty_of_arguments(a = 25, b = 25, c = 25, d = 26)  => True
def plenty_of_arguments(a, b, **kwargs):
    total_sum = a + b
    for value in kwargs.values():
        total_sum += value
    return total_sum > 100

print(plenty_of_arguments(20, 30) == False)
print(plenty_of_arguments(a = 50, b = 75) == True)
print(plenty_of_arguments(a = 50, b = 25, c = 50) == True)
print(plenty_of_arguments(a = 25, b = 25, c = 25, d = 25) == False)
print(plenty_of_arguments(a = 25, b = 25, c = 25, d = 26) == True)

def plenty_of_arguments_solution(a, b, **kwargs):
    return a + b + sum(kwargs.values()) > 100

print(plenty_of_arguments_solution(20, 30) == False)
print(plenty_of_arguments_solution(a = 50, b = 75) == True)
print(plenty_of_arguments_solution(a = 50, b = 25, c = 50) == True)
print(plenty_of_arguments_solution(a = 25, b = 25, c = 25, d = 25) == False)
print(plenty_of_arguments_solution(a = 25, b = 25, c = 25, d = 26) == True)
