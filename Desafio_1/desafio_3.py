#Analisador de Texto:
#Desenvolva um programa que analise um texto e forneça estatísticas, como número de palavras, número de frases, palavras mais frequentes, etc.


print('Digite uma frase para começar')
frase = input()

print(f'a frase contem {len(frase.replace(' ','').replace(".", ""))} letras ')
print(f'a frase contem {len(frase.split( ))} palavras')
print(f'a frase contem {len(frase.split("."))-1} frases')

palavras = frase.split()
contador = {}
for palavra in palavras:
        if palavra in contador:
            contador[palavra] += 1
        else:
            contador[palavra] = 1
    
print(contador)



