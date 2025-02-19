def greeting() -> str:
    """
    Создать функцию, которая печатает приветствие
    >>> greeting()
    'Hello, World!'
    """
    return 'Hello, World!'


def calculate_square(number: int) -> int:
    """
    Создать функцию, которая принимает число и возвращает его квадрат
    >>> calculate_square(4)
    16
    """
    return number ** 2


def check_number(number: int) -> str:
    """
    Создать функцию, которая определяет положительное число или отрицательное
    >>> check_number(-5)
    'negative'
    >>> check_number(10)
    'positive'
    """
    return 'negative' if number < 0 else 'positive'


def print_info(name: str, age: int) -> str:
    """
    Создать функцию, которая печатает информацию о человеке (имя и возраст)
    >>> print_info('Alex', 25)
    'Name: Alex, Age: 25'
    """
    return f'Name: {name}, Age: {age}'


def calculate_sum(a: int, b: int, c: int) -> int:
    """
    Создать функцию, которая считает сумму трех чисел
    >>> calculate_sum(1, 2, 3)
    6
    """
    return a + b + c


if __name__ == "__main__":
    import doctest

    doctest.testmod()
