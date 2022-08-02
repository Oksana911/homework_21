from store import Store


class Shop(Store):

    @property
    def items(self):
        pass

    @property
    def capacity(self):
        pass

    def __init__(self, items: dict, capacity=20):
        self._items = items
        self._capacity = capacity

    def add(self, product, amount):  # увеличивает запас items
        if self.get_unique_items_count() >= 5:
            return 'Магазин не может быть наполнен, если в нем уже есть 5 разных товаров.'
        if self.get_free_space() >= amount:
            self._items[product] += amount
            return f'Товар {product} успешно выгружен в магазин в количестве {amount}'
        else:
            return 'Недостаточно свободного места в магазине'


# shop = Shop(items={'яблоко': 3, 'дыня': 3, 'слива': 1})
