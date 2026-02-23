class Color:
    def apply(self):
        pass

class Red(Color):
    def apply(self):
        return "Красный"

class Shape:
    def __init__(self, color):
        self.color = color

class Circle(Shape):
    def draw(self):
        print(f"Круг цвета {self.color.apply()}")

circle = Circle(Red())
circle.draw()
