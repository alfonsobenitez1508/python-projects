from src.datos import libros, usuarios, prestamos, historial_prestamos, hoy
from datetime import timedelta

def agregar_libro(titulo, autor, genero, año):
    """Agrega un libro nuevo al diccionario: libros.

    Args:
        titulo: Título del libro.
        autor: Autor del libro.
        genero: Género del libro.
        año: Año del libro.
    Returns:
        diccionario: Diccionario del libro agregado.
    """
    while True:
        try:
            int(año)
            break
        except ValueError:
            print("Año no válido, registre el año correctamente:")
            año = int(input("Año: "))
    iden=[]
    for diccionario in libros:
        iden.append(diccionario["id"])
    iden_nuevo = max(iden)+1
    diccionario = {"id": iden_nuevo, "titulo": titulo, "autor": autor, "genero": genero, "año": año, "disponible": True, "veces_prestado": 0}
    libros.append(diccionario)
    return diccionario

#2. Función que busque libros por criterio
#   Recibe: campo (titulo, autor, genero, año) y valor
#   Devuelve: lista de libros que coincidan

def buscar_libros(campo, valor):
    """ Busca libros por criterio (titulo, autor, genero o año)
    
    Args:
        campo: Campo que se quiere buscar.
        valor: Valor del campo.
    """
    campo = campo.lower().strip()
    while True:
        if campo in ["titulo", "autor", "genero", "año"]:
            break
        else:
            campo = input("Escriba un campo válido: ").lower().strip()

    while campo == "año":
        try:
            valor = int(valor)
            break
        except ValueError:
            valor = input("Escriba un año válido: ")

    coincidencias = []
    for diccionario in libros:
        if campo == "año":
            if valor == diccionario["año"]:
                coincidencias.append(diccionario)    
        else:
            if valor.lower() == diccionario[campo].lower():
                coincidencias.append(diccionario)
    print(coincidencias)


def eliminar_libro(id_libro):
    """Elimina un libro por id. El libro se elimina si no tiene préstamos activos.

    Args:
        id_libro: ID del libro a eliminar
    Returns:
        True: Si el libro se eliminó.
        False: Si el libro no se eliminó.
    """
    for i in range(len(libros)):
        diccionario = libros[i]
        if id_libro==diccionario["id"]:
            for j in prestamos:
                if j["id_libro"] == id_libro:
                    return False
            del libros[i]
            return True
    return False

def libros_disponibles():
    """Devuelve una lista de los libros que se encuentran disponibles.
    """
    idens=[i["id"] for i in prestamos]
    libros_disp = []
    for diccionario in libros:
        disponibilidad = diccionario["id"] not in idens
        if disponibilidad ==True:
            libros_disp.append(diccionario)
            print(f"{diccionario} disponible == {True}")


def estadisticas_libros():
    """Imprime un diccionario con las estadísticas de los libros.
    """
    total_libros = len(libros)
    total_disponibles = total_libros-len(prestamos)
    total_prestados = len(prestamos)
    generos={}
    num_max_pres = 0
    for diccionario in libros:
        genero = diccionario["genero"]
        generos[genero] = generos.get(genero, 0)+1

        if diccionario.get('veces_prestado') > num_max_pres:
            num_max_pres = diccionario["veces_prestado"]
            libro_mas_prestado = diccionario["titulo"]

        if num_max_pres == 0:
            libro_mas_prestado = None
    dicc = {
    "total_libros": total_libros,
    "total_disponibles": total_disponibles,
    "total_prestados": total_prestados,
    "generos": generos,
    "libro_mas_prestado": libro_mas_prestado
    }
    print(dicc)


def registrar_usuario(nombre, email):
    """Registra un usuario nuevo en lista de diccionarios: 'usuarios'.

    Se crea un ID nuevo (1 número mayor al ID más grande).

    Args: 
        nombre: nombre del nuevo usuario
        email: email del usuario nuevo
    Returns:
        dicc: Diccionario del usuario nuevo
        None: Si el email existe en 'usuarios'
    Raises:
        ValueError: si no se escribe un email o si no está en el formato correcto
    """
    while True:
        if "@" in email:
            break
        else:
            print("Escribir un correo válido: ")
            email = input("Email: ")

    #Inicializar variable
    id_mayor = 0

    #Iniciar loop para detectar si ya se encuentra el email en usuarios, así como para encontrar el 
    #ID mas alto y generar uno nuevo
    for diccionario in usuarios:
        if diccionario['email'] == email:
            raise ValueError('Email ya está registrado')
        if diccionario['id'] > id_mayor:
            id_mayor = diccionario['id']

    id_nuevo = id_mayor+1

    dicc = {
        'id': id_nuevo,
        'nombre': nombre,
        'email': email,
        'prestamos_activos': [],
        'historial': []
    }
    usuarios.append(dicc)
    return dicc


def buscar_usuario_por_email(email):
    for diccionario in usuarios:
        if email ==diccionario['email']:
            return diccionario
    return None


#3. Función que devuelva los usuarios con más préstamos
#   Recibe: n (cantidad de usuarios a devolver)
#   Devuelve: lista de tuplas (nombre, cantidad_prestamos) ordenada descendentemente

def usuarios_mas_activos(n=3):
    usuarios_a_devolver = []
    for diccionario in usuarios:
        if len(diccionario['prestamos_activos']) != 0:
            usuarios_a_devolver.append((diccionario['nombre'], diccionario['prestamos_activos']))
    usuarios_a_devolver.sort(key=lambda x: len(x[1]), reverse=True)
    return usuarios_a_devolver[0:n]


#4. Función que verifique si un usuario puede pedir préstamo
#   Recibe: id_usuario
#   Reglas: máximo 3 préstamos activos
#   Devuelve: True o False

def puede_pedir_prestamo(id_usuario):
    for diccionario in usuarios:
        if diccionario['id']==id_usuario:
            if len(diccionario['prestamos_activos']) > 3:
                return False
    return True


#5. Función que devuelva el perfil completo de un usuario
#   Recibe: id_usuario
#   Devuelve: diccionario con nombre, email, prestamos_activos (títulos),
#             historial (títulos), total_prestamos

def perfil_usuario(id_usuario):
    perfil = {}
    for diccionario in usuarios:
        if diccionario['id'] == id_usuario:
            perfil['nombre'], perfil['email'] = diccionario['nombre'], diccionario['email']
            ids_prestamos_activos = [i for i in diccionario['prestamos_activos']]
            ids_historial = [i for i in diccionario['historial']]
            titulos_prestamos_activos = []
            titulos_historial = []
            i=0
            for libro in libros:
                if libro['id'] in ids_prestamos_activos:
                    titulos_prestamos_activos.append(libro['titulo'])
                if libro['id'] in ids_historial:
                    titulos_historial.append(libro['titulo'])
                i+=1
            perfil['prestamos_activos'], perfil['historial'] = titulos_prestamos_activos, titulos_historial
            perfil['total_prestamos'] = len(perfil['prestamos_activos']) + len(perfil['historial'])
    return perfil


def realizar_prestamo(id_usuario, id_libro):
    """Verifica si el usuario y el libro existen, si el libro está disponible y si el usuario puede pedirlo.
    
    Se actualizan a los diccionarios los items: disponible y veces prestado
    
    Args:
        id_usuario: ID del usuario al que se le hará el préstamo.
        id_libro: ID del libro a prestar.
    Returns:
        resultado: Diccionario con las claves: éxito, mensaje (si el libro está disponible o el usuario puede pedirlo) y préstamo
        ValueError: Si se establece un valor inválido.
    """
    #Valida el tipo de dato
    while True:            
        try: 
            id_usuario = int(id_usuario)
            id_libro = int(id_libro)
            break
        except ValueError:
            print("Escriba valores válidos")
            id_usuario = input("ID de usuario: ")
            id_libro = input("ID de libro: ")

    resultado = {
        'exito': False,
        'mensaje': "",
        'prestamo': False
    }
    #Verificar existencia de usuario
    lista_id_us = [i['id'] for i in usuarios]
    lista_id_lib = [i['id'] for i in libros]
    if id_usuario not in lista_id_us:
        resultado['mensaje'] = 'ID de usuario no existe'
        return resultado
        
        
    if id_libro not in lista_id_lib:
        resultado['mensaje'] = 'ID de libro no existe'
        return resultado

    #Verifica si el libro está disponible
    for libro in libros:
        if libro['id']==id_libro and libro['disponible'] == False:
            resultado['mensaje'] = "El libro no está disponible"
            return resultado


    #Verifica si se puede pedir un préstamo
    for usuario in usuarios:
        if usuario['id']==id_usuario and len(usuario['prestamos_activos'])>3:
            resultado['mensaje'] = 'El usuario no puede pedir un préstamo'
            return resultado

        elif usuario['id']==id_usuario:
            usuario['prestamos_activos'].append(id_libro)
    for libro in libros:
        if libro['id'] ==id_libro:
            libro['veces_prestado'] += 1
            libro['disponible'] = False
            titulo =libro['titulo']

    fecha_entrega = hoy + timedelta(days=14)
    prestamos.append({'id_libro': id_libro, 'id_usuario':id_usuario, 'fecha_prestamo': hoy, "fecha_entrega": fecha_entrega})
    resultado['exito'] = True
    resultado['mensaje'] = f"Libro '{titulo}' prestado"
    resultado['prestamo'] = True
    return resultado



#2. Función que devuelva un libro
#   Recibe: id_usuario, id_libro
#   Actualiza: libro.disponible = True
#              usuario.prestamos_activos.remove(id_libro)
#              usuario.historial.append(id_libro)
#   Mueve de prestamos a historial_prestamos
#   Devuelve: True si se devolvió correctamente

def devolver_libro(id_usuario, id_libro):
    """Actualiza el estatus de determinado libro en el diccionario 'libros' y el estatus del usuario en el diccionario de usuarios, moviendo el libro de prestamos_activos a historial

    Args:
        id_usuario: ID del usuario.
        id_libro: ID del libro
    Returns: 
        True: Si se devuelve el libro correctamente.
        False: Si no se devuelve el libro correctamente
    """
    while True:
        try:
            id_usuario = int(id_usuario)
            id_libro = int(id_libro)
            break
        except ValueError:
            print("ID inválido")
            id_usuario = input("ID usuario: ")
            id_libro = input("ID libro: ")

    while True:
        if id_usuario not in [i["id"] for i in usuarios]:
            return False
        break

    for diccionario in usuarios:
        if diccionario['id'] == id_usuario and id_libro in diccionario['prestamos_activos']:
            diccionario['prestamos_activos'].remove(id_libro)
            if id_libro not in diccionario['historial']:
                diccionario['historial'].append(id_libro)
            for libro in libros:
                if libro['id'] == id_libro:
                    libro['disponible'] = True
            for prestamo in prestamos[:]:
                if prestamo['id_libro'] == id_libro:
                    prestamos.remove(prestamo)
                    historial_prestamos.append(prestamo)
            return True
            
    return False



#3. Función que calcule multas por retraso
#   Recibe: dias_retraso
#   Regla: $5 por día de retraso
#   Devuelve: monto de la multa

def calcular_multa(dias_retraso):
    """Calcula la multa en base a los días de atraso. $5 por día.
    
    Args:
        dias_retraso: Numero de días de atraso.
    Returns:
        monto: Monto total de la multa
    """
    monto = dias_retraso*5
    return monto



#4. Función que devuelva todos los préstamos activos de un usuario
#   Recibe: id_usuario
#   Devuelve: lista de diccionarios con info del préstamo y del libro

def prestamos_activos_usuario(id_usuario):
    """Devuelve una lista de los préstamos activos del usuario

    Args:
        id_usuario: ID del usuario.
    Returns:
        prest_act: Lista de diccionarios con la información del préstamos y el libro
    """
    prest_act = [
    ]
    for usuario in usuarios:
        if id_usuario == usuario['id']:
            for libro in libros:
                if libro['id'] in usuario['prestamos_activos']:
                    print(libro['id'])
                    prest_act.append({
                        "libro": {i: j for i, j in libro.items()},
                        "usuario": {i:j for i,j in usuario.items()}
                        })
            return prest_act



#5. Función que renueve un préstamo
#   Recibe: id_prestamo, dias_extra
#   Extiende la fecha de devolución
#   Devuelve: True si se renovó, False si no


def renovar_prestamo(id_prestamo, dias_extra=7):
    """Extiende la fecha de entrega
    
    Args:
        id_prestamo: ID del libro al que se va a renovar el préstamo.
        dias_extra: Días extra a agregar a la fecha de entrega.
    Returns:
        True: Si se renueva exitosamente.
        False: Si no se renueva.
    """
    for libro in prestamos:
        if libro['id'] == id_prestamo:
            libro['fecha_entrega'] += timedelta(days=dias_extra)
            return True
    return False


#1. Función que genere un reporte general de la biblioteca
#   Devuelve: diccionario con todas las estadísticas:
#   - Total libros, disponibles, prestados
#   - Total usuarios, usuarios activos
#   - Total préstamos históricos
#   - Libro más prestado
#   - Usuario más activo
#   - Género más popular

def reporte_general():
    """Genera un reporte con el total de libros, disponibles y prestados, total de usuarios en general y activos, total de préstamos históricos, libro más prestado, usuario más activo y género más popular
    Args:
    Returns:
        estadisticas: Diccionario con reporte general
    """
    estadisticas = {
    }
    #Total de libros
    estadisticas['total_libros'] = len(libros)

    #Libros disponibles
    estadisticas['libros_disponibles'] = len([i for i in libros if i['disponible']==True])

    #Libros prestados
    estadisticas['libros_prestados'] = len([i for i in libros if i['disponible']==False])

    #Total de usuarios
    estadisticas['total_usuarios'] = len(usuarios)

    #Usuarios activos
    estadisticas['usuarios_activos'] = len([i for i in usuarios if len(i['prestamos_activos'])>0])

    #Total de préstamos históricos
    estadisticas['prestamos_historicos'] = sum([i['veces_prestado'] for i in libros])

    #Libro mas prestado
    estadisticas['libro_mas_prestado'] = max(libros, key=lambda x:x['veces_prestado'])['titulo']

    #Usuario mas activo
    estadisticas['usuario_mas_activo'] = max(usuarios, key=lambda x:len(x['prestamos_activos']))['nombre']

    #Genero mas popular
    suma_genero = {}
    for libro in libros:
        suma_genero[libro['genero']] = suma_genero.get(libro['genero'], 0)+ libro['veces_prestado']
    estadisticas['genero_mas_popular'] = max(suma_genero.items(), key=lambda x:x[1])[0]

    print(estadisticas)
                                                             

#2. Función que recomiende libros a un usuario
#   Recibe: id_usuario, n (cantidad de recomendaciones)
#   Basado en: géneros que ha leído, libros populares
#   Devuelve: lista de títulos recomendados

def recomendar_libros(id_usuario, n=3):
    """Devuelve una lista de títulos recomendados en base a los géneros que el usuario ha leído y los libros populares

    Args: 
        id_usuario: ID del usuario
        n: Numero de libros a agregar a la lista
    """
    while True:
        try:
            id_usuario = int(id_usuario)
            n = int(n)
            break
        except ValueError:
            if type(id_usuario) != int:
                print("ID inválido")
                id_usuario = input("ID de usuario: ")
            elif type(n) != int:
                print("Número de recomendaciones inválido")
                n = input("Número de recomendaciones: ")
    if id_usuario not in [i['id'] for i in usuarios]:
        return print("El ID de usuario no existe.")


    #Diccionario = leidos: numero de libros
    generos_leidos = {}
    libros_leidos = []
    for i in usuarios:
        if i['id'] == id_usuario:
            libros_leidos = i['historial']
    for libro in libros:
        if libro['id'] in libros_leidos:
            generos_leidos[libro['genero']] = generos_leidos.get(libro['genero'], 0) + 1

    #Lista de libros populares de los géneros leídos
    libros_populares = sorted([i for i in libros if i['genero'] in generos_leidos], key=lambda i: i['veces_prestado'], reverse=True)
    libros_populares = [i['titulo'] for i in libros_populares]
    libros_recomendados = libros_populares[0:n]
    return libros_recomendados



#3. Función que encuentre libros relacionados
#   Recibe: id_libro, n (cantidad)
#   Basado en: mismo género o mismo autor
#   Devuelve: lista de títulos relacionados

def libros_relacionados(id_libro, n=3):
    """Encuentra y devuelve una lista de títuos de libros relacionados

    Args:
        id_libro: ID del libro.
        n: número de libros
    Returns:
        lista_titulos: Lista de títulos relacionados a id_libro.
    """

    for libro in libros:
        if libro['id'] == id_libro:
            genero = libro['genero']
            autor = libro['autor']

    lista_titulos = [i['titulo'] for i in libros if (i['genero']==genero or i['autor'] == autor) and i['id'] != id_libro]
    lista_titulos = lista_titulos[0:n]
    return lista_titulos



def ranking_libros(criterio="prestado"):
    """Devuelve una lista de libros ordenados según el criterio
    Args: 
        criterio: Puede ser "prestado", "año" o "título".
    Return:
        lista_libros: Lista de libros ordenados según el criterio.
    """
    if criterio not in ["prestado", "año", "titulo"]:
        raise ValueError('Argumento no válido')

    if criterio == "prestado":
        criterio = "disponible"

    lista_libros = sorted(libros, key=lambda i:i[criterio])
    print(f"Libros: {lista_libros}")




#5. Función que exporte reporte a formato texto
#   Recibe: nombre_archivo
#   Guarda el reporte general en un archivo .txt

def exportar_reporte(nombre_archivo):
    with open(f"{nombre_archivo}.txt", "w", encoding="utf-8") as f:
        for l in libros:
            f.write(f'{l["id"]} | {l["titulo"]} | {l["autor"]} | {l["genero"]} | {l["año"]} | {l["disponible"]} | {l["veces_prestado"]}\n')
