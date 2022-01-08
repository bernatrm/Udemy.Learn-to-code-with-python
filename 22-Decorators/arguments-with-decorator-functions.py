def be_nice(fn):
    def inner(*args, **kwargs): # Convert parameters into a Tuple and Dictionary
        print("Nice to meet you! I'm honored to execute your function for you!")
        # print(args)
        # print(kwargs)
        fn(*args, **kwargs) # Convert Tuple and Dictionary into arguments
        print("It was my pleasure executing your function! Have a nice day")    
    
    return inner

@be_nice
def complex_business_logic(stakeholder):
    print(f"Something complex for {stakeholder} !")

@be_nice
def more_complex_business_logic(stakeholder, position):
    print(f"Something complex for our {position} {stakeholder} !")

# complex_business_logic("Boris", 1, 2, stakeholder="Boris", hello = True)
complex_business_logic("Boris")
complex_business_logic(stakeholder="Boris")

more_complex_business_logic("Boris", "CEO")
more_complex_business_logic(stakeholder="Boris", position="CEO")
more_complex_business_logic("Boris", position="CEO")
