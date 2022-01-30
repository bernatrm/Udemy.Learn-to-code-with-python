class Student():
    def __init__(self, math, history, writing):
        self.math = math
        self.history = history
        self.writing = writing

    @property
    def grades(self):
        return self.math + self.history + self.writing

    def __eq__(self, other_student: object) -> bool:
        return self.grades == other_student.grades

    def __gt__(self, other_student: object) -> bool: # > - greater
        return self.grades > other_student.grades

    def __le__(self, other_student: object) -> bool:  # < - lesser
        return self.grades <= other_student.grades    # Why "<="

    def __add__(self, other_studend: object) -> float:
        return self.grades + other_studend.grades

    def __sub__(self, other_studend: object) -> float:
        return self.grades - other_studend.grades

bob = Student(math= 90, history= 90, writing= 90)  #270
moe = Student(math= 100, history= 90, writing= 80) #270
joe = Student(math= 40, history= 45, writing= 50)  #135

print(moe > joe)
print(moe <= joe)
print(bob + moe)
print(moe - joe)




