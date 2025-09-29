import modules.utils as u

estudiantes = {}
materias_disponibles = {"Matemáticas", "Física", "Química", "Historia", 
"Geografía", "Biología", "Lenguaje", "Inglés", "Informática"}

def registrar_estudiante():
    u.clear_screen()
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
    u.clear_screen()
    print("AGREGAR MATERIA DISPONIBLE")
    print("-" * 50)
    materia = input("\nIngrese el nombre de la materia: ").strip().title()
    if materia in materias_disponibles:
        print("Esta materia ya fue agregada anteriormente.")
    else:
        materias_disponibles.add(materia)
        print(f"\n'{materia}' fue agregada como materia disponible.")

def inscribir_materia():
    u.clear_screen()
    print("INSCRIBIR ESTUDIANTE A MATERIA")
    print("-" * 50)
    id_estudiante = input("\nIngrese el ID del estudiante: ")
    if id_estudiante not in estudiantes:
        print("\nEl estudiante aun no ha sido registrado.")
    else:
        print(f"\n>>> Materias disponibles: ")
        lista_materias = sorted(materias_disponibles)
        for idx, materia in enumerate(lista_materias, 1):
            print(f"{idx}. {materia}")
        
        materia_num = int(input("\nIngrese el número de la materia a inscribir: "))
        if materia_num >= 1 and materia_num <= len(lista_materias):
            ins_materia = lista_materias[materia_num - 1]
            if ins_materia in estudiantes[id_estudiante]["materias"]:
                print(f"\nEl estudiante ya está inscrito en la materia '{ins_materia}'")
            else:
                estudiantes[id_estudiante]["materias"][ins_materia] = []
                print(f"\nEl estudiante ha sido inscrito en la materia '{ins_materia}'")
        else:
            print("\nLa materia no está disponible.")

def registrar_calificacion():
    try:
        u.clear_screen()
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
                print("\n>>> Materias inscritas:")
                for idx, materia in enumerate(lista_materias, 1):
                    print(f"{idx}. {materia}")
                materia_num = int(input("\nIngrese el número de la materia para registrar la calificación: "))
                if materia_num >=1 or materia_num <= len(lista_materias):
                    materia = lista_materias[materia_num - 1]
                    nota = float(input("\nIngrese la calificación (0-10): "))
                    if nota >= 0 and nota <= 10:
                        estudiantes[id_estudiante]["materias"][materia].append(nota)
                        print(f"\nCalificación de {nota} registrada en '{materia}' para {nombre}.") 
                    else:
                        print("\nError: La calificación debe estar entre 0 y 10.")
    except ValueError:
        print("\nError: Opción no válida. Intente nuevamente.")

def materias_comunes():
    u.clear_screen()
    print("MATERIAS COMUNES ENTRE DOS ESTUDIANTES")
    print("-" * 50)
    id_estudiante1 = input("\nIngrese el ID del primer estudiante: ").strip()
    id_estudiante2 = input("Ingrese el ID del segundo estudiante: ").strip()
    if id_estudiante1 not in estudiantes or id_estudiante2 not in estudiantes:
        print("\nUno o ambos estudiantes aún no ha sido registrado.")
    else:
        materias1 = set(estudiantes[id_estudiante1]["materias"].keys())
        materias2 = set(estudiantes[id_estudiante2]["materias"].keys())
        comunes = materias1.intersection(materias2)
        if comunes:
            print(f"\nMaterias comunes entre {estudiantes[id_estudiante1]['nombre']} y {estudiantes[id_estudiante2]['nombre']}:")
            for materia in comunes:
                print(f"- {materia}")
        else:
            print("\nNo hay materias comunes entre los estudiantes.")

def generar_reporte():
    u.clear_screen()
    print("REPORTE ACADÉMICO")
    print("-" * 50)
    for id_estudiante, datos in estudiantes.items():
        nombre = datos["nombre"]
        print(f"\nEstudiante: {nombre} (ID: {id_estudiante})")
        if not datos["materias"]:
            print("\nNo está inscrito en ninguna materia.")
        else:
            for materia, calificaciones in datos["materias"].items():
                if calificaciones:
                    promedio = sum(calificaciones) / len(calificaciones)
                    print(f"    Materia: {materia} | Calificaciones: {calificaciones} | Promedio: {promedio:.2f}")
                else:
                    print(f"\n{materia} sin calificaciones registradas.")