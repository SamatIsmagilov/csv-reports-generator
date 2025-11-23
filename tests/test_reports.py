"""
Тесты для модуля отчетов
"""

import pytest

from src.reports.performance import PerformanceReport


def test_performance_report():
    """Тест отчета performance"""
    test_data = [
        {'position': 'Backend Developer', 'performance': '4.8'},
        {'position': 'Frontend Developer', 'performance': '4.7'},
        {'position': 'Backend Developer', 'performance': '4.9'},
        {'position': 'Frontend Developer', 'performance': '4.5'},
    ]

    report = PerformanceReport(test_data)
    result = report.generate()

    # Проверяем, что результат содержит ожидаемые данные
    assert 'Backend Developer' in result
    assert 'Frontend Developer' in result
    assert '4.85' in result
    assert '4.6' in result


def test_performance_report_empty_data():
    """Тест с пустыми данными"""
    with pytest.raises(ValueError, match='Нет данных для генерации отчета'):
        report = PerformanceReport([])
        report.generate()


def test_performance_report_single_position():
    """Тест с одной позицией"""
    test_data = [
        {'position': 'Developer', 'performance': '4.8'},
        {'position': 'Developer', 'performance': '4.9'},
    ]

    report = PerformanceReport(test_data)
    result = report.generate()

    assert 'Developer' in result
    assert '4.85' in result
