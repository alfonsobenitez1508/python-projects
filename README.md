# Sistema de Gestión de Biblioteca

Sistema de consola para gestionar libros, usuarios y préstamos de una biblioteca.
Desarrollado en Python como proyecto de portafolio para demostrar fundamentos
de programación: estructuras de datos, funciones, manejo de errores, fechas y
modularización.

---

## Funcionalidades

### Libros
- Agregar libros con ID automático.
- Buscar por título, autor, género o año.
- Eliminar libros (solo si no tienen préstamos activos).
- Ver disponibilidad del catálogo.
- Estadísticas: total, disponibles, prestados, por género, más prestado.

### Usuarios
- Registrar nuevos usuarios con validación de email único.
- Buscar usuario por email.
- Ranking de usuarios más activos.
- Verificar si un usuario puede pedir préstamo (máximo 3 activos).
- Perfil completo con préstamos activos e historial.

### Préstamos
- Realizar préstamos con validación de reglas (disponibilidad, límite, existencia).
- Devolver libros, moviéndolos a historial.
- Calcular multas por retraso ($5 por día).
- Ver préstamos activos de un usuario.
- Renovar préstamos extendiendo la fecha de entrega.

### Reportes
- Reporte general de la biblioteca.
- Recomendaciones basadas en géneros leídos.
- Libros relacionados por género o autor.
- Ranking por popularidad, año o título.
- Exportar catálogo a archivo de texto.

---

## Cómo ejecutar

Requiere Python 3.8 o superior. Sin dependencias externas.

```bash
git clone https://github.com/tu-usuario/biblioteca.git
cd biblioteca
python main.py
```

---

## Estructura del proyecto

```
biblioteca/
├── main.py                  # Punto de entrada
├── README.md
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── datos.py             # Datos iniciales (libros, usuarios, listas)
│   ├── funciones.py         # Todas las operaciones del sistema
│   └── menu.py              # Interfaz de consola
│
└── tests/
    ├── __init__.py
    └── test_basico.py       # Tests unitarios
```

---

## Ejemplo de uso

```
============================================================
MENÚ PRINCIPAL
============================================================

Digita el número correspondiente:
1. Ver todos los libros
2. Buscar libros
3. Agregar un libro
4. Ver usuarios
5. Registrar usuario
6. Realizar un préstamo
7. Devolver libro
8. Ver préstamos activos
9. Ver estadísticas
10. Ver recomendaciones
0. Salir

> 6
ID usuario: 1
ID libro: 3
{'exito': True, 'mensaje': "Libro 'El Principito' prestado", 'prestamo': True}
Presiona enter para continuar
```

---

## Conceptos aplicados

- **Estructuras de datos:** listas, diccionarios, diccionarios anidados.
- **Comprensiones:** listas y diccionarios con filtros.
- **Funciones de orden superior:** `sorted` con `key`, `lambda`, `max`, `min`.
- **Manejo de errores:** `try/except ValueError` para validar entradas.
- **Manejo de fechas:** `datetime.date`, `datetime.timedelta`.
- **Persistencia:** escritura de archivos con `open(..., encoding="utf-8")`.
- **Modularización:** separación de responsabilidades por archivo.
- **Validación de estado:** verificación de disponibilidad, límites y existencia antes de modificar datos.

---

## Reglas del sistema

- Un usuario puede tener **máximo 3 préstamos activos**.
- Un libro no se puede prestar si ya está prestado.
- Un libro no se puede eliminar si alguien lo tiene prestado.
- La fecha de entrega es **14 días** después del préstamo.
- La multa por retraso es de **$5 por día**.
- Los emails de usuario son únicos.

---

## Posibles mejoras futuras

- Persistencia en base de datos (SQLite).
- Interfaz web con Flask o FastAPI.
- Autenticación de usuarios.
- Interfaz gráfica con Tkinter.
- Exportación a JSON o CSV además de TXT.
- Búsqueda avanzada con múltiples criterios combinados.

---

## Autor

**Alfonso Benítez Martínez**

- GitHub: [@tu-usuario](https://github.com/tu-usuario)
- LinkedIn: [tu-perfil](https://linkedin.com/in/tu-perfil)

---

