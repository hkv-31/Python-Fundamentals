'''
Library Management System

1. Add book
2. Add member
3. Borrow book
4. View available books
'''

class Library:
    def __init__(self):
        self.books = [
            {"author": "J. K. Rowling", "title": "Harry Potter"},
            {"author": "Rick Riordan", "title": "Percy Jackson"},
            {"author": "Leigh Bardugo", "title": "Six of Crows"}
        ]

        self.members = [
            {"name": "Hetanshi"}
        ]

    def add_book(self):
        author = input("Add Author name")
        title = input("Add book title")
        self.books.append({"author": author, "title": title})
        print(f"{title}, Book added")

    def add_member(self):
        name = input("Enter your name to become a member")
        self.members.append(name)

    def show_books(self):
        for book in self.books:
            print(f"{book['title']} by {book['author']}")


class Borrow(Library):
    def borrow_book(self):
        name = input("Enter your name to borrow book")
        title = input("Enter nook title to borrow")
        for book in self.books:
            if book["title"] == title:
                self.books.remove(book)
                print(f"Removed: {title}")
                break


if __name__ == "__main__":
    obj = Borrow()
    obj.show_books()
    obj.add_book()
    obj.add_member()
    obj.borrow_book()
