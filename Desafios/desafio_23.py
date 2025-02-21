#trocar letras por numeros
import string

a = list(string.ascii_lowercase)
b=[]
palavra = input('Digite uma palavra: ').lower()

for letra in palavra:
    numero = a.index(letra) + 1 
    b.append(numero)
print(b) 