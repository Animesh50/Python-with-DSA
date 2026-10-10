class Calculater:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"the square is {self.n*self.n}")

    def cube(self):
        print(f"the cube is {self.n*self.n*self.n}")

    def squareRoot(self):
        print(f"the squareRoot is {self.n**1/2}")

n = int(input("Enter the number: "))
a = Calculater(n)
a.square()
a.cube()
a.squareRoot()