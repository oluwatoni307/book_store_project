exit_app = False
Books = []
def save_book():
    name = input("What is the name of the book")
    author = input("Who wrote the book")
    name = name.capitalize()
    author =  author.capitalize()
    book_status =  True
    book = {
        "name" : name,
        "author": author,
        "read": book_status
    }
    Books.append(book)

def retrieve_books(name):
    name = name.capitalize()
    for book in Books:
        if name == book["name"]:
            for key, value in book.items():
                print(f"{key}: {value}")

def markbook(name):
        name = name.capitalize()
        for book in Books:
            if name == book["name"]:
                book["read"]= True

def delete_record(name):
        name = name.capitalize()
        for book in Books:
            if name == book["name"]:
                 Books.remove(book)


        



    


while exit_app == False:
    prompt = """
Hello welcome to the book library
for Entering book details, pick 1
for retriving book details,pick 2
to mark book as read pick 3
to delete book pick 4
To Exit app pick 5
Pick A Number:   
"""
    answer = int(input(prompt))
    if answer == 1:
        save_book()
    elif answer == 2:
        name = input("name of book")
        retrieve_books(name)
    elif answer == 3:
        name = input("What is the name of the book")
        markbook(name)
    elif answer == 4:
        name = input("What is the name of the book you want delete")
        delete_record(name)
    elif answer == 5:
        print(" Thank you for visiting our library. you are welcome back anytime")
        exit_app = True
