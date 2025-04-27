import numpy as np 
lista_idades = [1, 2, 3, 4, 5, 10, 20, 34, 98]
# Soma de todas as idades
np.sum(lista_idades)
# Quantidade de idades
len(lista_idades)
# Média das idades
np.sum(lista_idades)/len(lista_idades)
# Outra forma de fazer a média
media = np.mean(lista_idades)
print ("Média aritmética", media)
# Mediana
mediana = np.median(lista_idades)
