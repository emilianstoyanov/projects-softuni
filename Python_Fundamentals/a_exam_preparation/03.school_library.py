books = input().split("&")

while True:
    commands = input().split(" | ")

    if commands[0] == "Done":
        print(", ".join(books))
        break

    elif commands[0] == "Add Book":
        book_name = commands[1]
        if book_name not in books:
            ins = books.insert(0, book_name) 
        else:
            continue

    elif commands[0] == "Take Book":
        books_names = commands[1]
        if books_names in books:
            rem = books.remove(books_names)  
        else:
            continue

    elif commands[0] == "Swap Books":
        book1 = commands[1]
        book2 = commands[2]
        if book1 in books and book2 in books:
            idx1 = books.index(book1) 
            idx2 = books.index(book2) 
            rev = books[idx1], books[idx2] = books[idx2], books[idx1] 

        else:
            continue

    elif commands[0] == "Insert Book":
        app_name_book = commands[1]
        append = books.append(app_name_book) 

    elif commands[0] == "Check Book":
        index_book = int(commands[1])
        if index_book >= 0 and index_book <= len(books):
            print(books[index_book]) 
        else:
            continue
