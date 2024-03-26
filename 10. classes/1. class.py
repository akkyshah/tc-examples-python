class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def __str__(self):
        return self.fname + " " + self.lname + " (" + str(self.age) + ")"

    def increase_age(self):
        self.age += 1


p1 = Person('John', 'Doe', 21)

print(p1.age)

p1.increase_age()

print(p1.age)
