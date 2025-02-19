from typing import Dict, List, Tuple, Union, Any


def default_args(name: str) -> str:
    """
    Создать функцию с дефолтным значением
    >>> default_args()
    'Hello, Guest'
    >>> default_args('Alice')
    'Hello, Alice'
    """
    pass


def args_sum(*args: int) -> int:
    """
    Создать функцию, принимающую произвольное количество позиционных аргументов
    >>> args_sum(1, 2, 3)
    6
    >>> args_sum(1, 2, 3, 4, 5)
    15
    """
    pass


def kwargs_print(**kwargs: Any) -> Dict[str, Any]:
    """
    Создать функцию, принимающую именованные аргументы и печатающую их
    >>> kwargs_print(name='Alex', age=25)
    {'name': 'Alex', 'age': 25}
    """
    pass


def mixed_args(a: int, b: int, operation: str = 'add') -> int:
    """
    Создать функцию, использующую позиционные и именованные аргументы
    >>> mixed_args(1, 2, operation='add')
    3
    >>> mixed_args(10, 5, operation='subtract')
    5
    """
    pass


def validate_args(first: str, second: int) -> bool:
    """
    Создать функцию с проверкой типов аргументов
    >>> validate_args('hello', 5)
    True
    >>> validate_args(10, 'world')
    False
    """
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
