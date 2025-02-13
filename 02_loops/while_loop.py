"""Писать реализацию через цикл While"""


def find_digit_sum(number: int) -> int:
    """
    Найти сумму цифр числа
    >>> find_digit_sum(123)
    6
    >>> find_digit_sum(456)
    15
    """
    pass


def binary_search(number: int) -> int:
    """
    Найти количество попыток для угадывания числа (1-100) методом бинарного поиска
    >>> binary_search(50)  # число 50 будет угадано за 6 или менее попыток
    6
    >>> binary_search(1)   # число 1 будет угадано за 7 или менее попыток
    7
    """
    pass


def collatz_sequence_length(n: int) -> int:
    """
    Найти длину последовательности Коллатца
    (если n четное - делим на 2, если нечетное - умножаем на 3 и прибавляем 1)
    >>> collatz_sequence_length(13)
    10
    >>> collatz_sequence_length(6)
    9
    """
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
