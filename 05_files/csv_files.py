from typing import List, Dict, Tuple


def get_student_average(grades_file: str, student_id: int) -> float:
    """
    Вычислить средний балл студента по всем предметам

    Args:
        grades_file (str): путь к файлу с оценками
        student_id (int): ID студента

    Returns:
        float: средний балл студента

    Пример:
        Для студента с id=1 средний балл будет 88.5 (85 + 92) / 2
        Для студента с id=2 средний балл будет 81.5 (78 + 85) / 2
    """
    pass


def find_top_students(grades_file: str, students_file: str, subject: str) -> List[Tuple[str, int]]:
    """
    Найти топ-3 студента по указанному предмету

    Args:
        grades_file (str): путь к файлу с оценками
        students_file (str): путь к файлу со списком студентов
        subject (str): название предмета

    Returns:
        List[Tuple[str, int]]: список кортежей (имя студента, оценка), 
                              отсортированный по убыванию оценки

    Пример:
        [('Виктор', 95), ('Дмитрий', 90), ('Анна', 85)]
    """
    pass


def group_students_by_performance(grades_file: str, students_file: str) -> Dict[str, List[str]]:
    """
    Сгруппировать студентов по успеваемости

    Args:
        grades_file (str): путь к файлу с оценками
        students_file (str): путь к файлу со списком студентов

    Returns:
        Dict[str, List[str]]: словарь, где ключи - уровни успеваемости, 
                             значения - списки имен студентов

    Критерии оценки:
        "Отлично" - средний балл >= 90
        "Хорошо" - средний балл >= 80 и < 90
        "Удовлетворительно" - средний балл < 80

    Пример:
        {
            'Отлично': ['Дмитрий', 'Виктор'],
            'Хорошо': ['Анна', 'Борис'],
            'Удовлетворительно': ['Галина']
        }
    """
    pass


def add_student_grade(grades_file: str, student_id: int,
                     subject: str, grade: int, date: str) -> None:
    """
    Добавить новую оценку для студента

    Args:
        grades_file (str): путь к файлу с оценками
        student_id (int): ID студента
        subject (str): название предмета
        grade (int): оценка
        date (str): дата в формате YYYY-MM-DD

    Пример:
        При вызове add_student_grade('grades.csv', 1, 'Chemistry', 94, '2024-02-03')
        в файл grades.csv должна добавиться новая строка с этими данными
    """
    pass


def calculate_group_stats(grades_file: str, students_file: str) -> Dict[str, Dict[str, float]]:
    """
    Рассчитать статистику по группам

    Args:
        grades_file (str): путь к файлу с оценками
        students_file (str): путь к файлу со списком студентов

    Returns:
        Dict[str, Dict[str, float]]: словарь с статистикой по каждой группе

    Пример:
        {
            'A1': {'avg': 90.0, 'max': 95, 'min': 85},
            'B1': {'avg': 81.0, 'max': 85, 'min': 78},
            'A2': {'avg': 92.0, 'max': 94, 'min': 90}
        }
    """
    pass


if __name__ == "__main__":
    pass