from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

"""
1. Se genera una clave aleatoria de 64 bits (clave).
2. Se crea un objeto DES utilizando la clave y el modo ECB.
3. Se asegura de que el mensaje tenga una longitud que sea múltiplo de 8 bytes agregando relleno si es necesario.
4. El mensaje se cifra utilizando el objeto DES.
5. El mensaje cifrado se descifra utilizando el mismo objeto DES.
6. Se muestran los resultados, incluido el mensaje original, el mensaje cifrado y el mensaje descifrado.
"""

# Definir una clave de 8 bytes (64 bits)
clave = get_random_bytes(8)

cipher = DES.new(clave, DES.MODE_ECB) # Modo de operación: Electronic Code Book (ECB)

# Mensaje a cifrar (debe ser múltiplo de 8 bytes) 
mensaje = b"01234567abcdefgh"

while len(mensaje) % 8 != 0: # Si el mensaje no es múltiplo de 8 bytes, agregar bytes nulos
    mensaje += b'\x00'

mensaje_cifrado = cipher.encrypt(mensaje) # Cifrar el mensaje

mensaje_descifrado = cipher.decrypt(mensaje_cifrado) # Descifrar el mensaje

print("Mensaje original:", mensaje)
print("Mensaje cifrado:", mensaje_cifrado)
print("Mensaje descifrado:", mensaje_descifrado.rstrip(b'\x00'))

