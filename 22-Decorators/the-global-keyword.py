# x = 10

# def change_stuff():
#     x = 15 # Refer to local Scope

# print(x)
# change_stuff()
# print(x)

# x = 10

def change_stuff_global():
    global x # Refer to Global Scope, in fact modify the global variable
    x = 15   # If not exists, It will be created. VERY BAD PRACTICE

# print(x)
change_stuff_global()
print(x)