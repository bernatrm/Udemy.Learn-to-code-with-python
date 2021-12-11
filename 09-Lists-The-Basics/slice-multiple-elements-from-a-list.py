print("programming"[3:6]) # Starting index inclusive and ending index exclusive

muscles = ["Biceps", "Triceps", "Deltoid", "Sartorius"]

print(muscles[1:3]) # prints a list of 2 elements
print(muscles[1:2]) # print  list of 1 element

print(muscles[0:2])
print(muscles[:2])
print(muscles[2:5])
print(muscles[2:])
print(muscles[2:100]) # Will not crash, simpli extracts since the end

print(muscles[-4:-2])
print(muscles[-3:])
print(muscles[:-1])
print(muscles[1:-1])

print(muscles[::2]) # Increments of 2
print(muscles[::-2]) # Increments of 2 from the end of the list
print(muscles[::-1]) # Return in reverse order