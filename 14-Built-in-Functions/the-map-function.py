numbers = [4, 8, 16, 23, 42]
cubes = [number ** 3 for number in numbers]
print(cubes)

def cube(number):
    return number ** 3

other_cubes = [cube(number) for number in numbers]
print(other_cubes)


print(list(map(cube, numbers)))

animals = ["cat", "bear", "zebra", "donkey", "cheetah"]
print(list(map(len, animals)))