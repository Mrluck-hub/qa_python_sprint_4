import pytest

from main import BooksCollector

class TestBooksCollector:
    
    @pytest.fixture
    def collector(self):
        return BooksCollector()
    
    def test_init_books_genre_is_empty(self, collector):
        assert collector.books_genre == {}
    
    def test_add_new_book_name_length_40_is_added(self, collector):
        long_name = 'a'*40
        collector.add_new_book(long_name)
        assert long_name in collector.books_genre

    def test_set_book_genre_to_non_existent_book(self, collector):
        collector.set_book_genre('Несуществующая книга', 'Ужасы')
        assert 'Несуществующая книга' not in collector.get_books_genre()

    def test_get_book_genre_return_correct_genre(self, collector):
        collector.books_genre = {'Книга': 'Комедии'}
        assert collector.get_book_genre('Книга') == 'Комедии'

    def test_get_books_with_specific_genre_filters_correctly(self, collector):
        collector.books_genre = {
            'Книга 1': 'Фантастика',
            'Книга 2': 'Ужасы',
            'Книга 3': 'Фантастика'
        }
        assert collector.get_books_with_specific_genre('Фантастика') == ['Книга 1', 'Книга 3']

    def test_get_books_genre_is_empty_initially(self, collector):
        assert collector.get_books_genre() == {}

    def test_get_books_for_children_excludes_genres(self, collector):
        collector.books_genre = {
            'Шрек': 'Мультфильмы',
            'Оно': 'Ужасы',
            'Шерлок': 'Детективы',
            'Звёздные воины': 'Фантастика'
        }
        assert 'Шрек' in collector.get_books_for_children()
        assert 'Оно' not in collector.get_books_for_children()
        assert 'Шерлок' not in collector.get_books_for_children()
        assert 'Звёздные воины' in collector.get_books_for_children()
        