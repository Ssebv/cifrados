"""
La operación XOR toma dos valores binarios (0 o 1) y devuelve un resultado que es 1 si exactamente uno de los valores es 1,
y 0 en cualquier otro caso. 

Aquí están todas las combinaciones posibles para la operación XOR:

0 XOR 0 = 0
0 XOR 1 = 1
1 XOR 0 = 1
1 XOR 1 = 0
"""

# Función para cifrar un mensaje
def cifrar(mensaje, clave):
    mensaje_cifrado = ""
    for i in range(len(mensaje)):
        # Aplicar operación XOR entre el carácter del mensaje y el carácter de la clave
        mensaje_cifrado += chr(ord(mensaje[i]) ^ ord(clave[i % len(clave)]))
    return mensaje_cifrado

# Función para descifrar un mensaje cifrado
def descifrar(mensaje_cifrado, clave):
    mensaje_descifrado = ""
    for i in range(len(mensaje_cifrado)):
        # Aplicar nuevamente la operación XOR con el mismo carácter de la clave
        mensaje_descifrado += chr(ord(mensaje_cifrado[i]) ^ ord(clave[i % len(clave)]))
    return mensaje_descifrado

# Mensaje en claro
mensaje_original = "Hola, este es un mensaje secreto."

# Clave secreta (debe ser conocida por ambas partes)
clave_secreta = "clave"

# Cifrar el mensaje
mensaje_cifrado = cifrar(mensaje_original, clave_secreta)

# Mostrar el mensaje cifrado
print("Mensaje cifrado:", hex(int.from_bytes(mensaje_cifrado.encode(), 'big')))

# Descifrar el mensaje cifrado
mensaje_descifrado = descifrar(mensaje_cifrado, clave_secreta)

# Mostrar el mensaje descifrado
print("Mensaje descifrado:", mensaje_descifrado)