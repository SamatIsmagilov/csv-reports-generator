"""
Модуль для обработки аргументов командной строки
"""

import argparse


def parse_arguments():
    """Парсинг аргументов командной строки"""
    parser = argparse.ArgumentParser(
        description='Генератор отчетов из CSV-файлов с данными сотрудников'
    )

    parser.add_argument(
        '--files',
        nargs='+',
        required=True,
        help='Пути к CSV-файлам с данными'
    )

    parser.add_argument(
        '--report',
        required=True,
        help='Название отчета для генерации'
    )

    return parser.parse_args()
