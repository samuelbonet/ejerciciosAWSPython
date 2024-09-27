import pyfiglet
entrada = input("Input: ")
fig = pyfiglet.Figlet(font='doom')
salida = fig.renderText(entrada) 
print("Output:\n",salida)

