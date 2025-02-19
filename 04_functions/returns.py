from typing import Dict, List, Tuple, Union, Any


def dict_return(name: str, age: int) -> Dict[str, Union[str, int]]:
    """
    Создать функцию, которая принимает имя и возраст,
    а возвращает словарь с ключами 'name' и 'age'

    >>> dict_return('Alex', 25)
    {'name': 'Alex', 'age': 25}
    """
    pass


def tuple_with_list_return(numbers: List[int]) -> Tuple[List[int], int, float]:
    """
    Создать функцию, которая возвращает кортеж,
    где первый элемент - список чисел,
    второй элемент - их сумма,
    третий элемент - их среднее значение

    >>> tuple_with_list_return([1, 2, 3, 4, 5])
    ([1, 2, 3, 4, 5], 15, 3.0)
    """
    pass


def list_of_tuples_return(names: List[str]) -> List[Tuple[str, int]]:
    """
    Создать функцию, которая принимает список имен,
    и возвращает список кортежей (имя, длина_имени)

    >>> list_of_tuples_return(['Alex', 'Emma', 'John'])
    [('Alex', 4), ('Emma', 4), ('John', 4)]
    """
    pass


def nested_dict_return(name: str, age: int, grades: List[int]) -> Dict[str, Dict[str, Any]]:
    """
    Создать функцию, которая принимает информацию о студенте
    и возвращает вложенный словарь с персональными данными и оценками

    >>> nested_dict_return('Alex', 20, [5, 4, 5])
    {'personal': {'name': 'Alex', 'age': 20}, 'grades': {'marks': [5, 4, 5], 'average': 4.67}}
    """
    pass


def combined_return(text: str) -> Tuple[int, List[str], Dict[str, int]]:
    """
    Создать функцию, которая анализирует текст и возвращает кортеж,
    содержащий длину текста, список слов и словарь частоты слов

    >>> combined_return('hello world hello')
    (16, ['hello', 'world', 'hello'], {'hello': 2, 'world': 1})
    """
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
