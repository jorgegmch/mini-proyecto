"""
Sistema de Gestión de Tienda de Videojuegos

Enunciado:

Desarrolla un sistema completo para gestionar una tienda de videojuegos que incluya inventario,
clientes, ventas, empleados y reportes analíticos. El sistema debe manejar diferentes tipos de
usuarios, control de stock, historial de transacciones y generar análisis de negocio.

Requisitos Técnicos Específicos:
Todos los Tipos de Datos Obligatorios:

Listas: Historial de ventas, empleados activos
Tuplas: Información inmutable de productos y transacciones
Conjuntos: Plataformas, géneros, clientes VIP
Diccionarios: Inventario, clientes, empleados, configuración

Estructuras de Control Requeridas:

If/elif/else: Validaciones y lógica de negocio
Match-case: Menús y clasificaciones
While: Bucle principal y submenús
For: Iteraciones sobre inventario y reportes
Enumerate: Mostrar listas numeradas

Operadores Obligatorios:

Aritméticos: Cálculos de precios, descuentos, totales
Comparación: Validaciones de stock, precios
Lógicos: Condiciones complejas
Conjuntos: Intersección, unión, diferencia
Pertenencia: in , not in

Funciones Requeridas (mínimo 15):

Gestión completa modularizada por categorías
"""

import os

def clear_screen():
    os.system("cls" if os.name=="nt" else "clear")

def pause():
    input("Presione ENTER para continuar...")

def menu():
    clear_screen()
    print("SISTEMA DE GESTIÓN DE TIENDA DE VIDEOJUEGOS")
    print("-" * 50)
    print("\n~~ MENÚ DE OPCIONES ~~\n")
    print("1. Inventario")
    print("2. Clientes")
    print("3. Empleados")
    print("4. Ventas")
    print("5. Reportes")
    print("6. Configuración")
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
                    print("Gracias por usar este sistema de gestión😊.\n")
                    isActive = False

                case _:
                    print("\nError: Debe ingresar un número entre 0 y 6. Intente nuevamente.")
                    pause()
        except ValueError:
            print("\nError: Opción no válida. Intente nuevamente.")
            pause()

if __name__ == "__main__":
    main()