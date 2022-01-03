# Assign a list of four dictionaries to a "complexity" variable below

# The first and third dictionaries should have two key-value pairs
# For those dictionaries, the keys should be strings and the values should be Booleans

# The second and fourth dictionaries should have three key-value pairs
# For those dictionaries, the keys shoulds be floats and the values should be list of strings. 
# The lists can be of any length.
complexity = [
    {
        "color": False, 
        "active": True},
    {
        9.9: ["cheap", "expensive"], 
        3.3: ["nice", "rough"], 
        1.1: ["old"]},
    {
        "color": True, 
        "active": False},
    {
        9.9: ["slow", "fast"], 
        3.3: ["good", "bad"], 
        1.1: ["new"]}
]

for element in complexity:
    print(len(element))
    for key, value in element.items():
        print(f"El tipo de la clave {key} es {type(key)} y el tipo del valor es {type(value)}")