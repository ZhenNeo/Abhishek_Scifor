class Book:
    def __init__(self, book_id, title, price):
        self.book_id = book_id
        self.title = title
        self.price = price

class Bookstore:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book has been added.")

    def get_book_by_id(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
                
    def get_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
                    
    def get_book_by_price(self, price):
        for book in self.books:
            if book.price == price:
                return book
                    
    def show_all_books(self):
        if self.books:
            print("All books in the bookstore: ")
            for book in self.books:
                print(f"Book ID : {book.book_id}, Title : {book.title}, Price : {book.price}")
        else:
            print("No books available in the store")

    def delete_book(self, book_info):
        if isinstance(book_info, int):
            for book in self.books:
                if book.book_id == book_info:
                    self.books.remove(book)
                    print("Book has been Deleted")
                    return
            print("Book not found")
        elif isinstance(book_info, str):
            for book in self.books:
                if book.title == book_info:
                    self.books.remove(book)
                    print("Book has been deleted")
                    return
            print("Book not found")
        elif isinstance(book_info, float):
            for book in self.books:
                if book.price == book_info:
                    self.books.remove(book)
                    print("Book Deleted successfully")
                    return
            print("Book not found")
        else:
            print("invalid Input")
        

if __name__ == "__main__":
    bookstore = Bookstore()

    book1 = Book(1, "Lord of the Rings", 200.0)
    book2 = Book(2, "Song of Ice and Fire", 250.50)
    book3 = Book(3, "White Nights", 300.18)

    bookstore.add_book(book1)
    bookstore.add_book(book2)
    bookstore.add_book(book3)

    bookstore.show_all_books()   

    found = bookstore.get_book_by_id(2)
    if found:
        print(f"Book found : {found.title}")
    else:
        print("No book Found")

    book_found = bookstore.get_book_by_price(200.0)
    if book_found:
        print(f"Book : {book_found.title}")

    book_found1 = bookstore.get_book_by_title("White Nights")
    if book_found1:
        print(f"Book : {book_found1.title}")