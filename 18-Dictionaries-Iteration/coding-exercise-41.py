# You are writing a Python program to model a remote control
# for a television set. Declare a stations_to_numbers
# function that accepts a dictionary. The keys will be
# channel numbers and the values will be the station names.
# For example...
# channels = {
#   2: "CBS",
#   4: "NBC",
#   5: "FOX",
#   7: "ABC"
# }
# The stations_to_numbers function should return an
# inverted dictionary where the keys are the station names
# and the values are the channel numbers
#
# stations_to_numbers(channels) => {'CBS': 2, 'NBC': 4, 'FOX': 5, 'ABC': 7}
def stations_to_numbers(channels):
    return { station: number for number, station in channels.items()} # index, key for enumerate(iterable)

channels = {
    2: "CBS",
    4: "NBC",
    5: "FOX",
    7: "ABC"    
}

print("stations_to_numbers")
print(stations_to_numbers(channels) == {'CBS': 2, 'NBC': 4, 'FOX': 5, 'ABC': 7})

# Declare a coaster_conversion function that accepts a dictionary
# The keys of the dictionary will be strings representing roller coasters
# The values will be the heights of each coaster in meters
#
# Return a new dictionary with the same keys.
# The values should be the heights converted from meters to feet,
# The final values (in feet) should also be rounded to the closest integer
# HINT: 1 meter is equal to 3.28084 feet
# HINT: The round function rounds a number to the nearest integer
#
# coasters = {
#   "Kingda Ka": 139,
#   "Top Thrill Dragster": 130,
#   "Superman: Escape From Krypton": 126
# }
#
# coaster_conversion(coasters) => {'Kingda Ka': 456, 'Top Thrill Dragster': 427, 'Superman: Escape From Krypton': 413}
def coaster_conversion(my_coasters):
    return { roller_coaster: round(height*3.28084) for roller_coaster, height in my_coasters.items()}

coasters = {
    "Kingda Ka": 139,
    "Top Thrill Dragster": 130,
    "Superman: Escape From Krypton": 126
}

print("coaster_conversion")
print(coaster_conversion(coasters) == {'Kingda Ka': 456, 'Top Thrill Dragster': 427, 'Superman: Escape From Krypton': 413})
