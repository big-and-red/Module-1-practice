from typing import List, Dict, Tuple, Any


def count_word_frequency(filename: str) -> Dict[str, int]:
    """
    Подсчитать частоту встречаемости слов в тексте

    Args:
        filename (str): путь к текстовому файлу

    Returns:
        Dict[str, int]: словарь с количеством употреблений каждого слова

    Пример:
        count_word_frequency('article.txt')
        # Вернёт:
        # {
        #     'искусственный': 2,
        #     'интеллект': 2,
        #     'ии': 3,
        #     ...
        # }
    """
    pass


def parse_log_by_level(filename: str) -> Dict[str, List[str]]:
    """
    Сгруппировать записи лога по уровню события

    Args:
        filename (str): путь к файлу лога

    Returns:
        Dict[str, List[str]]: словарь, где ключ - уровень события,
                             значение - список сообщений

    Пример:
        parse_log_by_level('log.txt')
        # Вернёт:
        # {
        #     'INFO': ['Система запущена', 'Загрузка конфигурации', ...],
        #     'ERROR': ['Ошибка подключения к базе данных', ...],
        #     'WARNING': ['Не найден файл настроек'],
        #     'SUCCESS': ['Подключение установлено', ...]
        # }
    """
    pass


def extract_book_info(filename: str) -> List[Dict[str, Any]]:
    """
    Извлечь информацию о книгах из текстового файла

    Args:
        filename (str): путь к файлу с информацией о книгах

    Returns:
        List[Dict[str, Any]]: список словарей с информацией о каждой книге

    Пример:
        extract_book_info('books.txt')
        # Вернёт:
        # [
        #     {
        #         'название': 'Война и мир',
        #         'автор': 'Лев Толстой',
        #         'год': 1869,
        #         'страниц': 1225
        #     },
        #     ...
        # ]
    """
    pass


def find_lines_with_date(filename: str) -> List[Tuple[str, str]]:
    """
    Найти все строки, содержащие дату в формате YYYY-MM-DD

    Args:
        filename (str): путь к текстовому файлу

    Returns:
        List[Tuple[str, str]]: список кортежей (дата, строка)

    Пример:
        find_lines_with_date('log.txt')
        # Вернёт:
        # [
        #     ('2024-02-20', '2024-02-20 08:30:15 INFO: Система запущена'),
        #     ('2024-02-20', '2024-02-20 08:30:16 INFO: Загрузка конфигурации'),
        #     ...
        # ]
    """
    pass


def analyze_text_statistics(filename: str) -> Dict[str, int]:
    """
    Собрать статистику по тексту

    Args:
        filename (str): путь к текстовому файлу

    Returns:
        Dict[str, int]: словарь со статистикой

    Пример:
        analyze_text_statistics('article.txt')
        # Вернёт:
        # {
        #     'строк': 12,
        #     'слов': 98,
        #     'символов': 548,
        #     'предложений': 15,
        #     'абзацев': 4
        # }
    """
    pass


if __name__ == "__main__":
    pass
