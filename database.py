books = []

def get_all_books():
    return books

def insert_book(name, author, price, description):
    books.append({'name': name, 'author': author, 'price': price, 'description': description, 'read': False})

def mark_book_as_read(name):
    for book in books:
        if book['name'] == name:
            book['read'] = True

def delete_book(name):
    global books
    books = [book for book in books if book['name'] != name]


def search_book(name):
    for book in books:
        if book['name'] == name:
            return book
    return None
def update_book(name, new_name=None, new_author=None, new_price=None, new_description=None):
    for book in books:
        if book['name'] == name:
            if new_name:
                book['name'] = new_name
            if new_author:
                book['author'] = new_author
            if new_price:
                book['price'] = new_price
            if new_description:
                book['description'] = new_description
            return True
    return False

