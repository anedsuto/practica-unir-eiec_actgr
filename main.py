# Diferentes acciones con las palabras ingresadas

def main():
 
    cadena = input ("Dime unas palabras: ")
    contar_palabras(cadena)
    factorial(23)

    
# Cuenta las palabras recibidas por consola
def contar_palabras(palabras):
    if palabras != None:
        separarPalabras= palabras.split(' ')

        print("En total me dijiste " , len(separarPalabras) , "palabras")
     
def factorial(n):
    fact = 1

    for i in range(1,n+1):
     fact = fact * i

    print("El factorial es : "end="")
    print (fact)

main()
