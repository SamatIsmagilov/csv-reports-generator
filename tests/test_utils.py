"""
Тесты для утилит
"""

import os
import tempfile

import pytest

from src.utils.file_reader import read_csv_files


def test_read_csv_files():
    """Тест чтения CSV-файлов"""
    # Создаем временные файлы для тестирования
    csv_content1 = """name,position,performance
Alex,Developer,4.8"""

    csv_content2 = """name,position,performance
Maria,Designer,4.7"""

    with tempfile.NamedTemporaryFile(mode='w',
                                     suffix='.csv', delete=False) as f1:
        f1.write(csv_content1)
        file1 = f1.name

    with tempfile.NamedTemporaryFile(mode='w',
                                     suffix='.csv', delete=False) as f2:
        f2.write(csv_content2)
        file2 = f2.name

    try:
        data = read_csv_files([file1, file2])
        assert len(data) == 2
        assert data[0]['name'] == 'Alex'
        assert data[1]['name'] == 'Maria'
    finally:
        os.unlink(file1)
        os.unlink(file2)


def test_read_csv_files_not_found():
    """Тест с несуществующим файлом"""
    with pytest.raises(FileNotFoundError):
        read_csv_files(['nonexistent.csv'])
