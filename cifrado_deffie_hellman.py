# Implementación simplificada del algoritmo de Diffie-Hellman

# Parámetros públicos (acordados por ambas partes)

p = 23  # Número primo
g = 5   # Generador (debe ser un número menor que p)

# Parte A elige un número secreto 'a' menor que p
a = 6

# Parte B elige un número secreto 'b' menor que p
b = 15

# Cálculo de las claves públicas de A y B
A = (g ** a) % p
B = (g ** b) % p

# Intercambio de las claves públicas A y B

# Parte A calcula la clave compartida
clave_compartida_A = (B ** a) % p

# Parte B calcula la clave compartida
clave_compartida_B = (A ** b) % p

# Ambas partes ahora tienen la misma clave compartida
print("Clave compartida A:", clave_compartida_A)
print("Clave compartida B:", clave_compartida_B)
