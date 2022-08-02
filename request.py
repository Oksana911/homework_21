from shop import Shop
from store import Store


class Request:
    """класс Request в котором хранится запрос"""
    # Доставить 3 печеньки из склад в магазин

    def __init__(self, request_str):
        req_list = request_str.split(" ")
        self.__amount = int(req_list[1])
        self.__product = req_list[2]
        self.__from = req_list[4]
        self.__to = req_list[6]

    def move(self):
        if self.__to:
            eval(self.__to).add(self.__product, self.__amount)
        if self.__from:
            eval(self.__from).remove(self.__product, self.__amount)
