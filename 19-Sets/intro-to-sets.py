{"Primer": 1, "Segon": 2} # Dictionary
{ 1, 2} # Set

stocks = { "MSFT", "FB", "IBM", "FB"}

print(stocks)

prices = { 1, 2, 3, 4, 5, 3, 4 ,2 }
print(prices)

lottyery_numbers = { (1, 2, 3), (4, 5, 6), (1, 2, 3)}
print(lottyery_numbers)

print(len(stocks))
print(len(prices))
print(len(lottyery_numbers))

print("MSFT" in stocks)
print("GOOG" not in stocks)

# print(stocks[2]) # Raises an error, Sets are not ordered

for number in prices:
    print(number) # Order is totally ramdon

for numbers in lottyery_numbers:
    for number in numbers:
        print(number)

squares = { number ** 2 for number in [-5, -4, -3, 3, 4, 5] }
print(squares) # Set of 3 elements, because square of -5 and 5 has the same result
print(len(squares))
