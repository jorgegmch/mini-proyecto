import modules.utils as u

def menu():
    u.clear_screen()
    print("SISTEMA DE GESTIÓN DE ESTUDIANTES Y MATERIAS")
    print("-" * 50)
    print("\n~~ MENÚ DE OPCIONES ~~\n")
    print("1. Registrar estudiante")
    print("2. Agregar materia disponible")
    print("3. Inscribir estudiante a materia")
    print("4. Registrar calificación")
    print("5. Ver materias comunes")
    print("6. Generar reporte académico")
    print("0. Salir")
    option = input("\n>>> Ingrese una opción (0-6): ")
    return option