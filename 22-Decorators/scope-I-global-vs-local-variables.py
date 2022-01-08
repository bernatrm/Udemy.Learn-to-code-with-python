age = 28 # Global scope in current file

def fancy_fun():
    # nonsense = 10 # Local Scope to the function
    age = 100 # this variable, as local will be used, not the global one
              # Shadow Variable: Not a best practice
    print(age)

fancy_fun()
print(age)

TAX_RATE = 0.08

def calculate_tax(price):
    return round(price * TAX_RATE, 2)

def calculate_tip(price):
    return round(price * (TAX_RATE * 3), 2)

print(calculate_tax(10))
print(calculate_tip(10))
