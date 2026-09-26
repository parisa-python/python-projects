import json
books = [] 
def load_books():
    global books
    try:
        with open("books.json", "r") as file:
            books = json.load(file)
    except FileNotFoundError:
        books = []
def save_books():
    with open("books.json", "w") as file:
        json.dump(books, file, indent=4)   

def add_book():
    title = input("Book title: ")
    outher= input("outher: ")
    year= int(input("Year: "))
    book = {"title": title, "outher": outher, "year":year}
    books.append(book)
    save_books()
    print("Book added!")
def show_books():
    if not books:
        print("Not books found")
        return
    for number, book in enumerate(books, start=1):
        print(f"{number}, {book['title']} _ " f"{book['auther']} _ {book['year']}")   
def search_book():
    title = input("Enter book title: ").lower()
    for book in books:
        if title in book["title"].lower():
            print(book)
            return
    print("Book not found")    
    
def delete_book():
    name= input("Book name for delete: ")
    for book in books:
        if book["name"] == name:
            books.remove(book)
            print("Delete book") 
            return
        print("Not found book")
def update_book():
    if not books:
        print("No books found")
        return
    show_books()
    number = int(input("Enter book number: "))
    index = number - 1
    if 0<= index < len(books):
        books[index]["title"] =input("New title: ")
        books[index]["outhor"] = input("New author: ")
        books[index]["year"] = int(input("New year: "))
        save_books()
        print("Book updeted")
    else:
        print("Invalid number")    
load_books()       
while True:
    print("\n_ _ _ Library Management _ _ _")
    print("1. Add book")
    print("2. Show books") 
    print("3. Search book")
    print("4. Delete book")
    print("5. Update book")
    print("6. Exit") 
    choice = input("Choose: ") 
    if choice == "1":
        add_book()
    elif choice == "2":
        show_books() 
    elif choice == "3":
        search_book()
    elif choice == "4":
        delete_book()
    elif choice == "5":
        update_book()
    elif choice == "6":
        print("Goodbye!") 
        break
    else:                             
         print("Invalid choice")
