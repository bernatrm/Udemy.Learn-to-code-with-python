empty_space = "      content         "

print(empty_space.rstrip())
print(len(empty_space.rstrip()))

print(empty_space.lstrip())
print(len(empty_space.lstrip()))

print(empty_space.strip())
print(len(empty_space.strip()))

website = "www.python.org"

print(website.lstrip("w")) # Remove from the left the specified string/char
print(website.rstrip("org")) # Remove from the right the specified string/char
print(website.strip("worg.")) # Remove any character specified from the right or the left

another_website = "www.py org thon.org"
print(another_website.strip("worg.")) # Remove any character specified from the right or the left, but not in the middle
