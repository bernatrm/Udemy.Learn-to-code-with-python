# Define an invoke_thrice function.
# It should accept a single argument (which will be a function)
# In its body, the invoke_thrice function should invoke
# the function that's passed in exactly three times.
def invoke_thrice(func):
    for i in range(0,3):
        func()

def sample():
    print("A")
    print("B")
    print("C")

def another_sample():
    print("D")
    print("E")

invoke_thrice(another_sample)