import re

pattern = re.compile("flower")

match = pattern.match("a red flower in the field") #difference between .search and .match is that match only search at the beginning of the string

if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())

