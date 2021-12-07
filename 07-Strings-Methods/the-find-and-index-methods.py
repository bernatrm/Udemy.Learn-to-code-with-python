browser = "Google Chrome"

print(browser.find("C")) # First ocurrence
print(browser.find("Ch")) # Starting position
print(browser.find("o"))
print(browser.find("G"))
print(browser.find("Z"))
print(browser.find("Zxy"))
print(browser.find("c")) # Case sensitive

print()

print(browser.find("o"))
print(browser.find("o", 2))
print(browser.find("o", 5))

print("Ch" in browser) # If only I want to know if it is in the string

print(browser.index("C"))
print(browser.index("Z")) # If not find the string raises and error