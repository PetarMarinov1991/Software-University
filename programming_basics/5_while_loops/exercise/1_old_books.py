searched_book = input()
library_capacity = int(input())

books_checked = 0
is_found = False
current_book = None

while books_checked < library_capacity:
    current_book = input()
    if current_book == searched_book:
        is_found = True
        break
    books_checked += 1
if is_found:
    print(f'You checked {books_checked} books and found it.')
else:
    print(f'The book you search is not here!\nYou checked {books_checked} books.')
