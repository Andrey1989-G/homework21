from class_request import Capitalize, Request
from class_shop import Shop
from class_store import Store

if __name__ == '__main__':
    print('Начинаем работу. Для выхода ввести "стоп"')
    command = input('Введите команду')
    while command != 'стоп':
        shop = Shop({})
        store = Store({})
        if command[0] == 'К':
            com_story = Capitalize(command).result()
            store.add(com_story[0], com_story[1])
            print("товар добавлен на склад")
            print(f"остаток на складе:")
            [print(f'{items} {keys}') for keys, items in store.get_items().items()]
        elif command[0] == 'Д':
            com_shop = Request(command).result()
            if com_shop[0] in [i for i in store.get_items()]:
                shop.add(com_shop[0], com_shop[1])
                store.remove(com_shop[0], com_shop[1])
                print("товар добавлен в магазин")
                print(f"остаток на складе:")
                [print(f'{items} {keys}') for keys, items in shop.get_items.items()]





