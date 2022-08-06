from store import Store


class Shop(Store):

    def __init__(self, items: dict, capacity=20):
        super().__init__(items, capacity)

    def add(self, product, amount):  # увеличивает запас items
        if self.get_unique_items_count() >= 5:
            print('Магазин не может быть пополнен, если в нем уже есть 5 разных товаров.')
        else:
            super().add(product, amount)

    def get_unique_items_count(self):  # возвращает количество уникальных товаров
        return len(self._items.keys())
