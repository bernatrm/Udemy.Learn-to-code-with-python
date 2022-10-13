from ast import pattern
import re

pattern = re.compile("flower")

sentence = "The are a lot of flowers in the flowery flower field"

print(pattern.findall(sentence))
print(pattern.findall("Nonsense"))

for match in pattern.finditer(sentence):
    print(match)