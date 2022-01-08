class SmartPhone():
    def __init__(self):
        self._company = "Apple" # All attributes are public
        self._firmware = 10.0 # By underscore the attribute name, we suggest that you will not modify it directly

    def get_os_version(self):
        return self._firmware

    def update_firmware(self):
        print("Reaching out to the server for the next version")
        self._firmware += 1


iphone = SmartPhone()
print(iphone._company)
print(iphone._firmware)

iphone.update_firmware()
print(iphone._firmware)