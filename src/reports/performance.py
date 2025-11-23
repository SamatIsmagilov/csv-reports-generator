"""
Модуль для генерации отчета performance
"""

from collections import defaultdict

from src.reports.base import BaseReport


class PerformanceReport(BaseReport):
    """Отчет по эффективности сотрудников по позициям"""

    def generate(self):
        if not self.data:
            raise ValueError("Нет данных для генерации отчета")

        # Группировка данных по позициям
        position_data = defaultdict(list)

        for row in self.data:
            position = row['position']
            performance = float(row['performance'])
            position_data[position].append(performance)

        # Расчет средней эффективности и сортировка
        report_rows = []
        for position, performances in position_data.items():
            avg_performance = sum(performances) / len(performances)
            report_rows.append({
                'position': position,
                'performance': round(avg_performance, 2)
            })

        # Сортировка по убыванию эффективности
        report_rows.sort(key=lambda x: x['performance'], reverse=True)

        # Добавление нумерации
        numbered_rows = []
        for i, row in enumerate(report_rows, 1):
            numbered_rows.append([i, row['position'], row['performance']])

        return self.format_table(['#', 'position', 'performance'],
                                 numbered_rows)
