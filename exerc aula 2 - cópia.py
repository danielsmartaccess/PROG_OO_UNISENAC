'''
def contar_caracteres(texto):
    return len(texto)

print(contar_caracteres(texto = input("Digite texto: ")))

import math

def contar_digitos(numero):
    return int(math.log10(numero))+1 if numero != 0 else 1

print(contar_digitos(numero = int(input("Digite NÙMERO: ")))) 

def contar_digitos(numero):
    return len(str(numero))

print(contar_digitos(numero = input("Digite NÙMERO: "))) 

def inverter_numero(numero):
    numero_invertido = str(numero)[::-1]
    return int(numero_invertido)

print(inverter_numero(numero = input("Digite NÙMERO: ")))

import random

def gerar_numeros_aleatorios():
    numeros = random.sample(range(10, 1001), 10)
    return numeros
print(gerar_numeros_aleatorios()) # Saída: [573, 689, 363, 321, 164, 470, 76, 654, 137, 756]'''

def estatisticas_lista(lista):
    soma = sum(numeros)
    menor = min(numeros)
    maior = max(numeros)
    media = soma / len(numeros)
    return soma, menor, maior, media

lista = []
while True:
    numero = int(input("Digite um número inteiro (ou 0 para encerrar): "))
    if numero == 0:
        break
    lista.append(numero)

soma, menor, maior, media = estatisticas_lista(lista)

print(f"Soma: {soma}")
print(f"Menor: {menor}")
print(f"Maior: {maior}")
print(f"Média: {media}")

