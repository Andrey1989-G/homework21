from class_storage import Storage


class Store(Storage):
    def __init__(self, items: dict, capacity=100):
        super().__init__(items, capacity)
        self.items = items
        # if (capacity - sum([i for i in items.values()])) > capacity:
        self.capacity = capacity - sum([i for i in items.values()])
        # raise ValueError("допустимый объем 100")

    def add(self, name: str, quantity: int):
        """увеличивает запас items"""
        for key, value in self.items.items():
            if key == name and self.capacity + quantity <= 100:
                self.items[name] = value + quantity
                self.capacity = self.capacity + quantity
                break
            else:
                raise Exception("допустимый объем 100")


    def remove(self, name: str, quantity: int):
        """уменьшает запас items"""
        for key, value in self.items.items():
            if key == name and self.capacity + quantity <= 100:
                self.items[name] = value + quantity
                self.capacity = self.capacity + quantity
                break
            else:
                raise Exception("допустимый объем 100")

    def get_free_space(self):
        """Возвращает количество свободных мест"""
        return self.capacity

    def get_items(self) -> dict:
        """Возвращает содержание склада в словаре {товар: количество}"""
        return self.items

    def get_unique_items_count(self):
        """Возвращает количество уникальных товаров"""
        return len(self.items)

