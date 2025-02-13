def convert_types(number_str: str) -> tuple[int, float, bool]:
    """
    Конвертировать строку в различные типы данных
    >>> convert_types('123')
    (123, 123.0, True)
    >>> convert_types('0')
    (0, 0.0, False)
    """
    return


def get_variable_type(value: any) -> str:
    """
    Определить тип переменной
    >>> get_variable_type(123)
    'int'
    get_variable_type('hello')
    'str'
    """
    pass


def swap_variables(a: int, b: int) -> tuple[int, int]:
    """
    Поменять значения переменных местами без использования временной переменной
    >>> swap_variables(5, 10)
    (10, 5)
    """
    pass


def format_string(name: str, age: int) -> str:
    """
    Форматирование строки используя f-strings
    >>> format_string('John', 25)
    'My name is John and I am 25 years old'
    """
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
