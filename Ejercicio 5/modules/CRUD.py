import modules.utils as u

inventario = {}
clientes = {}
empleados = {}
configuracion = {"nombre_tienda": "Tienda de Videojuegos", "impuesto": 0.19, "descuento_vip": 0.1}

historial_ventas = []
empleados_activos = []

plataformas = set()
generos = set()
clientes_vip = set()

def generar_id(prefijo, coleccion):
    numero = len(coleccion) + 1
    return f"{prefijo}{numero:03d}"

def agregar_producto():
    u.clear_screen()
    print("AGREGAR PRODUCTO")
    nombre = input("Nombre del juego: ").strip()
    plataforma = input("Plataforma: ").strip()
    genero = input("Género: ").strip()
    while True:
        precio_raw = input("Precio unitario: ")
        try:
            precio = float(precio_raw)
            break
        except ValueError:
            print("Precio inválido, intente de nuevo.")
    while True:
        stock_raw = input("Stock inicial: ")
        try:
            stock = int(stock_raw)
            break
        except ValueError:
            print("Stock inválido, intente de nuevo.")
    plataformas.add(plataforma)
    generos.add(genero)
    pid = generar_id("P", inventario)
    info_producto = (pid, nombre, plataforma, genero, precio)
    inventario[pid] = {"info": info_producto, "stock": stock}
    print(f"Producto {pid} agregado.")
    u.pause()

def eliminar_producto():
    u.clear_screen()
    print("ELIMINAR PRODUCTO")
    pid = input("ID del producto a eliminar: ").strip()
    if pid in inventario:
        del inventario[pid]
        print(f"Producto {pid} eliminado.")
    else:
        print("Producto no encontrado.")
    u.pause()

def actualizar_stock():
    u.clear_screen()
    print("ACTUALIZAR STOCK")
    pid = input("ID del producto: ").strip()
    if pid not in inventario:
        print("Producto no existe.")
        u.pause()
        return
    while True:
        delta_raw = input("Cantidad a sumar (negativa para restar): ")
        try:
            delta = int(delta_raw)
            break
        except ValueError:
            print("Entrada inválida.")
    actual = inventario[pid]["stock"]
    nuevo = actual + delta
    if nuevo < 0:
        print("No permitido dejar stock negativo.")
    else:
        inventario[pid]["stock"] = nuevo
        print(f"Stock actualizado: {actual} -> {nuevo}")
    u.pause()

def listar_productos():
    u.clear_screen()
    print("LISTA DE PRODUCTOS")
    if not inventario:
        print("No hay productos.")
        u.pause()
        return
    encabezado = f"{'Nº':3} {'ID':6} {'Nombre':30} {'Plat':8} {'Género':12} {'Precio':8} {'Stock':5}"
    print(encabezado)
    print("-" * len(encabezado))
    for i, (pid, dato) in enumerate(inventario.items(), start=1):
        _, nombre, plat, gen, precio = dato["info"]
        stock = dato["stock"]
        print(f"{i:3} {pid:6} {nombre[:30]:30} {plat[:8]:8} {gen[:12]:12} {precio:8.2f} {stock:5d}")
    u.pause()

def registrar_cliente():
    u.clear_screen()
    print("REGISTRAR CLIENTE")
    nombre = input("Nombre completo: ").strip()
    vip_resp = input("¿Es cliente VIP? (s/n): ").strip().lower()
    vip = vip_resp == "s"
    cid = generar_id("C", clientes)
    clientes[cid] = {"nombre": nombre, "vip": vip, "compras": 0}
    if vip:
        clientes_vip.add(cid)
    print(f"Cliente registrado: {cid}")
    u.pause()

def actualizar_cliente():
    u.clear_screen()
    print("ACTUALIZAR CLIENTE")
    cid = input("ID cliente: ").strip()
    if cid not in clientes:
        print("Cliente no encontrado.")
        u.pause()
        return
    nombre = input(f"Nuevo nombre (enter para mantener '{clientes[cid]['nombre']}'): ").strip()
    if nombre:
        clientes[cid]["nombre"] = nombre
    vip_resp = input("Marcar VIP? (s/n/enter para mantener): ").strip().lower()
    if vip_resp == "s":
        clientes[cid]["vip"] = True
        clientes_vip.add(cid)
    elif vip_resp == "n":
        clientes[cid]["vip"] = False
        clientes_vip.discard(cid)
    print("Cliente actualizado.")
    u.pause()

def listar_clientes():
    u.clear_screen()
    print("LISTA DE CLIENTES")
    if not clientes:
        print("No hay clientes.")
        u.pause()
        return
    for i, (cid, dato) in enumerate(clientes.items(), start=1):
        tag_vip = "VIP" if dato["vip"] else ""
        print(f"{i}. {cid} - {dato['nombre']} {tag_vip} (Compras: {dato['compras']})")
    u.pause()

def agregar_empleado():
    u.clear_screen()
    print("AGREGAR EMPLEADO")
    nombre = input("Nombre del empleado: ").strip()
    rol = input("Rol (admin/vendedor): ").strip().lower()
    eid = generar_id("E", empleados)
    empleados[eid] = {"nombre": nombre, "rol": rol, "activo": True}
    empleados_activos.append(eid)
    print(f"Empleado añadido: {eid}")
    u.pause()

def activar_desactivar_empleado():
    u.clear_screen()
    print("ACTIVAR/DESACTIVAR EMPLEADO")
    eid = input("ID empleado: ").strip()
    if eid not in empleados:
        print("Empleado no encontrado.")
        u.pause()
        return
    empleados[eid]["activo"] = not empleados[eid]["activo"]
    if empleados[eid]["activo"]:
        if eid not in empleados_activos:
            empleados_activos.append(eid)
        print(f"Empleado {eid} activado.")
    else:
        if eid in empleados_activos:
            empleados_activos.remove(eid)
        print(f"Empleado {eid} desactivado.")
    u.pause()

def listar_empleados():
    u.clear_screen()
    print("LISTA DE EMPLEADOS")
    if not empleados:
        print("No hay empleados.")
        u.pause()
        return
    for i, (eid, dato) in enumerate(empleados.items(), start=1):
        estado = "ACTIVO" if dato["activo"] else "INACTIVO"
        print(f"{i}. {eid} - {dato['nombre']} ({dato['rol']}) - {estado}")
    u.pause()

def seleccionar_cliente_para_venta():
    opcion = input("ID cliente (enter para venta anónima): ").strip()
    if opcion == "":
        return ""
    if opcion in clientes:
        return opcion
    else:
        print("Cliente no encontrado, se continuará como anónimo.")
        return ""

def registrar_venta():
    u.clear_screen()
    print("REGISTRAR VENTA")
    if not inventario:
        print("Inventario vacío. No se puede registrar venta.")
        u.pause()
        return
    cid = seleccionar_cliente_para_venta()
    es_vip = cid != "" and clientes[cid]["vip"]
    carrito = []
    while True:
        listar_productos()
        pid = input("ID producto a añadir (enter para terminar): ").strip()
        if pid == "":
            break
        if pid not in inventario:
            print("Producto no existe.")
            continue
        while True:
            q_raw = input("Cantidad: ")
            try:
                cantidad = int(q_raw)
                break
            except ValueError:
                print("Cantidad inválida.")
        if cantidad <= 0:
            print("Cantidad debe ser positiva.")
            continue
        if cantidad > inventario[pid]["stock"]:
            print("Stock insuficiente.")
            continue
        carrito.append((pid, cantidad))
        print(f"Añadido {cantidad} x {inventario[pid]['info'][1]}")
    if not carrito:
        print("Carrito vacío. Venta cancelada.")
        u.pause()
        return
    subtotal = 0.0
    for pid, cantidad in carrito:
        precio = inventario[pid]["info"][4]
        subtotal += precio * cantidad
    impuesto = subtotal * configuracion["impuesto"]
    descuento = 0.0
    if es_vip:
        descuento = subtotal * configuracion["descuento_vip"]
    total = subtotal + impuesto - descuento
    print("\nRESUMEN")
    for pid, cantidad in carrito:
        nombre = inventario[pid]["info"][1]
        precio = inventario[pid]["info"][4]
        print(f"{cantidad} x {nombre} @ {precio:.2f} = {cantidad * precio:.2f}")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Impuesto: {impuesto:.2f}")
    if descuento > 0:
        print(f"Descuento VIP: -{descuento:.2f}")
    print(f"Total: {total:.2f}")
    confirmar = input("Confirmar venta? (s/n): ").strip().lower()
    if confirmar != "s":
        print("Venta cancelada.")
        u.pause()
        return
    for pid, cantidad in carrito:
        inventario[pid]["stock"] -= cantidad
    tid = generar_id("T", {t[0]: t for t in historial_ventas})
    items_transaccion = tuple((pid, cantidad) for pid, cantidad in carrito)
    transaccion = (tid, "N/A", cid, items_transaccion, total)
    historial_ventas.append(transaccion)
    if cid:
        clientes[cid]["compras"] += 1
    print(f"Venta registrada: {tid}")
    u.pause()

def listar_ventas():
    u.clear_screen()
    print("HISTORIAL DE VENTAS")
    if not historial_ventas:
        print("No hay ventas registradas.")
        u.pause()
        return
    for i, t in enumerate(historial_ventas, start=1):
        tid, fecha, cid, items, total = t
        nombre_cliente = clientes[cid]["nombre"] if cid and cid in clientes else "Anónimo"
        print(f"{i}. {tid} | {fecha} | Cliente: {nombre_cliente} | Total: {total:.2f}")
        for pid, cantidad in items:
            nombre_producto = inventario.get(pid, {}).get("info", ("", "Desconocido"))[1]
            print(f"    - {cantidad} x {nombre_producto} (ID:{pid})")
    u.pause()

def reporte_ventas_por_genero():
    u.clear_screen()
    print("REPORTE: VENTAS POR GÉNERO")
    totales_genero = {}
    for tid, fecha, cid, items, total in historial_ventas:
        for pid, cantidad in items:
            prod = inventario.get(pid)
            if prod:
                genero = prod["info"][3]
                totales_genero[genero] = totales_genero.get(genero, 0.0) + prod["info"][4] * cantidad
    if not totales_genero:
        print("No hay datos.")
        u.pause()
        return
    for genero, monto in totales_genero.items():
        print(f"{genero}: {monto:.2f}")
    u.pause()

def reporte_top_clientes(n=5):
    u.clear_screen()
    print(f"TOP {n} CLIENTES POR NÚMERO DE COMPRAS")
    if not clientes:
        print("No hay clientes.")
        u.pause()
        return
    ordenados = sorted(clientes.items(), key=lambda kv: kv[1]["compras"], reverse=True)
    for i, (cid, datos) in enumerate(ordenados[:n], start=1):
        print(f"{i}. {datos['nombre']} (ID:{cid}) - Compras: {datos['compras']} - {'VIP' if datos['vip'] else ''}")
    u.pause()

def reporte_stock_alertas(umbral=3):
    u.clear_screen()
    print("ALERTAS DE STOCK")
    bajos = [(pid, dato["info"][1], dato["stock"]) for pid, dato in inventario.items() if dato["stock"] <= umbral]
    if not bajos:
        print("No hay alertas.")
        u.pause()
        return
    for pid, nombre, stock in bajos:
        print(f"{pid}: {nombre} - stock {stock}")
    u.pause()

def reporte_conjuntos_operaciones():
    u.clear_screen()
    print("OPERACIONES CONJUNTOS: PLATAFORMAS Y GÉNEROS")
    union = plataformas.union(generos)
    interseccion = plataformas.intersection(generos)
    diferencia = plataformas.difference(generos)
    print("UNIÓN (plataformas ∪ géneros):")
    for i, val in enumerate(sorted(list(union)), start=1):
        print(f"{i}. {val}")
    print("\nINTERSECCIÓN (plataformas ∩ géneros):")
    if interseccion:
        for i, val in enumerate(sorted(list(interseccion)), start=1):
            print(f"{i}. {val}")
    else:
        print("No hay intersección.")
    print("\nDIFERENCIA (plataformas - géneros):")
    if diferencia:
        for i, val in enumerate(sorted(list(diferencia)), start=1):
            print(f"{i}. {val}")
    else:
        print("No hay diferencia.")
    u.pause()

def generar_reportes_todos():
    reporte_ventas_por_genero()
    reporte_top_clientes()
    reporte_stock_alertas()
    reporte_conjuntos_operaciones()

def configurar_tienda():
    u.clear_screen()
    print("CONFIGURACIÓN DE LA TIENDA")
    nombre = input(f"Nombre tienda (actual: {configuracion['nombre_tienda']}) (enter=mantener): ").strip()
    if nombre:
        configuracion["nombre_tienda"] = nombre
    impuesto_raw = input(f"Impuesto actual {configuracion['impuesto']} (enter=mantener): ").strip()
    if impuesto_raw:
        try:
            impuesto = float(impuesto_raw)
            configuracion["impuesto"] = impuesto
        except ValueError:
            print("Valor inválido, impuesto no cambiado.")
    descuento_raw = input(f"Descuento VIP actual {configuracion['descuento_vip']} (enter=mantener): ").strip()
    if descuento_raw:
        try:
            descuento = float(descuento_raw)
            configuracion["descuento_vip"] = descuento
        except ValueError:
            print("Valor inválido, descuento no cambiado.")
    print("Configuración actualizada.")
    u.pause()

def menu_inventario():
    activo = True
    while activo:
        u.clear_screen()
        print("GESTIÓN DE INVENTARIO")
        print("-" * 40)
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar stock")
        print("4. Listar productos")
        print("0. Volver")
        opcion = input("\n>>> Ingrese una opción: ").strip()
        match opcion:
            case "1":
                agregar_producto()
            case "2":
                eliminar_producto()
            case "3":
                actualizar_stock()
            case "4":
                listar_productos()
            case "0":
                activo = False
            case _:
                print("Opción inválida.")
                u.pause()

def menu_clientes():
    activo = True
    while activo:
        u.clear_screen()
        print("GESTIÓN DE CLIENTES")
        print("-" * 40)
        print("1. Registrar cliente")
        print("2. Actualizar cliente")
        print("3. Listar clientes")
        print("0. Volver")
        opcion = input("\n>>> Ingrese una opción: ").strip()
        match opcion:
            case "1":
                registrar_cliente()
            case "2":
                actualizar_cliente()
            case "3":
                listar_clientes()
            case "0":
                activo = False
            case _:
                print("Opción inválida.")
                u.pause()

def menu_empleados():
    activo = True
    while activo:
        u.clear_screen()
        print("GESTIÓN DE EMPLEADOS")
        print("-" * 40)
        print("1. Agregar empleado")
        print("2. Activar/Desactivar empleado")
        print("3. Listar empleados")
        print("0. Volver")
        opcion = input("\n>>> Ingrese una opción: ").strip()
        match opcion:
            case "1":
                agregar_empleado()
            case "2":
                activar_desactivar_empleado()
            case "3":
                listar_empleados()
            case "0":
                activo = False
            case _:
                print("Opción inválida.")
                u.pause()

def menu_ventas():
    activo = True
    while activo:
        u.clear_screen()
        print("GESTIÓN DE VENTAS")
        print("-" * 40)
        print("1. Registrar venta")
        print("2. Listar ventas")
        print("0. Volver")
        opcion = input("\n>>> Ingrese una opción: ").strip()
        match opcion:
            case "1":
                registrar_venta()
            case "2":
                listar_ventas()
            case "0":
                activo = False
            case _:
                print("Opción inválida.")
                u.pause()

def menu_reportes():
    activo = True
    while activo:
        u.clear_screen()
        print("REPORTES")
        print("-" * 40)
        print("1. Ventas por género")
        print("2. Top clientes")
        print("3. Alertas de stock")
        print("4. Operaciones con conjuntos")
        print("5. Generar todos los reportes")
        print("0. Volver")
        opcion = input("\n>>> Ingrese una opción: ").strip()
        match opcion:
            case "1":
                reporte_ventas_por_genero()
            case "2":
                n_raw = input("¿Cuántos top mostrar? (enter=5): ").strip()
                n = int(n_raw) if n_raw.isdigit() else 5
                reporte_top_clientes(n)
            case "3":
                umbral_raw = input("Umbral de stock (enter=3): ").strip()
                umbral = int(umbral_raw) if umbral_raw.isdigit() else 3
                reporte_stock_alertas(umbral)
            case "4":
                reporte_conjuntos_operaciones()
            case "5":
                generar_reportes_todos()
            case "0":
                activo = False
            case _:
                print("Opción inválida.")
                u.pause()

def menu_configuracion():
    activo = True
    while activo:
        u.clear_screen()
        print("CONFIGURACIÓN")
        print("-" * 40)
        print("1. Configurar tienda")
        print("0. Volver")
        opcion = input("\n>>> Ingrese una opción: ").strip()
        match opcion:
            case "1":
                configurar_tienda()
            case "0":
                activo = False
            case _:
                print("Opción inválida.")
                u.pause()



def seed_demo():
    pid = generar_id("P", inventario)
    inventario[pid] = {"info": (pid, "Elden Ring", "PS5", "RPG", 149.0), "stock": 5}
    plataformas.add("PS5"); generos.add("RPG")
    pid2 = generar_id("P", inventario)
    inventario[pid2] = {"info": (pid2, "Halo Infinite", "Xbox", "Shooter", 129.0), "stock": 3}
    plataformas.add("Xbox"); generos.add("Shooter")
    cid = generar_id("C", clientes)
    clientes[cid] = {"nombre": "Ana Pérez", "vip": True, "compras": 1}
    clientes_vip.add(cid)
    eid = generar_id("E", empleados)
    empleados[eid] = {"nombre": "Carlos", "rol": "vendedor", "activo": True}
    empleados_activos.append(eid)
    trans_items = ((list(inventario.keys())[0], 1),)
    historial_ventas.append(("T001", "N/A", cid, trans_items, inventario[list(inventario.keys())[0]]["info"][4]))