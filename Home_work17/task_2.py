class Library:
    def __init__(self, name):
        self.name = name
        self.books = []   # Список для хранения экземпляров Book
        self.authors = []   # Список для хранения экземпляров Author

    def new_book(self, title, year, author):
        book = Book(title, year, author)  # Создаём книгу
        self.books.append(book)  # Добавляем книгу в библиотеку
        author.books.append(book)  # Добавляем книгу в список автора
        return book  # Возвращаем созданную книгу

    def group_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year):
        return [book for book in self.books if book.year == year]


class Book:
    book_count = 0  # Переменная класса для подсчёта всех книг

    def __init__(self, title,year,author):
        self.title = title
        self.year = year
        self.author = author  # Должен быть объектом Author
        Book.book_count += 1  # Увеличиваем счётчик при создании книги

    def __repr__(self):
            return f"Book({self.title}, {self.year}, Author: {self.author.name})"

    def __str__(self):
            return f"'{self.title}' by {self.author.name} ({self.year})"


class Author:
    def __init__(self, name,country,birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []  # Список книг, написанных автором

    def __repr__(self):
        return f"Author({self.name}, {self.country})"

    def __str__(self):
        return f"{self.name} ({self.country})"


# Создаём автора
# 1. Создан объект класса Author с именем "Лев Толстой".
# 2. Список книг пока пуст.
leo_tolstoy = Author("Лев Толстой", "р_____я", "09.09.1828")

# Создаём библиотеку
# 1. Создан объект класса Library с именем "Государственная библиотека".
# 2. Списки `books` и `authors` пока пусты.
library = Library("Государственная библиотека")

# Добавляем автора в библиотеку
# 1. Мы добавили объект автора (leo_tolstoy) в список авторов библиотеки.
# 2. Теперь библиотека "знает", что Лев Толстой — один из её авторов.
library.authors.append(leo_tolstoy)

# Создаём книгу и добавляем её в библиотеку
# 1. Метод `new_book` создал объект книги с названием "Война и мир".
# 2. Добавил её в список книг библиотеки `library.books`.
# 3. Также добавил эту книгу в список книг автора `leo_tolstoy.books`.
war_and_peace = library.new_book("Война и мир", 1869, leo_tolstoy)

# Проверяем книги в библиотеке
print("Книги в библиотеке:", library.books)

# Проверяем книги автора
print("Книги автора Льва Толстого:", leo_tolstoy.books)

# Проверяем общее количество книг
print("Общее количество книг:", Book.book_count)
# 1. `library.books` содержит объект книги "Война и мир".
# 2. `leo_tolstoy.books` тоже содержит эту книгу.
# 3. Переменная класса `Book.book_count` показывает, сколько книг создано (сейчас это 1).

# Группируем книги по автору
# 1. Метод `group_by_author` ищет книги, у которых `book.author == leo_tolstoy`.
# 2. Возвращает список таких книг.
books_by_tolstoy = library.group_by_author(leo_tolstoy)
print("Книги Льва Толстого:", books_by_tolstoy)

# Группируем книги по году
# 1. Метод `group_by_year` ищет книги, у которых `book.year == 1869`.
# 2. Возвращает список таких книг.
books_in_1869 = library.group_by_year(1869)
print("Книги, изданные в 1869 году:", books_in_1869)
