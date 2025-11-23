"""
Базовый класс для всех отчетов
"""

from abc import ABC, abstractmethod

from tabulate import tabulate


class BaseReport(ABC):
    """Абстрактный базовый класс для отчетов"""

    def __init__(self, data):
        self.data = data

    @abstractmethod
    def generate(self):
        """Генерация отчета"""
        pass

    def format_table(self, headers, rows):
        """Форматирование данных в таблицу"""
        return tabulate(rows, headers=headers, tablefmt='grid', floatfmt=".2f")
