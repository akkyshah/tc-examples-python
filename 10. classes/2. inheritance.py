class Person:
    def __init__(self, name, age):
        print('creating parent PERSON')
        self.name = name
        self.age = age

    def increase_age(self):
        self.age += 1


class Student(Person):
    def __init__(self, name, age, roll_no):
        print('creating child STUDENT')
        super().__init__(name, age)
        self.roll_no = roll_no
        self.grade = 1

    def __str__(self):
        return f'{self.roll_no}. {self.name} - Grade: {self.grade}'

    def increase_grade(self):
        self.grade += 1


class Employee(Person):
    def __init__(self, name, age, empId, salary):
        print('creating child RMPLOYEE')
        super().__init__(name, age)
        self.empId = empId
        self.salary = salary

    def increase_salary(self):
        self.salary *= 1.1


s = Student('John', 10, 21)
e = Employee('Mike', 45, 100011023, 100000)

s.increase_age() # 22
e.increase_age() # 46

s.increase_grade()
e.increase_salary()