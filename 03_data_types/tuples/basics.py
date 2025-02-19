def sort_by_length(*args) -> tuple:
    """
    Сортировка кортежа строк по длине
    >>> sort_by_length('apple', 'banana', 'cherry', 'date')
    ('date', 'apple', 'cherry', 'banana')
    """
    pass


def find_coordinates(point1: tuple, point2: tuple) -> float:
    """
    Вычислить расстояние между двумя точками на плоскости
    >>> find_coordinates((0, 0), (3, 4))
    5.0
    """
    pass


def zip_elements(tuple1: tuple, tuple2: tuple) -> tuple:
    """
    Создать кортеж пар из двух кортежей
    >>> zip_elements((1, 2, 3), ('a', 'b', 'c'))
    ((1, 'a'), (2, 'b'), (3, 'c'))
    """
    pass


def aggregate_elements(numbers: tuple) -> tuple:
    """
    Вернуть кортеж с суммой, средним значением, минимумом и максимумом
    >>> aggregate_elements((1, 2, 3, 4, 5))
    (15, 3.0, 1, 5)
    """
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
