from abc import ABC, abstractmethod


class Storage(ABC):
    def __init__(self, items: dict, capacity: int):
        self.items = items
        self.capacity = capacity

    @property
    @abstractmethod
    def add(self, name: str, quantity: int):
        """увеличивает запас items"""
        pass
        # for key, value in self.items.items():
        #     if key == name:
        #         self.items[name] = value + quantity

    @property
    @abstractmethod
    def remove(self, name: str, quantity: int):
        """уменьшает запас items"""
        pass
        # for key, value in self.items.items():
        #     if key == name:
        #         self.items[name] = value - quantity

    @property
    @abstractmethod
    def get_free_space(self):
        """Возвращает количество свободных мест"""
        # return self.capacity
        pass

    @property
    @abstractmethod
    def get_items(self) -> dict:
        """Возвращает содержание склада в словаре {товар: количество}"""
        # return self.items
        pass

    @property
    @abstractmethod
    def get_unique_items_count(self):
        """Возвращает количество уникальных товаров"""
        # return len(self.items)
        pass
