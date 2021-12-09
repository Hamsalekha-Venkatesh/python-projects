class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    def divide(self):
        if self.y == 0:
            raise BaseException("Invalid input has been passed!")

        return self.x / self.y


# cal = Calculator(6, 2)
# print(cal.add())
# print(cal.subtract())
# print(cal.multiply())
# print(cal.divide())