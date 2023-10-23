# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
numero1 = int(input("Insira um número: "))
numero2 = int(input("Insira um número: "))
numero3 = int(input("Insira um número: "))
Numeros = [numero1, numero2, numero3]
maior = numero1
if numero2 > maior:
    maior = numero2
if numero3 > maior:
    maior = numero3
print(f"O maior número da lista é {maior}")
menor = numero1
if numero2 < menor:
   menor = numero2
if numero3 < menor:
   menor = numero3
print(f"O menor número da lista é {menor}")

