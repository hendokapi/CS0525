lista = [5, 7, 8, 1, 4, 9, 2]

lista_nuova = []
for indice in range(len(lista) - 1, -1, -1):
    lista_nuova.append(lista[indice])

print(lista_nuova)
