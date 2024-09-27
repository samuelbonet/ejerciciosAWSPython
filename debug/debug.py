'''Errores de excepciones cuando no se cumple la condicion
ages = [20, 15, 30, -1]

def loguserages(ages):
    for age in ages:
        try:
            assert age >= 0, "Invalid age was supplied"
       
        except AssertionError as e:
            print(f"Error para la edad {age}: {e}")

loguserages(ages)
'''

import logging

logging.basicConfig(filename="app.log", level=logging.DEBUG)

logging.debug("Este es un mensaje de depuración.")
logging.info("Este es un mensaje informativo.")
logging.warning("Este es un mensaje de advertencia.")
logging.error("Este es un mensaje de error.")
logging.critical("Este es un mensaje crítico.")

