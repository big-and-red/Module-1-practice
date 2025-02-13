def arithmetic_operations(a: int, b: int) -> tuple[int, int, int, float]:
    """
    Выполнить базовые арифметические операции (+, -, *, /)
    >>> arithmetic_operations(10, 2)
    (12, 8, 20, 5.0)
    """
    pass


def comparison_operations(a: int, b: int) -> tuple[bool, bool, bool]:
    """
    Выполнить операции сравнения (>, <, ==)
    >>> comparison_operations(5, 3)
    (True, False, False)
    """
    pass


def logical_operations(a: bool, b: bool) -> tuple[bool, bool, bool]:
    """
    Выполнить логические операции (and, or, not)
    >>> logical_operations(True, False)
    (False, True, True)
    """
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
