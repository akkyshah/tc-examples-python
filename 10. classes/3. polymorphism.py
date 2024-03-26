class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def get_area(self):
        area = self.length * self.breadth
        return f'area = {area}'


class Square:
    def __init__(self, side):
        self.side = side

    def get_area(self):
        area = pow(self.side, 2)
        return f'area = {area}'


shapes = [
    Rectangle(100, 200),
    Square(5)
]

for shape in shapes:
    print(f'{type(shape)} - {shape.get_area()}')
