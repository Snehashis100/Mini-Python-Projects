class Library:

    def __init__(self, lst, user):
        self.list_of_book = lst
        self.user = user
        self.owner_book_dict = {}
        print(f"Welcome {self.user} to our Library")

    def displayBook(self):
        if len(self.list_of_book) == 0:
            print("Currently the Library has no books...kindly add some to display")
        else:
            print("The Library has the following books:")
            for item in self.list_of_book:
                print(f"# {item}")

    def lendBook(self, book_name, user_name):
        if book_name in self.list_of_book:
            self.list_of_book.remove(book_name)
            print(f"You have lended {book_name}")
            self.owner_book_dict[book_name]=user_name
        else:
            print(f"Sorry currently this book has been lended by {self.owner_book_dict[book_name]}")

    def addBook(self, name):
        self.list_of_book.append(name)
        print("The Book has been added successfully thanks for your contribution")

    def returnBook(self, book):
        flag=False
        for key,value in self.owner_book_dict.items():
            if key==book:
                self.owner_book_dict.pop(book)
                self.list_of_book.append(book)
                flag=True
                break
        if flag:
            print("Thanks for returning the book")
        else:
            print("You have not even lended this book")

if __name__ == '__main__':
    saheb = Library([], 'Snehashis')
    flag=True
    while flag:
        inp = int(input("""    
            Enter 1 : to add books
            Enter 2 : to display books
            Enter 3 : to lend books
            Enter 4 : to return books
            Enter 5 : to exit 
            """))
        if inp == 1:
            book_name = input("Enter the name of the book you want ot add: ")
            saheb.addBook(book_name)
        elif inp == 2:
            saheb.displayBook()
        elif inp == 3:
            book_name = input("Enter the name of the book you want to lend: ")
            user_name = input("Enter your name: ")
            saheb.lendBook(book_name, user_name)
        elif inp == 4:
            book_name = input("Enter the name of the book you want to return: ")
            saheb.returnBook(book_name)
        else:
            flag=False
            print("Thanks for coming to our Library...")