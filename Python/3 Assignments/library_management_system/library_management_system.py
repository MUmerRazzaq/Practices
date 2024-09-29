books = [
    {
        "id": "B001",
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Classic Fiction",
        "availability": "Checked Out"
    },
    {
        "id": "B002",
        "title": "1984",
        "author": "George Orwell",
        "genre": "Dystopian Fiction",
        "availability": "Available"
    },
    {
        "id": "B003",
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "genre": "Romantic Comedy",
        "availability": "Checked Out"
    },
    {
        "id": "B004",
        "title": "The Lord of the Rings",
        "author": "J.R.R. Tolkien",
        "genre": "High Fantasy",
        "availability": "Available"
    },
    {
        "id": "B005",
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "genre": "Philosophical Fiction",
        "availability": "Available"
    }
]
users = [
    {
        "id": "U001",
        "name": "John Doe",
        "borrowed_books": ["B001"]
    },
    {
        "id": "U002",
        "name": "Jane Smith",
        "borrowed_books": ["B002"]
    },
    {
        "id": "U003",
        "name": "Alice Johnson",
        "borrowed_books": ["B004"]
    }
]
def all_books():
    print("All Books:")
    for book in books:
        print(f"{book['id']}: {book['title']}, by {book['author']} in the genre {book['genre']} ({book['availability']})")

def available_books():
    print("Available Books:")
    for book in books:
        if book["availability"]=="Available":
            print(f"{book['id']}: {book['title']}, by {book['author']} in the genre {book['genre']} ({book['availability']})")
            
def unavailable_books():
    print("Checked Out Books:")
    for book in books:
        if book["availability"]=="Checked Out":
            print(f"{book['id']}: {book['title']}, by {book['author']} in the genre {book['genre']} ({book['availability']})")

def search_book():
    search_term=input("Please Enter Detail of book you want to search (ID,Title,Author,Genre): ").lower().strip()
    for book in books:
        if search_term in book['id'].lower() or search_term in book["title"].lower() or search_term in book["author"].lower() or search_term in book["genre"].lower():
            print(f"{book['id']}: {book['title']}, by {book['author']} in the genre {book['genre']} ({book['availability']})")

def borrow_book():
    user_id=input("Please Enter User ID: ")
    user_found=False
    for user in users:
        if user_id.capitalize() == user["id"]:
            user_found=True
            book_id=input("Please Enter the Book ID: ")
            book_found=False
            for book in books:                
                if book_id.capitalize() == book["id"]:
                    book_found=True
                    if book["availability"].lower()=="available":
                        book["availability"] ="Checked Out"
                        user["borrowed_books"].append(book["id"])
                        print(f"Book {book["id"]}, {book["title"]} is issued to User {user['id']}, {user["name"]}")
                    else:
                        print(f'Book {book["id"]}, {book["title"]} is Checked out')
                        break
            if not book_found:
                print("Book Not Found! Please View All Books To Confirm. ")
                break
    if not user_found:
        print("User not found!")   

def return_book():
    user_id=input("Please Enter User ID: ")
    user_found=False
    for user in users:
        if user_id.capitalize() == user["id"]:
            user_found=True
            book_id=input("Please Enter Book ID: ")
            book_found=False
            for book in books:                
                if book_id.capitalize() == book["id"]:
                    book_found=True
                    if book_id in user['borrowed_books']:
                        book["availability"]="Available"
                        user["borrowed_books"].remove(book_id)
                        print(f'{book["id"]}, {book["title"]} is Successfully returned form {user["id"]}, {user["name"]}')
                    elif book_id not in user["borrowed_books"]:
                        print(f"{book['id']}, {book['title']} is not issued to {user["id"]}, {user["name"]} ")
                        break
            if not book_found:
                print("Book Not Found! Please View All Books To Confirm. ")
                break
    if not user_found:
        print("User not found!")        

def all_users():
    for user in users:
        print(f"I'D: {user.get("id")}, Name:{user.get("name")}, Borrowed Books:{user.get("borrowed_books")}")

def register_user():
    user_id=input("Enter User Id:").capitalize().strip()
    for user in users:
        user_found=False
        if user_id == user["id"]:
            user_found=True
            print(f"{user_id} Already Exits, with User Name {user["name"]}")
            break
    if not user_found:
        user_name=input("Enter User Name").title().strip()
        new_user={
            "id":user_id,
            "name":user_name,
            "borrowed_books":[]
                    }
        users.append(new_user)
        print(f"New User Registered Successfully.\n ID: {user_id} Name: {user_name} ")
                        
def library_management_system():
    print("Welcome to the Community Library System! \n ______________________________________")
    while True:
        print('''  
                    1. View books
                    2. Search for a book
                    3. Borrow a book
                    4. Return a book
                    5. Users Management
                    6. Exit''')
        user_input=input("Please select the option number:")
        if user_input=="1":
            print('''
                     1. All Books
                     2. Available Books
                     3. Checked Out Books
                ''')
            user_input=input("Please select the option number:")
            if user_input=="1":
                all_books()
            elif user_input=="2":
                available_books()
            elif user_input=="3":
                unavailable_books()
            else:
                print("Invalid Input")
                
        elif user_input=="2":
            search_book()
        elif user_input=="3":
            borrow_book()
        elif user_input=="4":
            return_book()
        elif user_input=="5":
            print('''
                     1. View All Exiting User
                     2. Register New User
                ''')
            user_input=input("Please select the option number:")
            if user_input == "1":
                all_users()
            elif user_input == "2":
                register_user()
            else:
                print("Invalid Input")
        elif user_input=="6":
            print("Exiting the Library Management System.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


library_management_system()




            


        
