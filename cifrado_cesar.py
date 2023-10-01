"""
Cifrado César: En el cifrado César, se utiliza un desplazamiento fijo como clave secreta para cifrar el mensaje. 
                Cada letra del mensaje se desplaza un número fijo de posiciones hacia adelante o hacia atrás en el alfabeto. 
                El desplazamiento se determina mediante una clave numérica.
Cifrado Atbash: En el cifrado Atbash, no se utiliza un desplazamiento fijo. 
                En cambio, cada letra del alfabeto se reemplaza por su letra correspondiente en el alfabeto invertido. 
                Es decir, la letra "A" se reemplaza por "Z", "B" por "Y", "C" por "X", y así sucesivamente. No se necesita una clave numérica para determinar el desplazamiento, ya que es siempre el mismo.

"""

def cifrar_cesar(texto, desplazamiento):
    alfabeto_normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alfabeto_cesar = alfabeto_normal[desplazamiento:] + alfabeto_normal[:desplazamiento]
    
    texto_cifrado = ""
    
    for letra in texto:
        if letra.isalpha():
            if letra.isupper():
                indice = alfabeto_normal.index(letra)
                letra_cifrada = alfabeto_cesar[indice]
                texto_cifrado += letra_cifrada
            else:
                indice = alfabeto_normal.index(letra.upper())
                letra_cifrada = alfabeto_cesar[indice].lower()
                texto_cifrado += letra_cifrada
        else:
            # Mantener caracteres no alfabéticos sin cambios
            texto_cifrado += letra
    
    return texto_cifrado

def descifrar_cesar(texto_cifrado, desplazamiento):
    return cifrar_cesar(texto_cifrado, -desplazamiento)  # El descifrado es el mismo que el cifrado, pero con desplazamiento negativo

# Ejemplo de cifrado César con un desplazamiento de 3
mensaje_original = "HELLO"
desplazamiento = 3
mensaje_cifrado = cifrar_cesar(mensaje_original, desplazamiento)
print("Texto cifrado César:", mensaje_cifrado)

# Ejemplo de descifrado
mensaje_descifrado = descifrar_cesar(mensaje_cifrado, desplazamiento)
print("Texto descifrado César:", mensaje_descifrado)
