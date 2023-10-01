def cifrar_atbash(texto):
    alfabeto_normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alfabeto_atbash = alfabeto_normal[::-1]
    
    texto_cifrado = ""
    
    for letra in texto:
        if letra.isalpha():
            if letra.isupper():
                indice = alfabeto_normal.index(letra)
                letra_cifrada = alfabeto_atbash[indice]
                texto_cifrado += letra_cifrada
            else:
                indice = alfabeto_normal.index(letra.upper())
                letra_cifrada = alfabeto_atbash[indice].lower()
                texto_cifrado += letra_cifrada
        else:
            # Mantener caracteres no alfabéticos sin cambios
            texto_cifrado += letra
    
    return texto_cifrado

def descifrar_atbash(texto_cifrado):
    return cifrar_atbash(texto_cifrado)  # El descifrado Atbash es el mismo que el cifrado


mensaje_original = "HELLO"
mensaje_cifrado = cifrar_atbash(mensaje_original)
print("Texto cifrado Atbash:", mensaje_cifrado)

mensaje_descifrado = descifrar_atbash(mensaje_cifrado)
print("Texto descifrado Atbash:", mensaje_descifrado)

