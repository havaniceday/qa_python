import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2

        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # test 1 - check that it is impossible to add a book with empty title
    # or the book with a title longer than expected

    @pytest.mark.parametrize("book", ['',
                                      "The Enigmatic Chronicles of Serendipitous Adventures and Unexplored Mysteries Beyond the Realm of Imagination"])
    def test_add_new_book_title_empty_or_too_long_is_impossible(self, test_book_collector, book):
        test_book_collector.add_new_book(book)
        assert book not in test_book_collector.get_books_genre()

    #test 2 - check that it is impossible to add a book with the same title twice
    def test_add_new_book_already_existing_is_impossible(self, test_book_collector):
        test_book_collector.add_new_book('Дюна')
        assert list(test_book_collector.get_books_genre().keys()).count('Дюна') == 1

    #test 3 - check setting a valid book genre for existing book
    def test_set_book_genre_valid_input_genre_is_set(self, test_book_collector):
        test_book_collector.set_book_genre("Дюна", "Фантастика")
        assert test_book_collector.get_book_genre("Дюна") == "Фантастика"

    #test 4 check getting a book genre by its name
    def test_get_book_genre_existing_book_returns_genre(self, test_book_collector):
        for book_name, expected_genre in test_book_collector.books_genre.items():
            result_genre = test_book_collector.get_book_genre(book_name)
            assert result_genre == expected_genre

    #test 5 check getting  books list by genre and checking the list length
    def test_get_books_with_specific_genre_matching_genre_returns_books(self, test_book_collector):
        test_book_collector.add_new_book("Время")
        test_book_collector.add_new_book("Убик")
        test_book_collector.set_book_genre("Время", "Фантастика")
        test_book_collector.set_book_genre("Убик", "Фантастика")
        result_list = test_book_collector.get_books_with_specific_genre("Фантастика")
        assert len(result_list) == 3

    #test 6 check that the books_genre dictionnary is returned by getter
    def test_get_books_genre_returns_dictionary(self, test_book_collector):
        result = test_book_collector.get_books_genre()
        assert result == test_book_collector.books_genre

    #test 7 check that there are no adult books in list for children
    def test_get_books_for_children_adult_books_are_filtered(self, test_book_collector):
        result = test_book_collector.get_books_for_children()
        assert len(result) == 5
        assert test_book_collector.get_books_with_specific_genre("Ужасы") not in result and test_book_collector.get_books_with_specific_genre("Детектив") not in result

    #test 8 check adding not existing book to favourites is impossible
    @pytest.mark.parametrize("book", ['Война и мир', 'Гордость и Предубеждение', 'Красавица и Чудовище'])
    def test_add_book_in_favourites_not_existing_book_is_not_added(self, book, test_book_collector):
        test_book_collector.add_book_in_favorites(book)
        assert book not in test_book_collector.get_list_of_favorites_books()

    #test 9 check deleting existing books from favourites list
    @pytest.mark.parametrize("book", ['Дюна', 'Эркюль Пуаро'])
    def test_delete_book_from_favorites_existing_book_is_deleted(self, book, test_book_collector):
        test_book_collector.delete_book_from_favorites(book)
        assert book not in test_book_collector.get_list_of_favorites_books()


    #test 10 check adding existing book to favourites
    @pytest.mark.parametrize("book", ['Время', 'Убик'])
    def test_add_book_in_favourites_existing_book_is_added(self, book, test_book_collector):
        test_book_collector.add_book_in_favorites(book)
        assert book in test_book_collector.get_list_of_favorites_books()


    #test 11 check that favourites list is returned by getter
    def test_get_list_of_favourites_books_returns_list(self, test_book_collector):
        result = test_book_collector.get_list_of_favorites_books()
        assert result == test_book_collector.favorites
