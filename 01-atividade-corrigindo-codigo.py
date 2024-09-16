"""Você está fazendo parte de uma equipe de desenvolvimento e precisa corrigir um código que um de seus colegas não concluiu.
 O objetivo é criar um algoritmo que leia 5 números inteiros e, em seguida, mostre na tela:

1. A quantidade de números pares e ímpares.
2. A quantidade de números positivos e negativos.
3. A quantidade de números inseridos.
4. O maior e o menor número.
5. A média de números pares.
6. A média de números ímpares.
7. A média de todos os números inseridos.
8. Mostrar os números lidos na ordem inversa."""
import os 
os.system("cls || clear")
# Variáveis para armazenar os números
numeros = []
numeros_pares = []
numeros_impares = []
numeros_negativos = []
numeros_positivos = []
contador_par = 0
contador_impar = 0
contador_positivo = 0
contador_negativo = 0
QTD = 5



for i in range(QTD):
    numero = int(input(f"Digite {i +1}° número: "))
    numeros.append(numero)
#1. A quantidade de números pares e ímpares.
    if numero == 0  or numero % 2 == 0:
      numeros_pares.append(numero)
      contador_par += 1
    else:
        numeros_impares.append(numero)  
        contador_impar += 1
#2. A quantidade de números positivos e negativos.
    if numero < 0:
        numeros_negativos.append(numero)
        contador_negativo += 1
    else:
      numeros_positivos.append(numero)
      contador_positivo += 1 
#3. A quantidade de números inseridos.
print(f"A quantidade de números inseridos foi de : {QTD} ")
#4. O maior e o menor número.
maior_numero = max(numeros)
menor_numero = min(numeros)
#5. A média de números pares.
if contador_par != 0:
  media_pares = sum(numeros_pares) / len(numeros_pares)  
#6. A média de números ímpares.
if contador_impar != 0:
  media_impares = sum(numeros_impares) / len(numeros_impares)  
#7. A média de todos os números inseridos.
media_total = sum(numeros) / len(numeros)
 
#caso o user não digite numeros pares/impares/positivos/negativos
if contador_positivo == 0:
  numeros_positivos = 0
if contador_negativo == 0:
  numeros_negativos = 0
if contador_par == 0:
    numeros_pares.append(0)
if contador_impar == 0:
    numeros_impares.append(0)
if contador_positivo == 0:
    numeros_positivos.append(0)
if contador_negativo == 0:
    numeros_negativos.append(0)


#saída do código para contador par e impar
print(f"A quantidade de números pares foram {contador_par}\nA quantidade de números impares foram {contador_impar}")
#saída do código para números pares e impares
print(f"Os números pares foram {numeros_pares}\nOs números impares foram {numeros_impares}")
#saída do código para números positivos e negativos
print(f"Os números negativos são{numeros_negativos},\n Os números posistivos foram {numeros_positivos}")
#saída para a média de todos os números
print(f" A media total foi de {media_total},\n A media de pares foi de {media_pares}, A media de impares foi  {media_impares}")
#8. Mostrar os números lidos na ordem inversa.
for i, numerostotais in enumerate(reversed(numeros)):
 print(f" numero reverso é {numerostotais}")

