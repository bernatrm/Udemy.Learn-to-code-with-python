import time
class Garbage():
    def __del__(self):  # It is executed when the program doesn't need anymore this object
        print("This is my last breath!")

g = Garbage()

g = [1, 2, 3]

time.sleep(5)

print("Program done!")