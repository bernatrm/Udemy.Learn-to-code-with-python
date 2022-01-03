a = { 1, 2, 4 }
b = { 1, 2, 3, 4, 5 }

print(a.issubset(b))
print(a < b) # Warning with the order
print(a <= b) # Warning with the order
print(b.issubset(a))

print(b.issuperset(a))
print(b > a) # Warning with the order
print(b >= a) # Warning with the order
print(a.issuperset(b))