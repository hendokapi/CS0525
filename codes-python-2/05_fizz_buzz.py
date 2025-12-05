'''
FizzBuzz
Scrivere un programma che stampi i primi 100 numeri ma al posto dei numeri divisibili per 3 stampi Fizz, al posto di quelli divisibili per 5 stampi Buzz e al posto di quelli divisibili sia per 3 che per 5 stampi FizzBuzz.

Esempio di output:

1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, ...
'''
'''
n % 3
n % 5 
n % 15
'''

# i = 1
# while i <= 100:
#     print(i)
#     i += 1 # i = i + 1

# for i in range(1, 31):
    # if i % 3 == 0 and i % 5 == 0:
    #     print('FizzBuzz')
    # elif i % 5 == 0:
    #     print('Buzz')
    # elif i % 3 == 0:
    #     print('Fizz')
    # else:
    #     print(i)

    # if i % 3 == 0:
    #     if i % 5 == 0:
    #         print('FizzBuzz')
    #     else:
    #         print('Fizz')
    # elif i % 5 == 0:
    #     print('Buzz')
    # else:
    #     print(i)

    # if i % 3 == 0 and i % 5 != 0:
    #     print('Fizz')
    # elif i % 5 == 0 and i % 3 != 0:
    #     print('Buzz')
    # elif i % 3 == 0 and i % 5 == 0:
    #     print('FizzBuzz')
    # else:
    #     print(i)

# versione con tabella

numbers = int(input('n numeri: '))
columns = int(input('n colonne: '))
larghezza = int(input('caratteri x cella: '))

print((columns * (larghezza + 3)) * '-') # prima linea di contorno della tabella

for number in range(1, numbers + 1):
    if (number - 1) % columns == 0:
        print("| ", end='')

    if number % 3 == 0 and number % 5 == 0:
        print(f'{'FizzBuzz':^{larghezza}}', end='')
    elif number % 3 == 0:
        print(f'{'Fizz':^{larghezza}}', end='')
    elif number % 5 == 0:
        print(f'{'Buzz':^{larghezza}}', end='')
    else:
        print(f'{number:^{larghezza}}', end='')

    # serve a capire quando cambiare riga
    if number % columns == 0:
        print(" |")
        print((columns * (larghezza + 3)) * '-') # linea di separazione tra righe 
    else:
        print(end=' | ') # separatore tra celle
