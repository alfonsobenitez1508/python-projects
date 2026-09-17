from datetime import date
hoy = date.today()

libros = [
    {"id": 1, "titulo": "Cien años de soledad", "autor": "García Márquez", 
     "genero": "Novela", "año": 1967, "disponible": True, "veces_prestado": 0},
    {"id": 2, "titulo": "1984", "autor": "Orwell", 
     "genero": "Ciencia ficción", "año": 1949, "disponible": True, "veces_prestado": 0},
    {"id": 3, "titulo": "El Principito", "autor": "Saint-Exupéry", 
     "genero": "Fábula", "año": 1943, "disponible": True, "veces_prestado": 0},
    {"id": 4, "titulo": "Don Quijote", "autor": "Cervantes", 
     "genero": "Novela", "año": 1605, "disponible": True, "veces_prestado": 0},
    {"id": 5, "titulo": "Rayuela", "autor": "Cortázar", 
     "genero": "Novela", "año": 1963, "disponible": True, "veces_prestado": 0},
    {"id": 6, "titulo": "Ficciones", "autor": "Borges", 
     "genero": "Cuento", "año": 1944, "disponible": True, "veces_prestado": 0},
    {"id": 7, "titulo": "La casa de los espíritus", "autor": "Allende", 
     "genero": "Novela", "año": 1982, "disponible": True, "veces_prestado": 0},
    {"id": 8, "titulo": "Pedro Páramo", "autor": "Rulfo", 
     "genero": "Novela", "año": 1955, "disponible": True, "veces_prestado": 0}
     ]

usuarios = [
    {"id": 1, "nombre": "Ana García", "email": "ana@mail.com", 
     "prestamos_activos": [], "historial": []},
    {"id": 2, "nombre": "Luis Pérez", "email": "luis@mail.com", 
     "prestamos_activos": [], "historial": []},
    {"id": 3, "nombre": "María López", "email": "maria@mail.com", 
     "prestamos_activos": [], "historial": []},
    {"id": 4, "nombre": "Carlos Ruiz", "email": "carlos@mail.com", 
     "prestamos_activos": [], "historial": []}
]

prestamos = []
historial_prestamos = []
