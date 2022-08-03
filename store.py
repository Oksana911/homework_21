from storage import Storage


class Store(Storage):

    @property
    def items(self):
        pass

    @property
    def capacity(self):
        pass

    def __init__(self, items: dict, capacity=100):
        self._items = items
        self._capacity = capacity

    def __repr__(self):
        st = ""
        for key, value in self._items.items():
            st += f"{key}: {value}\n"
        return st

    def add(self, product, amount):  # увеличивает запас items
        if product in self._items.keys():
            if self.get_free_space() >= amount:
                self._items[product] += amount
                print(f'Товар {product} успешно выгружен на склад в количестве {amount}')
            else:
                print('Недостаточно свободного места на складе')
                return False
        else:
            if self.get_free_space() >= amount:
                self._items[product] = product
                self._items[product] += amount
                print(f'Товар {product} успешно выгружен на склад в количестве {amount}')
            else:
                print('Недостаточно свободного места на складе')
                return False

    def remove(self, product, amount):  # уменьшает запас items
        if self._items[product] >= amount:
            print('Нужное количество товара есть на складе')
            self._items[product] -= amount
            print(f'Товар {product} успешно отгружен в количестве {amount}')
        else:
            print('Недостаточно товара')
            return False

    def get_free_space(self):  # вернуть количество свободных мест
        space_count = 0
        for value in self._items.values():
            space_count += value
        return self._capacity - space_count

    @property
    def get_items(self):  # возвращает содержание склада в словаре {товар: количество}
        return f'Всего в {self}: {self._items}'

    def get_unique_items_count(self):  # возвращает количество уникальных товаров
        pass
