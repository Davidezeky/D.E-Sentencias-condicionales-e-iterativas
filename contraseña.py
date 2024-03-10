

from string import ascii_lowercase
import getpass


abc = ascii_lowercase
print(type(abc))

pasword = getpass.getpass("ingresa la clave: ")
clave = ""
contador = 0
for letra in pasword:
    for caracter in abc: 
        contador += 1
        if letra == caracter:
            break  

print(f"la palabra se encontro en {contador} intentos")