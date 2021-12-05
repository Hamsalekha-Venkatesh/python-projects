class Point:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def sqSum(self):
        return pow(self.a, 2) + pow(self.b, 2) + pow(self.c, 2)
