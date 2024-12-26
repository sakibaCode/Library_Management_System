class Library:
    
    book_list = []

    @classmethod
    def entry_book(cls, book):
        
        cls.book_list.append(book)

    @classmethod
    def view_all_books(cls):
       
        if not cls.book_list:
            print("No books available in the library.")
        else:
            print("\nAvailable Books:")    
            for book in cls.book_list:
                book.view_book_info()


class Book:
    def __init__(self, book_id, title, author):

        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = True
        # Add the book to the library
        Library.entry_book(self)

    def borrow_book(self):

        if self.__availability:
            self.__availability = False
            print(f"\nYou borrowed: '{self.__title}' by {self.__author}.")
        else:
            print(f"The book '{self.__title}' is already borrowed.")

    def return_book(self):
      
        if not self.__availability:
            self.__availability = True
            print(f"The book '{self.__title}' has been returned.")
        else:
            print(f"The book '{self.__title}' was not borrowed.")

    def view_book_info(self):
        """Displays the book's details."""
        availability_status = "Available" if self.__availability else "Not Available"
        print(f"ID: {self.__book_id}, Title: {self.__title}, Author: {self.__author}, Status: {availability_status}")


def main():

    Book(1, "The Forty Rules of Love", "Elif Shafak")
    Book(2, "Harry Potter", "J.K. Rowling")
    Book(3, "Pride and Prejudice", "Jane Austen")

    while True:
        print("\nLibrary Management System")
        print("1. View All Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            Library.view_all_books()
        elif choice == "2":
            try:
                book_id = int(input("Enter the book ID to borrow: "))
                book = next((b for b in Library.book_list if b._Book__book_id == book_id), None)
                if book:
                    book.borrow_book()
                else:
                    print("Invalid book ID.")
            except ValueError:
                print("Please enter a valid numeric book ID.")
        elif choice == "3":
            try:
                book_id = int(input("Enter the book ID to return: "))
                book = next((b for b in Library.book_list if b._Book__book_id == book_id), None)
                if book:
                    book.return_book()
                else:
                    print("Invalid book ID.")
            except ValueError:
                print("Please enter a valid numeric book ID.")
        elif choice == "4":
            print("Exiting the Library Management System.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
