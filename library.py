class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def reading_time(self) -> int:
        return int(self.pages * 1.5)

    def __lt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages < other.pages

    def __str__(self):
        return f"📖 {self.title} - {self.author} ({self.pages}p)"


class EBook(Book):
    def __init__(self, title: str, author: str, pages: int, file_size: float):
        super().__init__(title, author, pages)
        self.file_size = file_size

    def __str__(self):
        return f"📱 {self.title} - {self.author} ({self.pages}p, {self.file_size}MB)"


class AudioBook(Book):
    def __init__(self, title: str, author: str, pages: int, duration: int):
        super().__init__(title, author, pages)
        self.duration = duration

    def reading_time(self) -> int:
        return self.duration

    def __str__(self):
        return f"🎧 {self.title} - {self.author} ({self.duration}분)"


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []

    def __str__(self) -> str:
        return f"[{self.name}] 보유 도서 {len(self.books)}권"

    def __len__(self) -> int:
        return len(self.books)

    def __contains__(self, title: str) -> bool:
        for book in self.books:
            if book.title == title:
                return True
        return False

def add_book(self, book: Book):
        if not isinstance(book, Book):
            raise TypeError("Book 인스턴스만 추가할 수 있습니다.")
        self.books.append(book)

    def remove_book(self, title: str):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return
        raise ValueError(f"'{title}' 제목의 도서를 찾을 수 없습니다.")
