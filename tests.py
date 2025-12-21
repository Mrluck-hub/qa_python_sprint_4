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