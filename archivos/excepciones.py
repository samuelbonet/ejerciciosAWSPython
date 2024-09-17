nombre=input("Archivo")
try:
    archivo_leer=open(nombre,"r")
    print("Archivo encontrado y abierto en lectura")
except FileNotFoundError:
        archivo_leer=open(nombre,"w")
        print("Archivo creado porque no se ha encontrado")
archivo_leer.close()