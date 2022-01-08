import functools

def be_nice(fn):
    @functools.wraps(fn) # This will preserve our original documentation
    def inner(*args, **kwargs): # Convert parameters into a Tuple and Dictionary
        print("Nice to meet you! I'm honored to execute your function for you!")
        result = fn(*args, **kwargs) # Convert Tuple and Dictionary into arguments
        print("It was my pleasure executing your function! Have a nice day")
        return result
    
    return inner

@be_nice
def complex_business_logic_sum(a, b):
    "Adds two numbers together"
    return a + b

help(complex_business_logic_sum)