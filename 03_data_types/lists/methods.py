def list_manipulation(numbers: list) -> tuple[list, list, list]:
    """
    1. Добавить число 4 в конец списка
    2. Добавить числа [5, 6] к результату первого списка
    3. Удалить последний элемент из результата второго списка

    >>> list_manipulation([1, 2, 3])
    ([1, 2, 3, 4], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5])
    """
    pass


def list_modification(fruits: list) -> tuple[list, list, list]:
    """
    1. Вставить 'banana' на позицию с индексом 1
    2. Удалить первое вхождение 'apple'
    3. Очистить список полностью

    >>> list_modification(['apple', 'orange', 'apple', 'pear'])
    (['apple', 'banana', 'orange', 'apple', 'pear'], ['banana', 'orange', 'apple', 'pear'], [])
    """
    pass


def list_counting(numbers: list) -> tuple[int, int, list]:
    """
    1. Посчитать количество вхождений числа 2
    2. Найти индекс первого вхождения числа 2
    3. Развернуть список

    >>> list_counting([1, 2, 3, 2, 4, 2, 5])
    (3, 1, [5, 2, 4, 2, 3, 2, 1])
    """
    pass


def list_sorting_example(words: list) -> tuple[list, list, list]:
    """
    1. Отсортировать список по возрастанию
    2. Отсортировать список по убыванию
    3. Отсортировать список по длине слов

    >>> list_sorting_example(['python', 'java', 'c++', 'javascript'])
    (['c++', 'java', 'javascript', 'python'], ['python', 'javascript', 'java', 'c++'], ['c++', 'java', 'python', 'javascript'])
    """
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
