"""
Вариант 11. Операции над множествами:
1. Магазины без соли
2. Магазины с молоком и сыром одновременно
3. Магазины с мясом и молоком одновременно
"""

def analyze_stores(stores: dict):
    """
    Принимает dict: {назв_магазина: set(товары)}.
    Выполняет три задачи и выводит списки магазинов.
    """
    no_salt = [name for name, goods in stores.items() if 'соль' not in goods]
    milk_and_cheese = [
        name for name, goods in stores.items()
        if {'молоко', 'сыр'}.issubset(goods)
    ]
    meat_and_milk = [
        name for name, goods in stores.items()
        if {'мясо', 'молоко'}.issubset(goods)
    ]

    print('Магазины, где нет соли:', no_salt)
    print('Магазины с молоком и сыром:', milk_and_cheese)
    print('Магазины с мясом и молоком:', meat_and_milk)


if __name__ == '__main__':
    stores = {
        'Магнит':    {'молоко', 'соль', 'сахар', 'печенье', 'сыр'},
        'Пятерочка': {'мясо', 'молоко', 'сыр'},
        'Перекресток': {'молоко', 'творог', 'сыр', 'сахар', 'печенье'},
        'Лента':     {'печенье', 'молоко', 'сыр'}
    }

    analyze_stores(stores)
