"""
Модуль для чтения CSV-файлов
"""

import csv


def read_csv_files(file_paths):
    """Чтение данных из нескольких CSV-файлов"""
    if not file_paths:
        raise ValueError("Не указаны файлы для чтения")

    all_data = []

    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                file_data = list(reader)
                if not file_data:
                    raise ValueError(f"Файл {file_path} пустой")
                all_data.extend(file_data)
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл не найден: {file_path}")
        except Exception as e:
            raise Exception(f"Ошибка чтения файла {file_path}: {e}")

    return all_data
