'''import tkinter as tk

ventana=tk.Tk()

bienvenida = tk.label(text="Hola,mundo")
bienvenida.pack()

ventana.mainloop()'''

SPANISH_YES= "S","SI","SÍ"
def main():
    game_over = False
    
    try:
        while not game_over:
            print("hola")
             
    except KeyboardInterrupt:
        print("\n\n Ueee\n")    

def usuario_salir():
    salir= input("¿Quieres salir? (S/N)").upper()
    if salir in SPANISH_YES:
        print ("Gracias")
                
if __name__=="__main__":
    main()