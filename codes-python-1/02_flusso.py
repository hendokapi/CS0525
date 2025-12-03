number = input("Inserisci un numero: ")
if number.isdigit():
    number = int(number)

    if number % 2 == 0:
        print("Numero pari")
    else:
        print("Numero dispari")

        if number < 10:
            print("Minore di 10")
        elif number < 20:
            print("Minore di 20")
        else:
            print("Maggiore o uguale a 20")
else:
    print("Dovevi inserire un numero")
print("Fine programma")
