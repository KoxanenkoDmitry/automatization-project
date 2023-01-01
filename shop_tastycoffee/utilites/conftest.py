import pytest


@pytest.fixture()
def start_and_end_tests():
    print("Тест запущен")
    yield
    print("Тест завершен")
