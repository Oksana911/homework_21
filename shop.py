from store import Store


class Shop(Store):

    def __init__(self, items: dict, capacity=20):
        super().__init__(items, capacity)

    def add(self, product, amount):  # увеличивает запас items
        if self.get_unique_items_count() >= 5:
            print('Магазин не может быть наполнен, если в нем уже есть 5 разных товаров.')
        if self.get_free_space() >= amount:
            self._items[product] += amount
            print(f'Товар {product} успешно выгружен в магазин в количестве {amount}')
        else:
            print('Недостаточно свободного места в магазине')
            return False
