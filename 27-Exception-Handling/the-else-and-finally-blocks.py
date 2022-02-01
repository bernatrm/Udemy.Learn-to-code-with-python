x = 10

try:
    print(x + 5)
except NameError:  # if there is an error
    print("Some variable is not defined!")
else: # if there is NOT an error
    print("This will print if there is no error in the try.")
finally:
    print("This will print with or without exception") # for exemple to close a file opened on try secction
    print("Closing file...")