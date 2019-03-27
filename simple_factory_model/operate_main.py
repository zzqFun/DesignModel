# coding = utf-8
class OperateMain:
    def __init__(self):
        self.__number_a = 0.0
        self.__number_b = 0.0

    @property
    def number_a(self):
        return self.__number_a

    @number_a.setter
    def number_a(self, value):
        self.__number_a = value

    @property
    def number_b(self):
        return self.__number_b

    @number_b.setter
    def number_b(self, value):
        self.__number_b = value
