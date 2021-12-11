def reverse(str):
    start_index = 0
    last_index = len(str) - 1
    reversed_string = ""

    while last_index >= start_index:
        reversed_string += str[last_index]
        last_index -= 1

    return reversed_string

print(reverse("straw")) # warts

def reverse_recursion(str):
    if len(str) <= 1:
        return str    

    return str[-1] + reverse_recursion(str[:-1])
    
print(reverse_recursion("straw")) # warts

# straw
# w + reverse(stra)
# w + a + reverse(str)
# w + a + r + reverse(st)
# w + a + r + t + reverse(s)
# w + a + r + t + s
