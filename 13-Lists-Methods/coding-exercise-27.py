# Define a word_lengths function that accepts a string. 
# It should return a list with the lengths of each word.
#
# EXAMPLES
# word_lengths("Mary Poppins was a nanny")  => [4, 7, 3, 1, 5]
# word_lengths("Somebody stole my donut")   => [8, 5, 2, 5]
def word_lengths(words):
    words_list = words.split(" ")
    lenghts = []
    for word in words_list:
        lenghts.append(len(word))
    return lenghts

print(word_lengths("Mary Poppins was a nanny") == [4, 7, 3, 1, 5])
print(word_lengths("Somebody stole my donut") == [8, 5, 2, 5])

# Define a cleanup function that accepts a list of strings.
# The function should return the strings joined together by a space.
# There's one BIG problem -- some of the strings are empty or only consist of spaces!
# These should NOT be included in the final string
#
# cleanup(["cat", "er", "pillar"])           => "cat er pillar"
# cleanup(["cat", " ", "er", "", "pillar"])  => "cat er pillar"
# cleanup(["", "", " "])                     => ""
def cleanup(strings):
    words = []
    for string in strings:
        if string != " " and string != "":
            words.append(string)
    return " ".join(words)

print(cleanup(["cat", "er", "pillar"]) == "cat er pillar"        )
print(cleanup(["cat", " ", "er", "", "pillar"]) == "cat er pillar")
print(cleanup(["", "", " "]) == "")

def cleanup_solution(strings):
    clean_strings = []
    for string in strings:
        if string.isspace() or len(string) == 0:
            continue
        clean_strings.append(string)
    return " ".join(clean_strings)

print(cleanup_solution(["cat", "er", "pillar"]) == "cat er pillar"        )
print(cleanup_solution(["cat", " ", "er", "", "pillar"]) == "cat er pillar")
print(cleanup_solution(["", "", " "]) == "")