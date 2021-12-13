class Students:
    def __init__(self, name, age, class_='Student'):
        self.name = name
        self.age = age
        self.class_ = class_

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nClass: {self.class_}\n"

    def set_class(self, class_):
        self.class_ = class_
        return f"{self.name}'s Class has been changed to {self.class_}\n"

    def average_test_score(self, s1, s2, s3):
        return f"{self.name}'s average test score is {round((s1 + s2 + s3)/3, 2)}\n"


jack = Students('Jack', 22)
dave = Students('Dave', 21, 'Physics')
print(jack)
print(dave)
print(jack.set_class('Maths'))
print(jack)
print(jack.average_test_score(75, 32, 76))
print(dave.average_test_score(54, 42, 46))
