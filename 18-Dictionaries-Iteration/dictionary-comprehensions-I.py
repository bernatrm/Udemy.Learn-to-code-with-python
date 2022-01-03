languages = ["Python", "JavaScript", "Ruby"]

# language will be the key, and len the value
lengths = { language: len(language) for language in languages if "t" in language } 
print(lengths)

word = "supercalifragilisticexpialidocious"

letter_counts = { letter: word.count(letter) for letter in word if letter > "j"}
print(letter_counts)
