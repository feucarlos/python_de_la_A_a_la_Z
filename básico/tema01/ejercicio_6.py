# Comprueba si la cadena es un número flotante válido
def is_valid_float(element: str) -> bool:
    try: 
        float(element)
        return True
    except ValueError:
        return False


# Se pide ingresar un número
numero = input("Dame un número decimal: ")
numero = numero.strip() #se borran espacios en blanco

if(is_valid_float(numero)):
    numero = int(float(numero)) # trunca y deja la parte entera
elif(numero.isdecimal()):
    numero = int(numero)

if (type(numero) == int):
    print("cadena: ", numero)
    print("el dato  es ", type(numero))
    numero = str(numero)
    print("ahora es ", type(numero))
else:
    print("Dato no válido")
