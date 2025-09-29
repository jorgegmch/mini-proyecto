import modules.utils as u

juegos = [] # Lista global para juegos

def add_game():
    while True:
        try:
            u.clear_screen()
            print("Sistema de Inventario de Videojuegos")
            print("\nAGREGAR VIDEOJUEGO")
            print("." * 60)
            nombre = input("\nIngrese el nombre del juego: ") # Usar input() para datos
            genero = input("Ingrese el genero del juego: ")
            estado = input("El juego está terminado ¿SÍ o NO?: ").lower()
            if estado == "si" or estado == "sí": 
                estado = True
                print(f"\n{nombre}, ha sido agregado con éxito a su lista.")
                registroJuego = (nombre, genero, estado) # Crear tupla (nombre, genero, False)
                juegos.append(registroJuego) # Usar append() en lista
                break
            elif estado == "no":
                estado = False
                print(f"\n{nombre}, ha sido agregado con éxito a su lista.")
                registroJuego = (nombre, genero, estado) # Crear tupla (nombre, genero, False)
                juegos.append(registroJuego) # Usar append() en lista
                break
            else:
                print("\nError: Debe ingresar SÍ o NO para validar el estado del juego.")
                u.pause()
        except ValueError:
            print("\nError: Opción no válida. Intente nuevamente.")
            u.pause()

def view_games():
    u.clear_screen()
    print("Sistema de Inventario de Videojuegos")
    print("\nCOLECCIÓN DE VIDEOJUEGOS")
    print("." * 60)
    if not juegos: # Usar if not para verificar lista vacía
        print("\nNo ha agregado videojuegos a su lista.")
    else:
        for indice, (nombre, genero, estado) in enumerate(juegos, 1): # Usar for con enumerate()
            if estado == True:
                estado = "✅"
            else:
                estado = "❌"
            print(f"\n{indice}. {nombre} | {genero} | {estado}") # Desempaquetar tupla

def complete_game():
    try:
        u.clear_screen()
        print("Sistema de Inventario de Videojuegos")
        print("\nMARCAR JUEGOS COMPLETADO / NO COMPLETADO")
        print("." * 60)
        if not juegos: # Usar if not para lista vacía
            print("\nNo ha agregado videojuegos a su lista.")
        else:
            view_games()
            game_num = int(input("\nNúmero del juego a marcar: "))

            # Cambiar estado
            if game_num >= 1 and game_num <= len(juegos): # Usar >= y <= para validar índice
                nombre, genero, estado = juegos[game_num - 1] # Modificar tupla en lista
                if estado == True:
                    juegos[game_num - 1] = (nombre, genero, False)
                    print(f"\n'{nombre}' marcado como NO COMPLETADO.")
                else:
                    juegos[game_num - 1] = (nombre, genero, True)
                    print(f"\n'{nombre}' marcado como COMPLETADO.")
            else:
                print("\nError: Debe ingresar un número válido.")
    except ValueError:
        print("\nError: Opción no válida. Intente nuevamente.")

def show_stats():
    u.clear_screen()
    print("Sistema de Inventario de Videojuegos")
    print("\nESTADÍSTICAS BÁSICAS")
    print("." * 60)
    if not juegos: # Usar if not para lista vacía
            print("\nNo ha agregado videojuegos a su lista.")
    else:
        total = len(juegos)
        completados = 0

        for juego in juegos: # Usar for para contar
            if juego[2]:
                completados += 1 # Operadores aritméticos

        no_completados = total - completados

        print(f"\n>>> Total de juegos: {total}")
        print(f">>> Completado: {completados}")
        print(f">>> Pendientes: {no_completados}")