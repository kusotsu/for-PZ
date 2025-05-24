def analyze_stores(stores: dict[str, set[str]]):
    """
    Принимает dict: {назв_магазина: set(товары)}.
    Возвращает три списка магазинов по заданным условиям.
    """
    no_salt = [name for name, goods in stores.items() if 'соль' not in goods]
    milk_and_cheese = [
        name for name, goods in stores.items()
        if 'молоко' in goods and 'сыр' in goods
    ]
    meat_and_milk = [
        name for name, goods in stores.items()
        if 'мясо' in goods and 'молоко' in goods
    ]

    return no_salt, milk_and_cheese, meat_and_milk


if __name__ == '__main__':
    magnit        = {'молоко', 'соль', 'сахар', 'печенье', 'сыр'}
    pyaterochka   = {'мясо', 'молоко', 'сыр'}
    perekrestok   = {'молоко', 'творог', 'сыр', 'сахар', 'печенье'}
    lenta         = {'печенье', 'молоко', 'сыр'}

    stores = {
        'Магнит':       magnit,
        'Пятерочка':    pyaterochka,
        'Перекресток':  perekrestok,
        'Лента':        lenta,
    }

    no_salt, milk_and_cheese, meat_and_milk = analyze_stores(stores)

    print('Магазины без соли:', no_salt)
    print('С молоком и сыром:', milk_and_cheese)
    print('С мясом и молоком:', meat_and_milk)
