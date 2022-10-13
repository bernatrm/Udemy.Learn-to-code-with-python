import re

pattern = re.compile("flower")
print(type(pattern))

print(pattern.search("candy"))

match = pattern.search("a red flower power in the field flower") # match returns first occurrence
print(type(match))

if match:
    print(match.group())
    print(match.start())
    print(match.end()) #exclusive position
    print(match.span()) #exclusive position



