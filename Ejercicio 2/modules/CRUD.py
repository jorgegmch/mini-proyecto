import modules.utils as u

books = []

def add_books():
    while True:
        try:
            u.clear_screen()
            print("AGREGAR LIBROS")
            print("-" * 50)
            book_title = input("\nTítulo: ").upper()
            author = input("Autor: ").title()
            book_genre = input("Género literario: ").title()
            publishing = int(input("Año de publicación: "))
            state = input("¿Ya lo ha leído?, ingrese SÍ o NO: ").lower()
            if state == "sí" or state == "si":
                state = True
                added_book = (book_title, author, book_genre, publishing, state)
                books.append(added_book)
                print(f"\nEl libro '{book_title}' ha sido agregado.")
                u.pause()
                break
            elif state == "no":
                state = False
                added_book = (book_title, author, book_genre, publishing, state)
                books.append(added_book)
                print(f"\nEl libro '{book_title}' ha sido agregado.")
                u.pause()
                break
            else:
                print("\nError: Debe ingresar SÍ o NO para validar el estado de lectura del libro.")
                u.pause()
        except ValueError:
            print("\nError: Debe ingresar un año válido.")
            u.pause()

def view_library():
    print("BIBLIOTECA PERSONAL")
    print("-" * 50)
    if not books:
        print("\nAún no hay libros en la biblioteca.")
    else:
        for idx, (book_title, author, book_genre, publishing, state) in enumerate(books, 1):
            if state == True:
                state_symbol = "✅"
            else:
                state_symbol = "❌"
            print(f"\n{idx}. {book_title}")
            print(f"Autor(a): {author} | Año de publicación: {publishing}")
            print(f"Género: {book_genre} | Estado de lectura: {state_symbol}")
            print("-" * 50)

def search_books():
    while True:
        try:
            u.clear_screen()
            print("BUSCADOR DE LIBROS")
            print("-" * 50)
            if not books:
                print("\nAún no hay libros en la biblioteca.")
            else:
                print("\n¿Cómo desea buscar?\n")
                print("1. Por título")
                print("2. Por autor")
                print("3. Por género")
                print("0. Salir\n")
                search_choice = input("Ingrese una opción (0-3): ")

                match search_choice:
                    case "1":
                        u.clear_screen()
                        search_title = input(">>> Ingrese un título: ").lower()
                        print("\nRESULTADOS ENCONTRADOS:")
                        print("-" * 60)
                        found = False
                        for book in books:
                            book_title = book[0].lower()
                            if search_title in book_title:
                                print(f"\nTítulo: {book[0]} | Autor: {book[1]} | Género: {book[2]} | Año: {book[3]}")
                                print("-" * 60)
                                found = True
                        if not found:
                            print("\nNo se encontraron resultados.")
                        u.pause()

                    case "2":
                        u.clear_screen()
                        search_author = input(">>> Ingrese el nombre de un autor: ").lower()
                        print("\nRESULTADOS ENCONTRADOS:\n")
                        print("-" * 60)
                        found = False
                        for book in books:
                            book_author = book[1].lower()
                            if search_author in book_author:
                                print(f"\nTítulo: {book[0]} | Autor: {book[1]} | Género: {book[2]} | Año: {book[3]}")
                                print("-" * 60)
                                found = True
                        if not found:
                            print("\nNo se encontraron resultados.")
                        u.pause()

                    case "3":
                        u.clear_screen()
                        search_genre = input(">>> Ingrese un género literario: ").lower()
                        print("\nRESULTADOS ENCONTRADOS:\n")
                        print("-" * 60)
                        found = False
                        for book in books:
                            book_genre = book[2].lower()
                            if search_genre in book_genre:
                                print(f"\nTítulo: {book[0]} | Autor: {book[1]} | Género: {book[2]} | Año: {book[3]}")
                                print("-" * 60)
                                found = True
                        if not found:
                            print("\nNo se encontraron resultados.")
                        u.pause()

                    case "0":
                        break

                    case _:
                        print("\nError: Debe ingresar un número entre 0 y 3. Intente nuevamente.")
                        u.pause()
        except ValueError:
            print("\nError: Opción no válida. Intente nuevamente.")

def change_state():
    try:
        u.clear_screen()
        print("MARCAR LIBRO LEÍDO / NO LEÍDO")
        print("-" * 50)
        if not books:
            print("\nAún no hay libros en la biblioteca.")
        else:
            for idx, (book_title, author, book_genre, publishing, state) in enumerate(books, 1):
                if state == True:
                    state_symbol = "✅"
                else:
                    state_symbol = "❌"
                print(f"\n{idx}. {book_title}")
                print(f"Autor(a): {author} | Año de publicación: {publishing}")
                print(f"Género: {book_genre} | Estado de lectura: {state_symbol}")
                print("-" * 50)

        book_num = int(input("\nIngrese el número del libro para modificar su estado: "))
        if book_num > 0 and book_num <= len(books):
            new_state = input("¿Ya leiste este libro?, ingrese SÍ o NO: ").lower()
            if new_state == "sí" or new_state == "si":
                new_state = True
                book_title, author, book_genre, publishing, _ = books[book_num - 1]
                books[book_num - 1] = (book_title, author, book_genre, publishing, new_state)
                print("\nEl estado de lectura ha sido actualizado.")
            elif new_state == "no":
                new_state = False
                book_title, author, book_genre, publishing, _ = books[book_num - 1]
                books[book_num - 1] = (book_title, author, book_genre, publishing, new_state)
                print("\nEl estado de lectura ha sido actualizado.")
            else:
                print("\nError. Opción no válida. Vuelva a intentar.")
    except ValueError:
        print("\nError: Opción no válida. Intente nuevamente. ")

def reading_stats():
    u.clear_screen()
    print("ESTADÍSTICAS DE LECTURA")
    print("-" * 50)
    if not books:
        print("\nAún no hay libros en la biblioteca.")
    else:
        total_books = len(books)
        total_read = 0
        genres_count = {}
        for book in books:
            state = book[4]
            genre = book[2]
            if state == True:
                total_read += 1
            if genre not in genres_count:
                genres_count[genre] = 0
            genres_count[genre] += 1
        total_unread = total_books - total_read

        print(f"\n>>> TOTAL DE LIBROS = {total_books}")
        print(f">>> TOTAL LEÍDOS = {total_read}")
        print(f">>> TOTAL NO LEÍDOS = {total_unread}")
        print(f"\n>>> GÉNEROS MÁS FRECUENTES:")
        for genre, count in genres_count.items():
            print(f"{genre}: {count}")

def delete_books():
    u.clear_screen()
    print("¿QUÉ LIBRO DESEA SACAR DE SU LISTA?")
    print("-" * 50)
    if not books:
        print("\nAún no hay libros en la biblioteca.")
    else: 
        for idx, (book_title, author, book_genre, publishing, state) in enumerate(books, 1):
                if state == True:
                    state_symbol = "✅"
                else:
                    state_symbol = "❌"
                print(f"\n{idx}. {book_title}")
                print(f"Autor(a): {author} | Año de publicación: {publishing}")
                print(f"Género: {book_genre} | Estado de lectura: {state_symbol}")
                print("-" * 50)
    try:
        book_num = int(input("\nIngrese el número del libro que desea eliminar: "))
        if book_num >= 1 and book_num <= len(books):
            delete_book = input("¿Seguro que desea eliminar este libro?, ingrese SÍ o NO: ").lower()
            if delete_book == "sí" or delete_book == "si":
                del books[book_num - 1]
                print(f"\nEl libro ha sido eliminado de su biblioteca.")
            elif delete_book == "no":
                print("\nOperación cancelada.")
            else:
                print("\nError: Debe ingresar SÍ o NO para validar la eliminación del libro indicado.")
    except ValueError:
        print("\nError: Debe ingresar un número válido.")
        u.pause()