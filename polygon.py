class Rectangle:
    def __init__(self, width, height):
        self.height = height
        self.width = width

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, width):
        self.width = width
        return width

    def set_height(self, height):
        self.height = height
        return height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_amount_inside(self, shape):
        return int(self.get_area() / shape.get_area())

    def get_picture(self):
        i = 0
        if self.width or self.height > 50:
            return "Too big for picture."
        while i < self.height:
            print("*" * self.width, end="\n") * self.height
            i -= 1


class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f'Square(side={self.width})'

    def set_side(self, side):
        self.width = side
        self.height = side
