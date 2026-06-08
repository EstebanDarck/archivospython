libros = [
    ['Papelucho programador', 'Marcela Paz', 1983],
    ['Don Python de la Mancha', 'Miguel de Cervantes', 1615],
    ['Raw_input y Julieta', 'William Shakespeare', 1597],
    ['La tuplamorfosis', 'Franz Kafka', 1915]
]

datos_autores = {
    'William Shakespeare': [[1564, 4, 26], [1616, 5, 3], 'inglés'],
    'Franz Kafka': [[1883, 7, 3], [1924, 6, 3], 'alemán'],
    'Marcela Paz': [[1902, 2, 28], [1985, 6, 12], 'español'],
    'Miguel de Cervantes': [[1547, 9, 29], [1616, 4, 22], 'español']
}

def buscar_libro(titulo):
    for libro in libros:
        if libro[0] == titulo:
            return libro
    return None

titulo_input = input('Ingrese titulo del libro: ')
libro_encontrado = buscar_libro(titulo_input)

if libro_encontrado:
    nombre_autor = libro_encontrado[1]
    anno_publicacion = libro_encontrado[2]
    info_autor = datos_autores[nombre_autor]
    
    anno_defuncion = info_autor[1][0]
    diferencia = anno_defuncion - anno_publicacion
    
    print(f'Idioma: {info_autor[2]}')
    print(f'Autor: {nombre_autor}')
    print(f'El autor falleció {diferencia} años después de haber escrito el libro.')
else:
    print("Libro no encontrado.")