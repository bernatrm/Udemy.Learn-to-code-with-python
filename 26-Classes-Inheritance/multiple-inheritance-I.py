class FrozenFood():
    def thaw(self, minutes):
        print(f"Thawing for {minutes} minutes")

    def store(self):
        print("Putting in the freezer!")
class Dessert():
    def add_weight(self):
        print("Putting on the pounds!")

    def store(self):
        print("Putting in the refrigerator")

class IceCream(Dessert, FrozenFood):
    pass

ic =IceCream()
ic.thaw(5)
ic.add_weight()
ic.store() # Executes by the order on definition, search on the first class, and if it not found, then search on the second one

print(IceCream.mro())