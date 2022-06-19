from replit import clear
class library:
    def __init__(self,list_of_books):
        self.books=list_of_books
        self.amount=0
    def display(self):
        print("Books Present in library are : ")
        for book in self.books:
            print("\t *"+book)
    def borrowBook(self,bookname):
        if bookname in self.books:
            print(f"You have been issued {bookname} . please keep it safe and return it within in 30 Days")
            self.books.remove(bookname)
            return True
        else:
            print("Sorry this book has been issued to someone else ,please wait until the book is returned")
            return False
    def return_book(self,bookName):
        days=int(input("no of days you have taken the book"))
        clear()
        self.track(days)
        self.books.append(bookName)
        print("Thanks for returning the book")
    def track(self,no_of_days):
        if(no_of_days<=30 and day>0):
            print("NO fine imposed")
        elif no_of_days>30:
            for i in range(31,no_of_days):
                self.amount+=1
            print(f"You have to pay this much {self.amount} amount ")
class student:
    def request(self):
        self.book=input("Enter the name of the book you want to borrow !")
        return self.book
    def return_book(self):
        self.book=input("Enter the name of the book you want to return !")
        return self.book
central_library=library(["python","java","Mysql","DBMS"])
studentobj=student()
while True:
    welcomemsg=''' ===     Welcome To Central Library === 
              please choose a option
              1.list all the books
              2.Request a book
              3.return a book
              4.exit the library
    '''
    print(welcomemsg)
    a=int(input("Enter a choose : "))
    print(welcomemsg)
    if(a==1):
        central_library.display()
    elif a==2:
        central_library.borrowBook(studentobj.request())
    elif a==3:
         central_library.return_book(studentobj.return_book())
    elif a==4:
        print("Thanks for choosing central library ")
        exit()
    else:
        print("Invalid choice")
