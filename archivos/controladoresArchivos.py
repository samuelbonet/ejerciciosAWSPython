# Abrir el archivo en modo lectura y leer su contenido
controladoresArchivos = open("archivos/nombres.txt", "r")
print(controladoresArchivos.read())  # Mostrar el contenido del archivo
controladoresArchivos.close()

# Abrir el archivo en modo lectura para almacenar el contenido anterior
archivo_escribir = open("archivos/nombres.txt", "r")
contenido_anterior = archivo_escribir.read()
archivo_escribir.close()

# Abrir el archivo en modo escritura para añadir el nuevo contenido
nuevo_contenido = input("¿Cómo te llamas? ")

# Ahora se abre el archivo en modo "write" (escritura)
archivo_escribir = open("archivos/nombres.txt", "w")
# Escribir el nuevo contenido combinado con el anterior
archivo_escribir.write(contenido_anterior + "," + nuevo_contenido)
archivo_escribir.close()


