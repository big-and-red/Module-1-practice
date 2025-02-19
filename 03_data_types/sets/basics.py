def find_common_elements(list1: list, list2: list) -> set:
    """
    Найти общие элементы двух списков, исключив дубликаты
    >>> find_common_elements([1, 2, 2, 3], [2, 3, 3, 4])
    {2, 3}
    """
    pass


def get_unique_chars(text: str) -> set:
    """
    Получить множество уникальных символов из строки
    >>> get_unique_chars('hello world')
    {'h', 'e', 'l', 'o', 'w', 'r', 'd', ' '}
    """
    pass


def symmetric_difference_multiple(*args) -> set:
    """
    Найти симметрическую разность нескольких множеств
    >>> symmetric_difference_multiple({1, 2, 3}, {3, 4, 5}, {5, 6, 1})
    {2, 4, 6}
    """
    pass


def is_subset_of_any(set1: set, sets_list: list) -> bool:
    """
    Проверить, является ли множество подмножеством хотя бы одного множества из списка
    >>> is_subset_of_any({1, 2}, [{1, 2, 3}, {4, 5, 6}])
    True
    """
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
