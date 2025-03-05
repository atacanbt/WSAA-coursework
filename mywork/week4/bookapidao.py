

import requests

URL = 'http://andrewbeatty1.pythonanywhere.com/books'

def get_books():
    response = requests.get(URL)
    return response.json()

def get_book(id):
    get_url = URL + '/' + str(id)
    response = requests.get(get_url)
    return response.json()

def add_book(book):
    book = {
    'title': 'Example Book',
    'author': 'John Doe',
    'price': 12.99  
}
    response = requests.post(URL, json=book)
    return response.json()

def update_book(id, bookdiff):
    update_url = URL + '/' + str(id)
    response = requests.put(update_url, json=bookdiff)
    return response.json()

def delete_book(id):
    delete_url = URL + '/' + str(id)
    response = requests.delete(delete_url)
    return response.json()

if __name__ == '__main__':
    
    bookdiff = {
        'price': 1000000
    }

    # print(get_books())
    # print(get_book(1616))
    # print(add_book({}))
    # print(update_book(1620, bookdiff))
    # print(delete_book(1620))