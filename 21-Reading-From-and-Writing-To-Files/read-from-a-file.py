# cupcakes_file = open("cupcakes.txt", "r")

# # faulty code

# cupcakes_file.close() # File never closes if an error happens before

# All file will be read, warning with it size
# with open("cupcakes.txt", "r") as cupcakes_file: # When block is done, file is autoclosed
#     print("The file has been opened!")
#     content = cupcakes_file.read()
#     print(content)

# print("The file has been closed. We are outside the context block!")

#Only for smallfiles
filename = input("What file would you want to open? ")
with open(filename, "r") as file_object:
    print(file_object.read())