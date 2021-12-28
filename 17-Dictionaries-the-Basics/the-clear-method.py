websites = {
    "Wikipedia": "http://www.wikipedia.org",
    "Google": "http://wwww.google.com",
    "Netflix": "http://www.netflix.com"
}

websites.clear()
print(websites)

del websites["Google"] # Deletes one element of the Dictionary
del websites # Deletes de variable

print(websites) # Raise an error because the variable no longer exists after "del"