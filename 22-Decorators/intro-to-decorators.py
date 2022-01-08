def be_nice(fn):
    def inner():
        print("Nice to meet you! I'm honored to execute your function for you!")
        fn()
        print("It was my pleasure executing your function! Have a nice day")    
    
    return inner

@be_nice
def complex_business_logic():
    print("Something complex!")

# result = be_nice(complex_business_logic)
# result()

# be_nice(complex_business_logic)() # the same as @be_nice

@be_nice
def another_fancy_function():
    print("Goo goo gaga")

complex_business_logic() # with the decorator @be_nice it is teh same than "be_nice(complex_business_logic)()"
another_fancy_function()