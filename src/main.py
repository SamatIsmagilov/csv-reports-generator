"""
Основной скрипт для генерации отчетов из CSV-файлов
"""

from src.cli import parse_arguments
from src.reports import ReportFactory
from src.utils.file_reader import read_csv_files


def main():
    """Основная функция скрипта"""
    args = parse_arguments()

    try:
        # Чтение данных из всех файлов
        data = read_csv_files(args.files)

        # Создание отчета
        report = ReportFactory.create_report(args.report, data)

        # Вывод отчета
        print(report.generate())

    except Exception as e:
        print(f"Ошибка: {e}")
        exit(1)


if __name__ == "__main__":
    main()
