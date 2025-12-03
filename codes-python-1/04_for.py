for numero in range(10):
    print(f"5 * {numero} = {5*numero}")

lista_spesa = [
    "pasta",
    "pane",
    "pomodori",
    58,
    "peperoni"
]

lista_spesa[2] = 'fragole'
print(lista_spesa[2])
lista_spesa.append('pizza')
print(lista_spesa)
lista_spesa.insert(1, 'ciao')

print('elementi in lista: ', len(lista_spesa))

for cibo in lista_spesa:
    print(cibo)
