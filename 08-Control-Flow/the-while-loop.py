# count = 0

# while count <= 5:
#     print(count)
#     count += 1

# print(count)

# # Never will execute it because count value is 6
# while count <= 5:
#     print(count)
#     count += 1

invalid_number = True

while invalid_number:
    user_value = int(input("Please enter a number above 10: "))
    if user_value > 10:
        print(f"Thanks, that works! {user_value} is great choice!")
        invalid_number  = False
    else:
        print("That doesen't fit, Try again!")