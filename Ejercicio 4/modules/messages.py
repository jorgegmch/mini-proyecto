import modules.utils as u

def menu():
    u.clear_screen()
    print("SISTEMA DE GESTIÓN DE BIBLIOTECA")
    print("-" * 50)
    print("\n~~ MENÚ DE OPCIONES ~~\n")
    print("1. Registrar usuario")
    print("2. Agregar libro")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Recomendar libros")
    print("6. Análisis de usuarios")
    print("0. Salir")
    option = input("\n>>> Ingrese una opción (0-6): ")
    return option