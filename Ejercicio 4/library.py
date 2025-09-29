"""
Sistema de Gestión de Biblioteca y Usuarios

Enunciado:

Desarrolla un sistema para gestionar una biblioteca que controle usuarios, libros disponibles,
préstamos activos y genere reportes. El sistema debe manejar usuarios únicos, catálogo de libros,
historial de préstamos y análisis de lectores.

Requisitos Técnicos Específicos:
Tipos de Datos Obligatorios:

Diccionarios: Para usuarios, libros y préstamos
Conjuntos: Para géneros literarios, autores favoritos y libros leídos
Listas: Para historial de préstamos por usuario
Strings: Para datos de usuarios y libros
Enteros: Para códigos de libros y contadores

Estructuras Requeridas:

Diccionario usuarios: {cedula: {"nombre", "generos_favoritos": set, "historial":[]}}
Diccionario libros: {codigo: {"titulo", "autor", "genero", "disponible": bool}}
Conjunto géneros: Géneros disponibles en la biblioteca

Operadores de Conjuntos Obligatorios:

Intersección: Para géneros en común entre usuarios
Diferencia simétrica: ^ para géneros únicos
Subconjunto: <= para verificar preferencias
Actualización: .update() para agregar múltiples géneros

Funcionalidades Requeridas:

1. Registrar usuario: Con géneros favoritos
2. Agregar libro: Al catálogo con validaciones
3. Prestar libro: Control de disponibilidad
4. Devolver libro: Actualizar estado y historial
5. Recomendar libros: Basado en géneros favoritos
6. Análisis de usuarios: Intersecciones y estadísticas
"""

import os

def clear_screen():
    os.system("cls" if os.name=="nt" else "clear")

def pause():
    input("Presione ENTER para continuar...")

def menu():
    clear_screen()
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


def main():
    isActive = True
    while isActive:
        try:
            clear_screen()
            choice = menu()

            match choice:
                case "1":
                    pass

                case "2":
                    pass

                case "3":
                    pass

                case "4":
                    pass

                case "5":
                    pass

                case "6":
                    pass

                case "0":
                    print("\n¡HASTA LUEGO! 👋")
                    print("Gracias por usar el gestor de biblioteca 😊.\n")
                    isActive = False

                case _:
                    print("\nError: Debe ingresar un número entre 0 y 6. Intente nuevamente.")
                    pause()
        except ValueError:
            print("\nError: Opción no válida. Intente nuevamente.")
            pause()

if __name__ == "__main__":
    main()