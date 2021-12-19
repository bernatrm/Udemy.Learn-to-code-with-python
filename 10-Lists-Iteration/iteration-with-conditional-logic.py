# Sum of Odds
def add_ods(numbers):
    total = 0
    for number in numbers:
        if number % 2 != 0:
            total += number
    return total

print(add_ods([1, 2, 3, 4, 5, 7]))
print()

# Solution
values = [3, 6, 9, 12, 15, 18, 21, 24] # 48
other_values = [5, 10, 15, 20, 25, 30] # 45

def odds_sum(numbers):
    total = 0
    for number in numbers:
        if number % 2 == 1:
            total += number
    return total

print(odds_sum(values))
print(odds_sum(other_values))
print()

# Find the greatest number
def greatest_number(numbers):
    greatest = numbers[0]
    for number in numbers:
        if number > greatest:
            greatest = number
    return greatest


print(greatest_number([1, 2, 3])) # 3
print(greatest_number([3, 2, 1])) # 3
print(greatest_number([4, 5, 5])) # 5
print(greatest_number([-3, -2, -1])) # -1