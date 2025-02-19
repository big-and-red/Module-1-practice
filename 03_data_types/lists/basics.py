def create_list_operations(a: int, b: int, c: int) -> tuple[list, int, int]:
    """
    Создать список из трех чисел, вернуть список, максимальное и минимальное значения
    >>> create_list_operations(10, 20, 30)
    ([10, 20, 30], 30, 10)
    """
    pass


def list_slicing(numbers: list) -> tuple[list, list, list]:
    """
    Вернуть первые два элемента, последние два элемента и список в обратном порядке
    >>> list_slicing([1, 2, 3, 4, 5])
    ([1, 2], [4, 5], [5, 4, 3, 2, 1])
    """
    pass


def find_second_largest(numbers: list) -> int:
    """
    Найти второе самое большое число в списке
    >>> find_second_largest([1, 3, 5, 2, 4])
    4
    """
    pass


def remove_duplicates(numbers: list) -> list:
    """
    Удалить дубликаты из списка, сохранив порядок элементов
    >>> remove_duplicates([1, 2, 2, 3, 3, 3, 4])
    [1, 2, 3, 4]
    """
    pass


def group_by_type(items: list) -> dict:
    """
    Сгруппировать элементы списка по их типам
    >>> group_by_type([1, 'hello', 3.14, True, 2])
    {'int': [1, 2], 'str': ['hello'], 'float': [3.14], 'bool': [True]}
    """
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
