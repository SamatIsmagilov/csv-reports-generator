"""
Фабрика отчетов
"""

from .performance import PerformanceReport


class ReportFactory:
    """Фабрика для создания отчетов"""

    @staticmethod
    def create_report(report_name, data):
        report_classes = {
            'performance': PerformanceReport,
        }

        if report_name not in report_classes:
            raise ValueError(f"Неизвестный отчет: {report_name}")

        return report_classes[report_name](data)
