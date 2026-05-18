from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit
- 's' to search for a book
- 'u' to update a book's details

Your choice: """


def menu():
   
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        elif user_input == 's':
            prompt_search_book()
        elif user_input == 'u':
            prompt_update_book()
        else:
            print("Unknown command. Please try again.")

        user_input = input(USER_CHOICE)



def prompt_add_book():
    name = input('Enter the new book name: ')
    author = input('Enter the new book author: ')
    price = input('Enter the new book price: ')
    description = input('Enter the new book description: ')

    database.insert_book(name, author, price, description)      


def list_books():
    for book in database.get_all_books():
        read = 'YES' if book['read'] else 'NO'  
        print(f"{book['name']} by {book['author']} — Read: {read}")


def prompt_read_book():
    name = input('Enter the name of the book you just finished reading: ')

    database.mark_book_as_read(name)


def prompt_delete_book():
    name = input('Enter the name of the book you wish to delete: ')

    database.delete_book(name)
def prompt_search_book(): 
    name = input('Enter the name of the book you wish to search for: ')
    book = database.search_book(name)
    if book:
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']} — Read: {read}")
    else:
        print("Book not found.")
def prompt_update_book():
    name = input('Enter the name of the book you wish to update: ')
    new_name = input('Enter the new name of the book (leave blank to keep unchanged): ')
    new_author = input('Enter the new author of the book (leave blank to keep unchanged): ')
    new_price = input('Enter the new price of the book (leave blank to keep unchanged): ')
    new_description = input('Enter the new description of the book (leave blank to keep unchanged): ')

    if database.update_book(name, new_name, new_author, new_price, new_description):
        print("Book updated successfully.")
    else:
        print("Book not found.")    


menu()
