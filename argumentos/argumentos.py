import sys
def main():
    if len(sys.argv) < 2:
        nombre=input("¿Cómo te llamas?")
        print(f'Hola, {nombre or "mundo"}!')
    elif len(sys.argv) == 3:
        print("Hola",sys.argv[1])
    else:
        sys.exit("Utiliza solamente 1 argumento \n python hola.py [nombre]")
        
if __name__=="__main__":
    main()