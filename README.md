# Тестируемое приложение: BookCollector.
### Функции класса
- Добавление новой книги (`add_new_book`)
- Установка жанра для книги (`set_book_genre`)
- Получение жанра книги (`get_book_genre`)
- Получение списка книг по жанру (`get_books_with_specific_genre`)
- Получение всех книг и их жанров (`get_books_genre`)
- Получение списка книг, предназначенных для детей (`get_books_for_children`)
- Добавление книги в список избранных (`add_book_in_favorites`)
- Удаление книги из списка избранных (`delete_book_from_favorites`)
- Получение списка избранных книг (`get_list_of_favorites_books`)

## Тесты

#### 1.Проверка добавления книги с валидным именем в рамках ГЗ (`test_add_new_book_name_is_valid`)
#### 2.Проверка добавления книги с невалидным именем за пределами ГЗ (`test_add_new_book_name_is_not_valid`)
#### 3.Проверка что нельзя установить жанр книги которой нет в коллекции (`test_set_book_genre_to_non_existent_book`)
#### 4.Проверка получения жанра по имени книги (`test_get_book_genre_return_correct_genre`)
#### 5.Проверка фильтрации книг по определённому жанру (`test_get_books_with_specific_genre_filters_correctly`)
#### 6.Проверка на пустой словарь книг с жанром (`test_get_books_genre_is_empty_initially`)
#### 7.Проверка что словарь книг с жанром не пустой (`test_get_books_genre_has_items`)
#### 8.Проверка что книги для детей не содержат жанры из списка age_raiting (`test_get_books_for_children_excludes_genres`)
#### 9.Проверка добавления книг в избранное (`test_add_book_in_favorites_adds_existing_book`)
#### 10.Проверка удаления книг из избранного (`test_delete_book_from_favorites_removes_book`)
#### 11.Проверка на пустой список Избранного (`test_get_list_of_favorites_books_is_empty_initially`)
#### 12.Проверка что список Избранного не пуст (`test_get_list_of_favorites_books`)
