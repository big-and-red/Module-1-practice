def string_methods_1(text: str) -> tuple[str, str, str]:
    """
    Привести строку к верхнему регистру, нижнему регистру и капитализировать
    >>> string_methods_1('python')
    ('PYTHON', 'python', 'Python')
    """
    pass


def string_methods_2(text: str) -> tuple[str, str, bool]:
    """
    Удалить пробелы в начале и конце строки,
    заменить 'o' на 'a' и проверить, начинается ли строка с 'py'
    >>> string_methods_2('  python  ')
    ('python', 'pythan', True)
    """
    pass


def string_methods_3(text: str) -> tuple[list, int, bool]:
    """
    Разделить строку по пробелам,
    найти позицию первого 'a',
    проверить, состоит ли строка только из букв
    >>> string_methods_3('python java android')
    (['python', 'java', 'android'], 7, True)
    """
    pass


def string_methods_4(text: str) -> tuple[str, str, int]:
    """
    Соединить список слов через дефис,
    дополнить строку нулями слева до 8 символов,
    посчитать количество букв 'e' в строке
    >>> string_methods_4('hello test weekend')
    ('hello-test-weekend', '00000test', 4)
    """
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
