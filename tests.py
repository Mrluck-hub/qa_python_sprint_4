import pytest

from main import BooksCollector

class TestBooksCollector:
    
    @pytest.fixture
    def collector(self):
        return BooksCollector()
    
    def test_init_books_genre_is_empty(self, collector):
        assert collector.books_genre == {}
    