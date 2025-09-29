import modules.utils as u

usuarios = {}
libros = {}
prestamos = {}
generos = set()

def registrar_usuario():
    u.clear_screen()
    print("REGISTRAR USUARIO")
    print("-" * 50)
    cedula = input("\nCédula del usuario: ").strip()
    if cedula in usuarios:
        print("\nEste usuario ya está registrado.")
    else:
        user = input("Nombre del usuario: ").strip().title()
        generos_fav = input("Ingrese los géneros favoritos (separados por comas): ").strip().title().split(",")
        generos_fav_set = {genero.strip() for genero in generos_fav if genero.strip}
        usuarios[cedula] = {"nombre": user, "generos_favoritos": generos_fav_set, "historial": []}
        print(f"\nUsuario '{user}' registrado con éxito.")

def agregar_libro():
    u.clear_screen()
    print("AGREGAR LIBRO")
    print("-" * 50)
    try:
        codigo = int(input("\nIngrese el código del libro (número entero): "))
        if codigo in libros:
            print("Este código fue está registrado anteriormente.")
        else:
            titulo = input("Título del libro: ").strip().title()
            autor = input("Autor del libro: ").strip().title()
            genero = input("Género del libro: ").strip().title()
            if genero not in generos:
                add_genero = input(f"\nEste género no ha sido agregado, ¿desea agregarlo?, ingrese SÍ o NO: ").strip().lower()
                if add_genero == "sí" or add_genero == "si":
                    generos.add(genero)
                    print(f"\nGénero agregado exitosamente.")
                else:
                    print("\nOperación cancelada. El libro no fue agregado.")
                    return
            libros[codigo] = {"titulo": titulo, "autor": autor, "genero": genero, "disponible": True}
            print(f"\nEl libro '{titulo}' fue agregado a la biblioteca.")
    except ValueError:
        print("Error: El código del libro debe ser un número entero.")

def prestar_libro():
    u.clear_screen()
    print("PRESTAR LIBRO")
    print("-" * 50)
    cedula = input("\nIngrese la cédula del usuario: ").strip()
    if cedula not in usuarios:
        print("\nEl usuario aún no ha sido registrado.")
    else:
        try:
            codigo = int(input("Ingrese el código del libro a prestar: "))
            if codigo not in libros:
                print("\nEl libro no está en el catálogo.")
            elif not libros[codigo]["disponible"]:
                print("\nEl libro no está disponible para préstamo.")
            else:
                libros[codigo]["disponible"] = False
                prestamos[codigo] = cedula
                usuarios[cedula]["historial"].append(codigo)
                print(f"\nEl libro '{libros[codigo]['titulo']}' ha sido prestado a '{usuarios[cedula]['nombre']}'.")
        except ValueError:
            print("Error: El código del libro debe ser un número entero.")

def devolver_libro():
    u.clear_screen()
    print("DEVOLVER LIBRO")
    print("-" * 50)
    cedula = input("\nIngrese la cédula del usuario: ").strip()
    if cedula not in usuarios:
        print("\nEl usuario aún no ha sido registrado.")
    else:
        try:
            codigo = int(input("Ingrese el código del libro a devolver: "))
            if codigo not in prestamos or codigo not in libros or prestamos[codigo] != cedula:
                print("\nEste libro fue prestado a otro usuario.")
            else:
                libros[codigo]["disponible"] = True
                del prestamos[codigo]
                print(f"\nEl libro '{libros[codigo]['titulo']}' ha sido devuelto por '{usuarios[cedula]['nombre']}'.")
        except ValueError:
            print("\nError: El código del libro debe ser un número entero.")

def recomendar_libros():
    u.clear_screen()
    print("RECOMENDAR LIBROS")
    print("-" * 50)
    cedula = input("\nIngrese la cédula del usuario: ").strip()
    if cedula not in usuarios:
        print("\nEl usuario aún no ha sido registrado.")
    else:
        user_generos = usuarios[cedula]["generos_favoritos"]
        recomendaciones = [libro for libro in libros.values() if libro["genero"] in user_generos and libro["disponible"]]
        if recomendaciones:
            print(f"\nLibros recomendados para '{usuarios[cedula]['nombre']}':")
            for libro in recomendaciones:
                print(f"- {libro['titulo']} por {libro['autor']} (Género: {libro['genero']})")
        else:
            print("\nNo hay libros disponibles que coincidan con los géneros favoritos del usuario.")

def analisis_usuarios():
    u.clear_screen()
    print("ANÁLISIS DE USUARIOS")
    print("-" * 50)
    if len(usuarios) < 2:
        print("\nSe necesitan al menos dos usuarios para realizar un análisis.")
        return
    cedula1 = input("\nIngrese la cédula del primer usuario: ").strip()
    cedula2 = input("Ingrese la cédula del segundo usuario: ").strip()
    if cedula1 not in usuarios or cedula2 not in usuarios:
        print("\nUno o ambos usuarios no están registrados.")
    else:
        gen1 = usuarios[cedula1]["generos_favoritos"]
        gen2 = usuarios[cedula2]["generos_favoritos"]
        interseccion = gen1 & gen2
        diferencia_simetrica = gen1 ^ gen2

        print(f"\nGéneros favoritos de '{usuarios[cedula1]['nombre']}': {', '.join(gen1) if gen1 else 'Ninguno'}")
        print(f"Géneros favoritos de '{usuarios[cedula2]['nombre']}': {', '.join(gen2) if gen2 else 'Ninguno'}")
        print(f"\nGéneros en común: {', '.join(interseccion) if interseccion else 'Ninguno'}")
        print(f"Géneros únicos entre ambos: {', '.join(diferencia_simetrica) if diferencia_simetrica else 'Ninguno'}")