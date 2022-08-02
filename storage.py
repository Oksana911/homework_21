from abc import ABC, abstractmethod


# абстрактный класс:
class Storage(ABC):
    @property
    @abstractmethod
    def items(self):
        pass

    @property
    @abstractmethod
    def capacity(self):
        pass

    @abstractmethod
    def add(self, product, amount):  # увеличивает запас items
        pass

    @abstractmethod
    def remove(self, product, amount):  # уменьшает запас items
        pass

    @abstractmethod
    def get_free_space(self):  # вернуть количество свободных мест
        pass

    @abstractmethod
    def get_items(self):  # возвращает содержание склада в словаре {товар: количество}
        pass

    @abstractmethod
    def get_unique_items_count(self):  # возвращает количество уникальных товаров
        pass
