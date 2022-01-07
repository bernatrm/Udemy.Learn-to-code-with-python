file_name = "my_first_file.txt"

with open(file_name, "w", encoding="utf-8") as file_object:
    file_object.write("Hello file!\n") # if the file exists, it's overwrite
    file_object.write("You're my favourite file!")