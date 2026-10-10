import sqlite3

db=sqlite3.connect("library.db")
db.execute("""CREATE TABLE IF NOT EXISTS books(
 id INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT,author TEXT,
 issued INTEGER DEFAULT 0, borrower TEXT)""")
db.commit()

def add_book():
    db.execute("INSERT INTO books(title,author) VALUES(?,?)",
               (input("Title: "),input("Author: "))); db.commit()

def show():
    for b in db.execute("SELECT * FROM books"): print(b)

def issue():
    bid=int(input("Book ID: "))
    db.execute("UPDATE books SET issued=1,borrower=? WHERE id=?",
               (input("Borrower: "),bid)); db.commit()

def return_book():
    db.execute("UPDATE books SET issued=0,borrower=NULL WHERE id=?",
               (int(input("Book ID: ")),)); db.commit()

while True:
    print("\n1 Add 2 List 3 Issue 4 Return 5 Exit")
    c=input("> ")
    if c=="1": add_book()
    elif c=="2": show()
    elif c=="3": issue()
    elif c=="4": return_book()
    elif c=="5": break
