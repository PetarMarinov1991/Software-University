class RhombusOfStars:
    def __init__(self, size):
        self.size = size

    def print_rhombus(self):
        rhombus_of_stars = ''
        for i in range(self.size):
            rhombus_of_stars += ' ' * (self.size - i)
            rhombus_of_stars += '* ' * (i + 1) + '\n'
        for i in range(self.size - 2, -1, -1):
            rhombus_of_stars += ' ' * (self.size - i)
            rhombus_of_stars += '* ' * (i + 1) + '\n'
        return rhombus_of_stars

    def __repr__(self):
        return f'{RhombusOfStars.print_rhombus(self)}'


rhombus = RhombusOfStars(int(input()))
print(rhombus)
