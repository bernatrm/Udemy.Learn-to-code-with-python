# LEGB: Local / Enclosing Functions / Global / Built-in
def outer_l():
    x = 10 # Enclosing Function Scope

    def inner():
        x = 5 # Local Scope
        return x
    
    return inner()

print(outer_l())


def outer_e():
    x = 10

    def inner():
        return x
    
    return inner()

print(outer_e())

x = 15 # Global Scope
def outer_g():

    def inner():
        return x
    
    return inner()

print(outer_g())

def outer_b():

    def inner():
        return len # Built-in Scope
    
    return inner()

print(outer_b()("python"))