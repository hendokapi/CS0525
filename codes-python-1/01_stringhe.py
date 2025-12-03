# # commento singola riga
# '''
# questo è un commento multiriga

# numero_testuale = "27"
# numero_testuale / 5
# '''

# # utilizzo di ' e di " per creare le stringhe
# saluto = "Hello World"
# testo1 = "l'amica di Gigi"
# testo2 = 'Gigi ha detto: "non so che dire"'
# # escaping dei caratteri speciali con il simbolo \
# testo3 = 'l\'amica di Gigi ha detto: "non so che dire"'

# name = 'Gigi'
# print(f"Ciao {name} come \nstai? {saluto}")

# # stringa multilinea
# testo_lungo = f'''ciao {name}
# come
# stai?'''

# print()
# print(testo_lungo)
# print()

# print(saluto)
# print(testo1)
# # cambiare la terminazione del print
# print(testo2, end=saluto)
# print(testo3)

# # concatenazione di stringhe
# print()
# print('CONCATENAZIONE')
# stringa1 = 'Ciao'
# stringa2 = 'a'

# stringa_concatenata = stringa1 + ' ' + stringa2 + ' tutti'
# print(stringa_concatenata)
# print(f"{stringa1} + ' ' +{stringa2}")
# print(f"{stringa1}" + ' ' +f"{stringa2}")

# print(f"{stringa1} {stringa2} tutti")

# result = 100
# number = 200
# print("Il risultato è: " + str(result))
# print(f"Il risultato è: {result + number}")

# Metodi delle stringhe
print()
print('METODI STRINGHE')

stringa = 'Ciao, a tutti quanti come state'

print(stringa.split(sep='Ciao'))
print(stringa.split(sep='a'))

print(stringa.upper())
print(stringa.lower())

string_user = input("Inserisci un umero: ")
print(string_user.isdigit()) # solo numeri
print(string_user.isnumeric()) # include anche alcuni caratteri speciali
print(string_user.isdecimal()) 
print(string_user.isalpha()) # solo lettere
print(string_user.isalnum()) # lettere e numeri

# per verificare i float va tentata la conversione
float('5')
