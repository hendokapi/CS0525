valore = input('Valore (0 per uscire): ')
while valore != '0':
    print('ciao')
    valore = input('Valore (0 per uscire): ')

# controlli sugli input
numero = input('Inserisci un numero: ')
# while numero.isdigit() == False:
while not numero.isdigit():
    if numero.isalpha():
        print('ma ci sono solo lettere!')
    elif numero.isalnum():
        print('misto di lettere e numeri!')
    numero = input('Deve essere un numero, inserisci un numero: ')

numero = int(numero)

print(numero / 2)