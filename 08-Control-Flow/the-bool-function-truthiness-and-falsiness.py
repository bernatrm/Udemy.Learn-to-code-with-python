# o is considered = False, other one is considered True (positive or negative)
if 3:
    print("Hello")

if -1:
    print("Goodbye")

if 0:
    print("Will this print?")

# empty string will be considered False
if "hello":
    print("la la la")

if "":
    print("This will not print")

print(bool(1))
print(bool(0))
print(bool(""))
print(bool("Python"))
print(bool(3.14))
print(bool(-1.309098))
print(bool(0.0))