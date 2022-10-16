
from class_store import Store


class Shop(Store):
    def __init__(self, items: dict, capacity=20):
        super().__init__(items, capacity)
        self.items = items
        if items:
            self.capacity = sum([i for i in items.values()])
        if self.capacity < 0 or self.capacity > 20:
            raise ValueError("допустимый объем 20")
        if len(items) > 5 or len(items) < 0:
            raise ValueError("недопустимое количество наименований")

    def add(self, name: str, quantity: int):
        """увеличивает запас items"""
        for key, value in self.items.items():
            if key == name and self.capacity + quantity <= 20:
                self.items[name] = value + quantity
                self.capacity = self.capacity + quantity
                break
            else:
                raise Exception("допустимый объем 20")

    # def remove(self, name: str, quantity: int):
    #     """уменьшает запас items"""
    #     for key, value in self.items.items():
    #         if key == name and value - quantity >= 0:
    #             self.items[name] = value - quantity
    #             self.capacity = self.capacity - quantity
    #             break
    #         else:
    #             raise Exception("недопустимый объем")
    #
    # def get_free_space(self):
    #     """Возвращает количество свободных мест"""
    #     return self.capacity
    #
    # def get_items(self) -> dict:
    #     """Возвращает содержание склада в словаре {товар: количество}"""
    #     return self.items
    #
    # def get_unique_items_count(self):
    #     """Возвращает количество уникальных товаров"""
    #     return len(self.items)

# r = {'питон': 5, 'пульт': 1, 'пут': 1, 'льт': 1, 'ьт': 1, 'ульт': 10}
#
# s = Shop(r)
#
# print(s.get_unique_items_count())
