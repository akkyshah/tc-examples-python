class Rectangle:
    def __init__(self, length, breadth):    # 5, 5
        self.length = length    # 5
        self.breadth = breadth  # 5

    def get_area(self):
        area = self.length * self.breadth
        return 'area = {}'.format(area)


class Square(Rectangle):
    def __init__(self, side):           # 5
        super().__init__(side, side)    # 5, 5

    def get_area(self):
        return super().get_area()


shapes = [
    Rectangle(100, 200),
    Square(5)
]

for shape in shapes:
    print(f'{type(shape)} - {shape.get_area()}')
