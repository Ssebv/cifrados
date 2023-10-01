# Calcula la cantidad de bloques de 64 bits que hay en una frase
frase = "Esta es una frase de ejemplo"

# Convertir la frase a una secuencia de bits
frase_bits = ''.join(format(ord(char), '08b') for char in frase)

# Especificar el tamaño del bloque en bits (por ejemplo, 64 bits)
tamano_bloque = 64

# Calcular cuántos bloques de bits hay en la frase
cantidad_bloques = len(frase_bits) / tamano_bloque

# Redondear hacia arriba para asegurarse de que se incluyan todos los bloques necesarios
import math
cantidad_bloques = math.ceil(cantidad_bloques)

# Imprimir el resultado
print("Cantidad de bloques de {} bits en la frase: {}".format(tamano_bloque, cantidad_bloques))
