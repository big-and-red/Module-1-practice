def tuple_methods(numbers: tuple) -> tuple[int, int, tuple]:
    """
    1. Посчитать сколько раз встречается число 2
    2. Найти индекс первого вхождения числа 3
    3. Создать новый кортеж с числом 5 в конце

    >>> tuple_methods((1, 2, 2, 3, 4, 2))
    (3, 3, (1, 2, 2, 3, 4, 2, 5))
    """
    pass


def tuple_slicing(data: tuple) -> tuple[tuple, tuple, tuple]:
    """
    1. Получить первые три элемента
    2. Получить элементы с конца в обратном порядке
    3. Получить каждый второй элемент

    >>> tuple_slicing((1, 2, 3, 4, 5, 6))
    ((1, 2, 3), (6, 5, 4, 3, 2, 1), (1, 3, 5))
    """
    pass


def tuple_operations(tuple1: tuple, tuple2: tuple) -> tuple[tuple, tuple, int]:
    """
    1. Соединить два кортежа
    2. Повторить кортеж три раза
    3. Получить длину результирующего кортежа

    >>> tuple_operations((1, 2), (3, 4))
    ((1, 2, 3, 4), (1, 2, 1, 2, 1, 2), 6)
    """
    pass


def tuple_conversions(data: list) -> tuple[tuple, tuple, tuple]:
    """
    1. Преобразовать список в кортеж
    2. Создать кортеж из строки
    3. Создать кортеж пар индекс-значение

    >>> tuple_conversions([1, 2, 3])
    ((1, 2, 3), ('1', '2', '3'), ((0, 1), (1, 2), (2, 3)))
    """
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
