def dict_methods(data: dict) -> tuple[dict, dict, any]:
    """
    1. Обновить словарь, добавив пару 'd': 4
    2. Получить значение по ключу 'x', вернуть 0 если ключ не найден
    3. Удалить пару с ключом 'b' и вернуть значение

    >>> dict_methods({'a': 1, 'b': 2, 'c': 3})
    ({'a': 1, 'b': 2, 'c': 3, 'd': 4}, 0, 2)
    """
    pass


def dict_methods_2(data: dict) -> tuple[list, list, list]:
    """
    1. Получить список всех ключей
    2. Получить список всех значений
    3. Получить список пар (ключ, значение)

    >>> dict_methods_2({'a': 1, 'b': 2, 'c': 3})
    (['a', 'b', 'c'], [1, 2, 3], [('a', 1), ('b', 2), ('c', 3)])
    """
    pass


def dict_methods_3(data: dict) -> tuple[dict, dict, dict]:
    """
    1. Создать новый словарь с дефолтным значением 0 для ключей ['x', 'y', 'z']
    2. Установить значение 100 для ключа 'new_key', если его нет
    3. Очистить словарь полностью

    >>> dict_methods_3({'a': 1, 'b': 2})
    ({'x': 0, 'y': 0, 'z': 0}, {'a': 1, 'b': 2, 'new_key': 100}, {})
    """
    pass


def dict_methods_4(data: dict) -> tuple[dict, str, dict]:
    """
    1. Создать копию словаря
    2. Получить значение по ключу 'a', если ключ не найден вернуть строку 'Not found'
    3. Обновить словарь данными из другого словаря {'x': 10, 'y': 20}

    >>> dict_methods_4({'a': 1, 'b': 2})
    ({'a': 1, 'b': 2}, 1, {'a': 1, 'b': 2, 'x': 10, 'y': 20})
    """
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
