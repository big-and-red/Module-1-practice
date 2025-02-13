def check_number_sign(number: int) -> str:
    """
    Определить знак числа (положительное, отрицательное или ноль)
    >>> check_number_sign(5)
    'positive'
    >>> check_number_sign(-3)
    'negative'
    >>> check_number_sign(0)
    'zero'
    """
    pass


def grade_calculator(score: int) -> str:
    """
    Определить оценку по баллам:
    90-100: 'A'
    80-89: 'B'
    70-79: 'C'
    60-69: 'D'
    0-59: 'F'
    >>> grade_calculator(95)
    'A'
    >>> grade_calculator(75)
    'C'
    """
    pass


def check_leap_year(year: int) -> bool:
    """
    Определить является ли год високосным
    Условия:
    - делится на 4
    - не делится на 100
    - или делится на 400
    >>> check_leap_year(2020)
    True
    >>> check_leap_year(2100)
    False
    """
    pass


def max_of_three(a: int, b: int, c: int) -> int:
    """
    Найти максимальное из трех чисел используя условные операторы
    >>> max_of_three(1, 5, 2)
    5
    >>> max_of_three(10, 2, 15)
    15
    """
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
