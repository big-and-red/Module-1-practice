"""Писать реализацию через цикл for"""


def sum_range(start: int, end: int) -> int:
    """
    Вычислить сумму чисел в диапазоне от start до end включительно
    >>> sum_range(1, 5)
    15
    >>> sum_range(2, 4)
    9
    """
    pass


def factorial(n: int) -> int:
    """
    Вычислить факториал числа n используя for
    >>> factorial(5)
    120
    >>> factorial(0)
    1
    """
    pass


def count_vowels(text: str) -> int:
    """
    Подсчитать количество гласных букв в строке
    >>> count_vowels('hello')
    2
    >>> count_vowels('AEIOU')
    5
    """
    pass


def find_divisors(number: int) -> list[int]:
    """
    Найти все делители числа
    >>> find_divisors(12)
    [1, 2, 3, 4, 6, 12]
    >>> find_divisors(7)
    [1, 7]
    """
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
