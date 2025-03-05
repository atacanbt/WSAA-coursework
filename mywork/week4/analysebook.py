from bookapidao import get_books

books = get_books()
total = 0
count = 0
for book in books:
    total += book['price']
    count += 1


print(f'Total price of all books: {total}')
print(f'Number of books: {count}')
print(f'Average price of all books: {total / count}')