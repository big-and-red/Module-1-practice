def get_string_info(text: str) -> tuple[int, str, str]:
    """
    Вернуть длину строки, первый и последний символы
    >>> get_string_info('Python')
    (6, 'P', 'n')
    """
    pass


def concatenate_and_multiply(str1: str, str2: str, n: int) -> str:
    """
    Соединить две строки и повторить n раз
    >>> concatenate_and_multiply('Hello', 'World', 2)
    'HelloWorldHelloWorld'
    """
    pass


def get_substring(text: str, start: int, end: int) -> str:
    """
    Получить подстроку из строки по индексам
    >>> get_substring('Python', 1, 4)
    'yth'
    """
    pass


def get_middle_chars(text: str) -> str:
    """
    Вернуть средний символ строки (если длина нечётная) или два средних символа (если длина чётная)
    >>> get_middle_chars('Python')
    'th'
    >>> get_middle_chars('Java')
    'a'
    """
    pass


def count_characters(text: str) -> dict:
    """
    Подсчитать количество каждого символа в строке
    >>> count_characters('hello')
    {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    """
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
