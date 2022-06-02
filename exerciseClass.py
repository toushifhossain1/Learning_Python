class triangle:
    base = ""
    height = ""

    def __init__(self, base, height) -> None:
        self.base = base
        self.height = height

    def area(self):
        print("this is running")
        print(int(self.base) * int(self.height) * 0.5)


triangle1 = triangle(2, 4)
triangle1.area()
