import datetime

NOMBRE_PARQUEADERO = "Otherworld Park"
ESPACIOS_TOTALES = 64
TARIFA_POR_HORA = 7000
TARIFA_POR_CUARTO_HORA = 1500


ADMIN_USUARIOS = { "admin": "admin123",  "comandante": "space2025", "supervisor": "hangar456"}

usuarios = {}
naves_en_hangar = {}

historial_naves_retiradas = []
total_recaudado = 0
tiempo_total_estancia = 0
cantidad_naves_retiradas = 0



def mostrar_encabezado():
    print("\n=== 🚀 Bienvenido al estacionamiento Otherworld Park 🪐 ===")
    print("     Control central de ingreso de naves espaciales")
    print("==============================================================")
    
    
def validar_nombre(nombre):
    # este  valida que el nombre tenga al menos 3 letras 
    if len(nombre) < 3:
        return False, "El nombre debe tener al menos 3 letras."
    
    # para verificar que no tenga números
    for caracter in nombre:
        if caracter.isdigit():
            return False, "El nombre no puede contener números."
    
    # para veerificar que solo tenga letras y espacios
    for caracter in nombre:
        if not caracter.isalpha() and caracter != " ":
            return False, "El nombre solo puede contener letras."
    
    return True, ""

def validar_apellido(apellido):
   #Valida que el apellido tenga al menos 3 letras
    if len(apellido) < 3:
        return False, "El apellido debe tener al menos 3 letras."
    
    # Verificar que no tenga números
    for caracter in apellido:
        if caracter.isdigit():
            return False, "El apellido no puede contener números."
    
    # Verifica que solo tenga letras y espacios
    for caracter in apellido:
        if not caracter.isalpha() and caracter != " ":
            return False, "El apellido solo puede contener letras."
    
    return True, ""   

def validar_documento(documento):
    # esta valida que el documento tenga entre 3 y 15 dígitos y solo contenga números
    if not documento.isdigit():
        return False, "El documento solo puede contener números."
    if len(documento) < 3 or len(documento) > 15:
        return False, "El documento debe tener entre 3 y 15 dígitos."
    return True, ""

def validar_placa(placa):
    #Valida que la placa tenga exactamente 6 caracteres 3 letras seguidas de 3 números
    if len(placa) != 6:
        return False, "La placa debe tener exactamente 6 caracteres."
    
    # Verifica que los primeros 3 caracteres sean letras
    for i in range(3):
        if not placa[i].isalpha():
            return False, "Los primeros 3 caracteres deben ser letras."
    
    # Verifica que los últimos 3 caracteres sean números
    for i in range(3, 6):
        if not placa[i].isdigit():
            return False, "Los últimos 3 caracteres deben ser números."
    
    return True, ""

def calcular_cobro(hora_entrada, hora_salida):
    #Calcula el cobro por tiempo de parqueo
    tiempo = hora_salida - hora_entrada
    minutos_totales = tiempo.total_seconds() / 60
    
    # Calcula horas completas
    horas_completas = int(minutos_totales // 60)
    minutos_restantes = int(minutos_totales % 60)
    
    # Calcula cuartos de hora (cada 15 minutos)
    cuartos_hora = 0
    if minutos_restantes > 0:
        cuartos_hora = int((minutos_restantes - 1) // 15) + 1
    
    # Calcula cobros
    cobro_horas = horas_completas * TARIFA_POR_HORA
    cobro_cuartos = cuartos_hora * TARIFA_POR_CUARTO_HORA
    total = cobro_horas + cobro_cuartos
    
    # Aplica el pago minimo
    if total < TARIFA_POR_HORA:
        total = TARIFA_POR_HORA
    
    return { 'minutos_totales': int(minutos_totales), 'horas_completas': horas_completas, 'cuartos_hora': cuartos_hora,
        'cobro_horas': cobro_horas,  'cobro_cuartos': cobro_cuartos,  'total': total }


def solicitar_datos_con_validacion(campo, funcion_validacion):
    #Solicita un dato y lo valida hasta que sea correcto
    while True:
        dato = input(f"{campo}: ").strip()
        if campo == "Matrícula de la nave (placa)":
            dato = dato.upper()
        
        valido, mensaje = funcion_validacion(dato)
        if valido:
            return dato
        else:
            print(f"⚠️ {mensaje}⚠️")


def registrar_tripulante():
    print("\n Registro de nuevo tripulante🧑‍🚀")
    
    # Solicita y valida cada uno de los datosss
    nombre = solicitar_datos_con_validacion("Nombre del tripulante", validar_nombre)    
    apellido = solicitar_datos_con_validacion("Apellido del tripulante", validar_apellido) 
    documento = solicitar_datos_con_validacion("Documento del tripulante", validar_documento) 
    placa = solicitar_datos_con_validacion("Matrícula de la nave (placa)", validar_placa)

    if placa in usuarios:
        print("⚠️ Ya existe un tripulante registrado con esta nave⚠️.")
    else:
        usuarios[placa] = {'nombre': nombre,'apellido': apellido, 'documento': documento }
        print(" Registro exitoso✅.")

def ingresar_nave():
    print("\n Acoplar nave al hangar🛸")
    if len(naves_en_hangar) >= ESPACIOS_TOTALES:
        print(" Hangar lleno❌. No hay espacios disponibles.")
        return

    placa = input("Placa de la nave : ").upper()

    if placa not in usuarios:
        print("⚠️ Tripulante no registrado⚠️ . Regístrese primero.")
        return

    if placa in naves_en_hangar:
        print("⚠️ Esta nave ya está acoplada⚠️.")
        return

    hora_entrada = datetime.datetime.now()
    naves_en_hangar[placa] = hora_entrada
    print(" Nave acoplada exitosamente✅.")

def retirar_nave():
    print("\n Desacoplar nave del hangar")
    placa = input("Matrícula de la nave (placa): ").upper()

    if placa not in naves_en_hangar:
        print("⚠️Esta nave no está en el hangar⚠️.")
        return

    hora_salida = datetime.datetime.now()
    hora_entrada = naves_en_hangar.pop(placa)
    
    # Csalcula cobro detallado
    cobro = calcular_cobro(hora_entrada, hora_salida)
    tripulante = usuarios[placa]
    
    historial_naves_retiradas = []
    total_recaudado = 0
    tiempo_total_estancia = 0
    cantidad_naves_retiradas = 0
    
    print("\n🧾 Recibo de misión completada")
    print(f"Tripulante: {tripulante['nombre']} {tripulante['apellido']}")
    print(f"Documento: {tripulante['documento']}")
    print(f"Nave: {placa}")
    print(f"Tiempo total: {cobro['minutos_totales']} minutos")
    print(f"Horas completas: {cobro['horas_completas']} horas")
    print(f"Cuartos de hora: {cobro['cuartos_hora']} cuartos")
    print(f"Cobro por horas: ${cobro['cobro_horas']}")
    print(f"Cobro por cuartos: ${cobro['cobro_cuartos']}")
    print(f"Total a pagar: ${cobro['total']}")
    
    if (cobro['total'] == TARIFA_POR_HORA and 
       (cobro['cobro_horas'] + cobro['cobro_cuartos']) < TARIFA_POR_HORA):
        print("(Se aplicó pago mínimo de una hora)")


def ver_reporte():
    print("\n Reporte del Hangar Espacial")
    print(f"Espacios disponibles: {ESPACIOS_TOTALES - len(naves_en_hangar)}")
    print(f"Naves en el hangar: {len(naves_en_hangar)}")
    if naves_en_hangar:
        print("Naves acopladas:")
        for placa, hora in naves_en_hangar.items():
            tripulante = usuarios[placa]
            print(f"- {placa} ({tripulante['nombre']} {tripulante['apellido']}), " +
                  f"desde las {hora.strftime('%H:%M')}")
    else:
        print("No hay naves acopladas actualmente.")
        
        
def menu_administrador():
    print("\n Acceso al sistema de administración")
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
    
    if usuario in ADMIN_USUARIOS and ADMIN_USUARIOS[usuario] == contraseña:
        print("Acceso autorizado✅ ")
        while True:
            print("\n===  Panel de Administración  ===")
            print("1. Total de vehículos registrados")
            print("2. Total de vehículos retirados")
            print("3. Total de vehículos sin retirar")
            print("4. Total pago de vehículos retirados")
            print("5. Tiempo promedio de estancia")
            print("6. Lista de usuarios")
            print("7. Vehículo con tiempo máximo y mínimo")
            print("8. Volver al menú principal")
            
            opcion = input("\nSeleccione una opción: ")
            
            if opcion == "1":
                reporte_vehiculos_registrados()
            elif opcion == "2":
                reporte_vehiculos_retirados()
            elif opcion == "3":
                reporte_vehiculos_sin_retirar()
            elif opcion == "4":
                reporte_total_pagos()
            elif opcion == "5":
                reporte_tiempo_promedio()
            elif opcion == "6":
                reporte_lista_usuarios()
            elif opcion == "7":
                reporte_tiempo_maximo_minimo()
            elif opcion == "8":
                break
            else:
                print("❌ Opción no válida❌. Intente de nuevo.")
    else:
        print("❌ Credenciales incorrectas❌.")        
        
def reporte_vehiculos_registrados():
    print("\n Reporte📋: Total de vehículos registrados")
    total = len(usuarios)
    print(f"Total de naves registradas: {total}")
    print("-" * 40)

def reporte_vehiculos_retirados():
    print("\n Reporte📋: Total de vehículos retirados")
    total = len(historial_naves_retiradas)
    print(f"Total de naves retiradas: {total}")
    if historial_naves_retiradas:
        print("\nHistorial de naves retiradas:")
        for registro in historial_naves_retiradas:
            print(f"- {registro['placa']} | {registro['tripulante']['nombre']} {registro['tripulante']['apellido']} | ${registro['cobro']}")
    print("-" * 40)

def reporte_vehiculos_sin_retirar():
    print("\n Reporte📋: Total de naves sin retirar")
    total = len(naves_en_hangar)
    print(f"Total de naves sin retirar (en hangar): {total}")
    if naves_en_hangar:
        print("\nNaves actualmente en el hangar:")
        for placa, hora_entrada in naves_en_hangar.items():
            tripulante = usuarios[placa]
            tiempo_transcurrido = datetime.datetime.now() - hora_entrada
            minutos = int(tiempo_transcurrido.total_seconds() / 60)
            print(f"- {placa} | {tripulante['nombre']} {tripulante['apellido']} | {minutos} minutos")
    print("-" * 40)

def reporte_total_pagos():
    print("\n Reporte📋: Total pago de naves retiradas")
    print(f"Total recaudado: ${total_recaudado}")
    print(f"Cantidad de naves retiradas: {cantidad_naves_retiradas}")
    if cantidad_naves_retiradas > 0:
        promedio = total_recaudado / cantidad_naves_retiradas
        print(f"Pago promedio por nave: ${promedio:.2f}")
    print("-" * 40)

def reporte_tiempo_promedio():
    print("\n Reporte📋: Tiempo promedio de estancia")
    if cantidad_naves_retiradas > 0:
        promedio_minutos = tiempo_total_estancia / cantidad_naves_retiradas
        horas = int(promedio_minutos // 60)
        minutos = int(promedio_minutos % 60)
        print(f"Tiempo promedio de estancia: {horas} horas y {minutos} minutos")
        print(f"Total de minutos promedio: {promedio_minutos:.2f}")
    else:
        print("No hay datos suficientes para calcular el promedio.")
    print("-" * 40)

def reporte_lista_usuarios():
    print("\n Reporte📋: Lista de usuarios")
    if usuarios:
        print("Lista completa de tripulantes registrados:")
        for placa, datos in usuarios.items():
            estado = "En hangar" if placa in naves_en_hangar else "Fuera del hangar"
            print(f"- {placa} | {datos['nombre']} {datos['apellido']} | Doc: {datos['documento']} | {estado}")
    else:
        print("No hay usuarios registrados.")
    print("-" * 40)

def reporte_tiempo_maximo_minimo():
    print("\n Reporte📋: Nave con tiempo máximo y mínimo")
    if historial_naves_retiradas:
        # Encontrando tiempo máximo y mínimo 
        max_tiempo = historial_naves_retiradas[0]
        min_tiempo = historial_naves_retiradas[0]

        for registro in historial_naves_retiradas:
            if registro['tiempo_minutos'] > max_tiempo['tiempo_minutos']:
                max_tiempo = registro
            if registro['tiempo_minutos'] < min_tiempo['tiempo_minutos']:
                min_tiempo = registro
        
        print(" Nave con MAYOR tiempo de estancia:")
        print(f"  Placa: {max_tiempo['placa']}")
        print(f"  Tripulante: {max_tiempo['tripulante']['nombre']} {max_tiempo['tripulante']['apellido']}")
        print(f"  Tiempo: {max_tiempo['tiempo_minutos']} minutos")
        print(f"  Cobro: ${max_tiempo['cobro']}")
        
        print("\n Nave con MENOR tiempo de estancia:")
        print(f"  Placa: {min_tiempo['placa']}")
        print(f"  Tripulante: {min_tiempo['tripulante']['nombre']} {min_tiempo['tripulante']['apellido']}")
        print(f"  Tiempo: {min_tiempo['tiempo_minutos']} minutos")
        print(f"  Cobro: ${min_tiempo['cobro']}")
    else:
        print("No hay datos suficientes para mostrar este reporte.")
    print("-" * 40)          
        

def menu():
    while True:
        mostrar_encabezado()
        print("\n1. Registrar tripulante")
        print("2. Ingresar nave")
        print("3. Retirar nave")
        print("4. Ver reporte del hangar")
        print("5. Panel de Administración")
        print("6. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            registrar_tripulante()
        elif opcion == "2":
            ingresar_nave()
        elif opcion == "3":
            retirar_nave()
        elif opcion == "4":
            ver_reporte()
        elif opcion == "5":
            menu_administrador()
        elif opcion == "6":
            print("\n Hasta la próxima misión, comandante👌.")
            break
        else:
            print("❌ Opción no válida❌. Intente de nuevo.")

# Ejecutar
menu()
