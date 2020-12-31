class Complex:
    def __init__(self, r=0, i=0):
        self.r = r
        self.i = i

    def __add__(self, other):
        return Complex(self.r + other.r, self.i + other.i)

    def __sub__(self, other):
        return Complex(self.r - other.r, self.i - other.i)

    def __mul__(self, other):
        return Complex(self.r * other.r - self.i * other.i, self.r * other.i + self.i * other.r)

    def __truediv__(self, other):
        return Complex((self.r * other.r - self.i * other.i) / (other.r * other.r + other.i * other.i),
                       (other.r * self.i - self.r * other.i) / (self.i * self.i + other.i * other.i))

    def __abs__(self):
        return (self.r * self.r + self.i * self.i) ** (1 / 2)

    def __str__(self):
        return "(" + str(self.r) + "," + str(self.i) + ")"


class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ")"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y, self.z * other.z)

    def __truediv__(self, other):
        return Vector(self.x / other.x, self.y / other.y, self.z / other.z)

    def length(self):
        return (self.x * self.x + self.y * self.y + self.z * self.z) ** (1 / 2)

    def area(self, other):
        return (((self.x ** 2 + self.y ** 2) * (other.x ** 2 + other.y ** 2)(
            1 - (self.x * other.x + self.y * other.y)) ** (1 / 2)) / ((self.x ** 2 + self.y ** 2) ** (1 / 2)) * (
                            other.x ** 2 + self.y ** 2) ** (1 / 2))

    def volume(self, other, another):
        return abs(self.x * (other.y * another.z - other.z * another.y) - self.y * (
                    other.x * another.z - another.x * other.z) + self.z * (other.x * another.y - other.y * another.z))

    def centrmass(self, other, another):
        return Vector((self.x + other.x + another.x) / 3, (self.y + other.y + another.y) / 3,
                      (self.z + other.z + another.z) / 3)
