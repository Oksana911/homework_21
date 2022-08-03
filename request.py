from shop import Shop
from store import Store

store = Store(items={'яблоко': 10, 'дыня': 20, 'слива': 10})
shop = Shop(items={'яблоко': 2, 'дыня': 2, 'слива': 2})

class Request:
    """Обрабатывает запрос типа "Доставить 3 печеньки из склад в магазин" """

    def __init__(self, request_str):
        req_list = request_str.split(" ")
        self.__amount = int(req_list[1])
        self.__product = req_list[2]
        self.__from = req_list[4]
        self.__to = req_list[6]

    def move(self):
        if self.__to == 'магазин':
            self.__to = 'shop'
        elif self.__from == 'магазин':
            self.__from = 'shop'
        elif self.__to == 'склад':
            self.__to = 'store'
        elif self.__from == 'склад':
            self.__from = 'store'

        if self.__to and self.__from:  # проверка на случай нехватки свободного места в точке выгрузки товара
            if eval(self.__to).add(self.__product, self.__amount):  # чтобы программа не перемещала товар
                eval(self.__from).remove(self.__product, self.__amount)
        elif self.__to:
            eval(self.__to).add(self.__product, self.__amount)
        elif self.__from:
            eval(self.__from).remove(self.__product, self.__amount)

