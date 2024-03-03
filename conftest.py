import pytest

from main import BooksCollector


@pytest.fixture(scope='session')
def test_book_collector():
    collector = BooksCollector()
    collector.books_genre = {
        'Дюна': '',
        'Кошмар на улице Вязов': 'Ужасы',
        'Эркюль Пуаро': 'Детективы',
        'Король Лев': 'Мультфильмы',
        'Золотой Теленок': 'Комедии'
    }

    collector.favorites = ['Дюна', 'Эркюль Пуаро']

    return collector




