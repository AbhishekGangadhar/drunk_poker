
class Player:
    def __init__(self, name: str):
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

