from shop import Shop
from store import Store


class Request:
    """Обрабатывает запрос типа "Доставить 3 яблоко из склад в магазин" """

    def __init__(self, request_str):
        req_list = request_str.split(" ")
        self.__amount = int(req_list[1])
        self.__product = req_list[2]
        self.__from = req_list[4]
        self.__to = req_list[6]

    def move(self):
        if self.__to == 'магазин':
            self.__to = 'shop'
        if self.__to == 'склад':
            self.__to = 'store'
        if self.__from == 'магазин':
            self.__from = 'shop'
        if self.__from == 'склад':
            self.__from = 'store'

        if eval(self.__from).remove(self.__product, self.__amount):
            eval(self.__to).add(self.__product, self.__amount)


store = Store(items={'яблоко': 10, 'дыня': 20, 'слива': 10, 'кокос': 10, 'банан': 10, 'перец': 10})
shop = Shop(items={'яблоко': 2, 'дыня': 2, 'слива': 2})
