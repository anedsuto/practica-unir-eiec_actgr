# Diferentes acciones con las palabras ingresadas

def main():
 
    cadena = input ("Dime unas palabras: ")
    contar_palabras(cadena)

    
# Cuenta las palabras recibidas por consola
def contar_palabras(palabras):
    if palabras != None:
        separarPalabras= palabras.split(' ')

        print("En total me dijiste " , len(separarPalabras) , "palabras")

main()
