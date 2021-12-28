# Define a to_dictionary function that accepts a list of strings. 
# The function should return a dictionary where the keys are the strings 
# and the values are their original index positions in the list.
#
# EXAMPLE:
# detectives = ["Sherlock Holmes", "Hercule Poirot", "Nancy Drew"]
# to_dictionary(detectives) => {'Sherlock Holmes': 0, 'Hercule Poirot': 1, 'Nancy Drew': 2}
def to_dictionary(strings):
    result = {}
    for string in strings:
        result[string] = strings.index(string)
    return result

print("to_dictionary")
detectives = ["Sherlock Holmes", "Hercule Poirot", "Nancy Drew"]
print(to_dictionary(detectives) == {'Sherlock Holmes': 0, 'Hercule Poirot': 1, 'Nancy Drew': 2})
print()

def to_dictionary_solution(strings):
    result = {}
    for index, string in enumerate(strings):
        result[string] = index
    return result

print("to_dictionary_solution")
detectives = ["Sherlock Holmes", "Hercule Poirot", "Nancy Drew"]
print(to_dictionary_solution(detectives) == {'Sherlock Holmes': 0, 'Hercule Poirot': 1, 'Nancy Drew': 2})
print()

# Define a length_counts function that accepts a list of strings. 
# The function should return a dictionary where the keys represent
# length and the values represent how many strings have that length.
#
# EXAMPLE:
# sa_countries = ["Brazil", "Venezuela", "Argentina", "Ecuador", "Bolivia", "Peru"]
# length_counts(sa_countries) => # {6: 1, 9: 2, 7: 2, 4: 1}
# There is 1 string with 6 letters, 2 strings with 9 letters, 
# 2 strings with 7 letters, and 1 string with 4 letters.
def length_counts(strings):
    result = {}
    for string in strings:
        length = len(string)
        if length in result:
            result[length] += 1
        else:
            result[length] = 1
    return result

print("length_counts")
sa_countries = ["Brazil", "Venezuela", "Argentina", "Ecuador", "Bolivia", "Peru"]
print(length_counts(sa_countries) == {6: 1, 9: 2, 7: 2, 4: 1})
print()

def length_counts_solution(strings):
    result = {}
    for string in strings:
        length = len(string)
        result[length] = result.get(length, 0) + 1
    return result

print("length_counts_solution")
sa_countries = ["Brazil", "Venezuela", "Argentina", "Ecuador", "Bolivia", "Peru"]
print(length_counts_solution(sa_countries) == {6: 1, 9: 2, 7: 2, 4: 1})
print()