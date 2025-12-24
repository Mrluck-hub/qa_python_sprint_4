import pytest

class TestBooksCollector:
   
    @pytest.mark.parametrize('name', [
        "a",
        "a"*40,
    ])     
    def test_add_new_book_name_is_valid(self, collector, name):
        collector.add_new_book(name)
        assert name in collector.books_genre

    @pytest.mark.parametrize('name', [
        "",
        "a"*41,
    ])     
    def test_add_new_book_name_is_not_valid(self, collector, name):
        collector.add_new_book(name)
        assert name not in collector.books_genre

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

    def test_add_book_in_favorites_adds_existing_book(self, collector):
        collector.add_new_book("Оса")
        collector.add_book_in_favorites("Оса")
        assert "Оса" in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_removes_book(self, collector):
        collector.add_new_book("Оса")
        collector.add_book_in_favorites("Оса")
        collector.delete_book_from_favorites("Оса")
        assert "Оса" not in collector.get_list_of_favorites_books()
