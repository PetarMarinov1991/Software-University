shelf = input().split("&")
line = input().split(" | ")

while line[0] != "Done":
    command = line[0]
    book = line[1]

    if command == "Add Book":
        if book not in shelf:
            shelf.insert(0, book)
    elif command == "Take Book":
        if book in shelf:
            shelf.remove(book)
    elif command == "Swap Books":
        book_2 = line[2]
        if book in shelf and book_2 in shelf:
            book_idx = shelf.index(book)
            book_2_idx = shelf.index(book_2)
            shelf[book_idx], shelf[book_2_idx] = shelf[book_2_idx], shelf[book_idx]
    elif command == "Insert Book":
        shelf.append(book)
    elif command == "Check Book":
        index = int(line[1])
        if not index > len(shelf):
            print(shelf[index])

    line = input().split(" | ")

print(", ".join(shelf))
