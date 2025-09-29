"""
Sistema de Gestión de Estudiantes y Materias

Enunciado:

Desarrolla un sistema para gestionar estudiantes, sus materias inscritas y calificaciones. El sistema
debe manejar estudiantes únicos, materias disponibles, inscripciones y generar reportes
académicos.

Requisitos Técnicos Específicos:
Tipos de Datos Obligatorios:

Diccionarios: Para estudiantes con sus datos y calificaciones
Conjuntos: Para materias disponibles y materias por estudiante
Listas: Para almacenar múltiples calificaciones por materia
Strings: Para nombres, códigos de materias, etc.
Enteros/Floats: Para calificaciones y promedios

Estructuras Requeridas:

Diccionario principal: estudiantes = {id_estudiante: datos}
Conjunto de materias: materias_disponibles = {"Matemáticas", "Física", ...}
Diccionario anidado: Para calificaciones por materia de cada estudiante

Operadores de Conjuntos Obligatorios:

Intersección: & o .intersection()
Unión: | o .union()
Diferencia: - o .difference()
Pertenencia: in para verificar elementos

Métodos de Diccionario Requeridos:

.get() , .keys() , .values() , .items()
.setdefault() para inicializar valores

Funcionalidades Requeridas:

1. Registrar estudiante: ID único, nombre
2. Agregar materias disponibles: Usar conjuntos
3. Inscribir estudiante a materia: Validar que exista
4. Registrar calificación: Agregar nota a materia específica
5. Ver materias comunes: Entre dos estudiantes (intersección)
6. Generar reporte: Promedio por estudiante y materia
"""
import os
estudiantes = {}
materias_disponibles = {"Matemáticas", "Física", "Química", "Historia", 
"Geografía", "Biología", "Lenguaje", "Inglés", "Informática"}

def clear_screen():
    os.system("cls" if os.name=="nt" else "clear")

def pause():
    input("\nPresione ENTER para continuar...")

def menu():
    clear_screen()
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

def registrar_estudiante():
    clear_screen()
    print("REGISTRAR ESTUDIANTE")
    print("-" * 50)
    id_estudiante = input("\nIngrese el ID del estudiante: ").strip()
    if id_estudiante in estudiantes:
        print("\nEste ID ya existe. Intente nuevamente.")
    else:
        nombre = input("Ingrese el nombre del estudiante: ").strip()
        estudiantes[id_estudiante] = {
            "nombre": nombre,
            "materias": {}
        }
        print(f"\n'{nombre}' ha registrado con éxito.")

def agregar_materia():
    clear_screen()
    print("AGREGAR MATERIA DISPONIBLE")
    print("-" * 50)
    materia = input("Ingrese el nombre de la materia: ").strip().title()
    if materia in materias_disponibles:
        print("Esta materia ya fue agregada anteriormente.")
    else:
        materias_disponibles.add(materia)
        print(f"'{materia}' fue agregada como materia disponible.")

def inscribir_materia():
    clear_screen()
    print("INSCRIBIR ESTUDIANTE A MATERIA")
    print("-" * 50)
    id_estudiante = input("\nIngrese el ID del estudiante: ")
    if id_estudiante not in estudiantes:
        print("\nEl estudiante aun no ha sido registrado.")
    else:
        print(f"\n>>> Materias disponibles: ")
        lista_materias = list(materias_disponibles)
        for idx, materia in enumerate(lista_materias, 1):
            print(f"{idx}. {materia}")
        
        materia = int(input("\nIngrese el número de la materia a inscribir: "))
        if materia >= 1 and materia <= len(lista_materias):
            ins_materia = lista_materias[materia - 1]
            estudiantes[id_estudiante]["materias"].setdefault(ins_materia, [])
            print(f"\nEl estudiante ha sido inscrito en la materia '{ins_materia}'")
        else:
            print("\nLa materia no está disponible.")

def registrar_calificacion():
    clear_screen()
    print("REGISTRAR CALIFACIÓN")
    print("-" * 50)
    id_estudiante = input("Ingrese el ID del estudiante: ").strip()
    if id_estudiante not in estudiantes:
        print("\nEl estudiante aun no ha sido registrado.")
    else:
        nombre = estudiantes[id_estudiante]["nombre"]
        if not estudiantes[id_estudiante]["materias"]:
            print(f"{nombre} no está inscrito en ninguna materia.")
        else:
            lista_materias = list(estudiantes[id_estudiante]["materias"].keys())
            print(f"Materias inscritas: {lista_materias}")
    pass

def main():
    isActive = True
    while isActive:
        try:
            clear_screen()
            choice = menu()

            match choice:
                case "1":
                    registrar_estudiante()
                    pause()

                case "2":
                    agregar_materia()
                    pause()

                case "3":
                    inscribir_materia()
                    pause()

                case "4":
                    registrar_calificacion()
                    pause()
                case "5":
                    pass

                case "6":
                    pass

                case "0":
                    print("\n¡HASTA LUEGO! 👋")
                    print("Gracias por usar este gestor académico 😊.\n")
                    isActive = False

                case _:
                    print("\nError: Debe ingresar un número entre 0 y 6. Intente nuevamente.")
                    pause()
        except ValueError:
            print("\nError: Opción no válida. Intente nuevamente.")
            pause()

if __name__ == "__main__":
    main()