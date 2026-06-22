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

    def search(self, keyword: str) -> list:
        results = []
        for book in self.books:
            if keyword in book.title or keyword in book.author:
                results.append(book)
        return results

    def total_reading_time(self) -> int:
        total = 0
        for book in self.books:
            total += book.reading_time()
        return total

    def get_stats(self) -> dict:
        stats = {"Book": 0, "EBook": 0, "AudioBook": 0}
        for book in self.books:
            if type(book) is Book:
                stats["Book"] += 1
            elif type(book) is EBook:
                stats["EBook"] += 1
            elif type(book) is AudioBook:
                stats["AudioBook"] += 1
        return stats

def main():
    lib = Library("중앙 도서관")

    lib.add_book(Book("어린왕자", "생텍쥐페리", 96))
    lib.add_book(EBook("파이썬 입문", "점프 투 파이썬", 300, 2.4))
    lib.add_book(AudioBook("해리포터", "롤링", 223, 135))
    lib.add_book(EBook("코스모스", "칼 세이건", 365, 5.1))
    lib.add_book(AudioBook("사피엔스", "유발 하라리", 638, 312))

    print(lib)
    print(f"보유 도서: {len(lib)}권")
    print()

    new_book = Book("데미안", "헤르만 헤세", 215)
    lib.add_book(new_book)
    print("데미안" in lib)
    print("없는책" in lib)
    print()

    results = lib.search("파이썬")
    for book in results:
        print(book)
    print()

    lib.remove_book("어린왕자")
    print(f"삭제 후 보유 도서 수: {len(lib)}권")
    print()

    print(f"전체 예상 독서 시간: {lib.total_reading_time()}분")
    print()

    print(lib.get_stats())
    print()

    try:
        lib.add_book("이건 책이 아님")
    except TypeError as e:
        print(f"TypeError: {e}")

    try:
        lib.remove_book("없는 책")
    except ValueError as e:
        print(f"ValueError: {e}")
    print()

    sorted_books = sorted(lib.books)
    for book in sorted_books:
        print(book)


if __name__ == "__main__":
    main()
