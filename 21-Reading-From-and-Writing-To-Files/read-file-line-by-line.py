with open("cupcakes.txt", encoding="utf-8") as file_object:
    for line in file_object:
        print(line.rstrip())