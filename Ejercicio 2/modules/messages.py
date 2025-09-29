import modules.utils as u

def title():
    print("GESTOR DE BIBLIOTECA PERSONAL")
    print("-" * 50)

def menu():
        u.clear_screen()
        title()
        print("\n~~ MENÚ DE OPCIONES ~~\n")
        print("1. Agregar libros")
        print("2. Ver biblioteca")
        print("3. Buscar libros")
        print("4. Cambiar estado (leído/no leído)")
        print("5. Estadísticas de lectura")
        print("6. Eliminar libros")
        print("0. Salir\n")
        choice = input("Ingrese una opción (0-6): ")
        return choice