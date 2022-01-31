class FilmMaker():
    def give_interview(self):
        print("I love making movies")

class Director(FilmMaker): # If a class appears more than one time on the tree search, last one will be keep, other will be removedIf it appears more than one time on the tree search, last one will be keep, others will be removed
    pass

class Screenwriter(FilmMaker):
    def give_interview(self):
        print("I love writing scripts!")

class JackOfAllTrades(Screenwriter, Director):
    pass

stallone = JackOfAllTrades()
stallone.give_interview()

print(JackOfAllTrades.mro())