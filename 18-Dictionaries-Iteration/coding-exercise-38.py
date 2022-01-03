# Declare a common_elements function that accepts a dictionary
# It should return a list with all of the elements that are found
# as both a key and a value in the dictionary
#
# HINT: Use the in operation to check for inclusion in a view or list object
#
# EXAMPLE:
# my_dict = {
#   "A": "K",
#   "B": "D",
#   "C": "A",
#   "D": "Z"
# }
#
# common_elements(my_dict) => ["A", "D"]
# def common_elements(elements):
#     result = []
#     for key in elements.keys():
#         if key in elements.values():
#             if key not in [result]:
#                 result.append(key)
#     for value in elements.values():
#         if value in elements.keys():
#             if value not in result:
#                 result.append(value)
#     return result
def common_elements(elements):
    result = {}
    for key in elements.keys():
        if key in elements.values():
            result[key] = key
    for value in elements.values():  # I don't need to iterate over keys and values, because I am searching 
        if value in elements.keys(): # for keys that appers as values or values that appears as keys...
            result[value] = value    # then if a key apperas as value, that value will appear as key
    return list(result.values())     # so I only need to do one iteration

def common_elements_solution(my_dict):
    return [key for key in my_dict.keys() if key in my_dict.values()]

print("common_elements")
my_dict = {
  "A": "K",
  "B": "D",
  "C": "A",
  "D": "Z"
}

print(common_elements(my_dict) == ["A", "D"])
print(common_elements_solution(my_dict) == ["A", "D"])
print()