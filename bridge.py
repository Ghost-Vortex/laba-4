class DrawingAPI:
    def draw_circle(self, x, y, radius):
        pass

class DrawingAPI1(DrawingAPI):
    def draw_circle(self, x, y, radius):
        return f"API1.circle at ({x},{y}) radius {radius}"

class DrawingAPI2(DrawingAPI):
    def draw_circle(self, x, y, radius):
        return f"API2.circle at ({x},{y}) radius {radius}"

class Circle:
    def __init__(self, x, y, radius, drawing_api):
        self.x = x
        self.y = y
        self.radius = radius
        self.drawing_api = drawing_api

    def draw(self):
        return self.drawing_api.draw_circle(self.x, self.y, self.radius)

if __name__ == "__main__":
    circle1 = Circle(1, 2, 3, DrawingAPI1())
    circle2 = Circle(4, 5, 6, DrawingAPI2())
    print(circle1.draw())
    print(circle2.draw())
