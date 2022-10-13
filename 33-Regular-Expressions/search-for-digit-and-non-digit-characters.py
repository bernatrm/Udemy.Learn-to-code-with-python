import re

pattern = re.compile(r"\d") # d = Digits

sentence = "I went to the store and bought 5 apples, 4 oranges, and 15 plums."
print(pattern.findall(sentence))

pattern = re.compile(r"\D") # D = All non digits
print(pattern.findall(sentence))