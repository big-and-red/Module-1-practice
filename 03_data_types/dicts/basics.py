def invert_dict(data: dict) -> dict:
    """
    Инвертировать словарь (поменять местами ключи и значения)
    >>> invert_dict({'a': 1, 'b': 2, 'c': 3})
    {1: 'a', 2: 'b', 3: 'c'}
    """
    pass


def nested_get(data: dict, path: str) -> any:
    """
    Получить значение из вложенного словаря по строке пути
    >>> nested_get({'a': {'b': {'c': 1}}}, 'a/b/c')
    1
    """
    pass


def count_values(data: dict) -> dict:
    """
    Подсчитать количество каждого значения в словаре
    >>> count_values({'a': 1, 'b': 2, 'c': 1, 'd': 1})
    {1: 3, 2: 1}
    """
    pass


def merge_dicts_with_sum(dict1: dict, dict2: dict) -> dict:
    """
    Объединить два словаря, суммируя значения для одинаковых ключей
    >>> merge_dicts_with_sum({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
    {'a': 1, 'b': 5, 'c': 4}
    """
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
