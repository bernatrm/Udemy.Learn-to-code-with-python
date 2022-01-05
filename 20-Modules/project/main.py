# import feature.subfeature.calculator
# import feature.copyright

# print(feature.subfeature.calculator.substract(10, 5))
# print(feature.copyright.date_of_copyright)

# from feature.subfeature import calculator
# print(calculator.substract(10, 3))

# from feature.subfeature.calculator import substract
# print(substract(10, 3))

# import feature.subfeature.calculator
# print(feature.subfeature.calculator.substract(10, -1))

import feature.subfeature # Direct avaliable in the packge, simply if it's included on __init__.py
print(feature.subfeature.substract(10, -1))
