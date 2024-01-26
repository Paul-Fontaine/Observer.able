from observable import Observable


class Temperature(Observable):
    def __init__(self, value: int = 0):
        Observable.__init__(self)
        self.__value: int = value

    def get_value(self) -> int:
        return self.__value

    def set_value(self, value: int):
        self.__value = value
