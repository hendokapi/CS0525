# Esercizi Python

## Siti utili

-   [HackerRank](https://www.hackerrank.com/)
-   [LeetCode](https://leetcode.com/)
-   [Codewars](https://www.codewars.com/)

### Calcolo della somma di due numeri

Scrivi un programma che chieda all'utente di inserire due numeri e poi calcoli e mostri la loro somma.

### Calcolo della media

Scrivi un programma che chieda tre numeri all'utente e calcoli la loro media.

### Pari o dispari

Scrivi un programma che chieda un numero all'utente e determini se è pari o dispari.

### Verifica di un anno bisestile

Scrivi un programma che chieda all'utente di inserire un anno e determini se è bisestile.

### Genera un nome per la tua band

Scrivere un programma in Python che genera un nome per una band musicale utilizzando due input forniti dall'utente: la città di origine e il nome del proprio animale domestico.
In questo esercizio, dovrai creare un programma che esegue le seguenti operazioni:

1. Richiesta di Input: Il programma deve chiedere all'utente di inserire:
    - il nome della città di origine
    - il nome del proprio animale domestico
2. Generazione del nome della band: Una volta ricevuti gli input, il programma deve combinare il nome della città e il nome dell'animale in un'unica stringa che rappresenta il nome della band.
3. Output: Il programma deve stampare a video il nome generato per la band.

-   Esempio di input:
    -   Città di origine: Roma
    -   Nome dell'animale: Max
-   Esempio di Output
    -   Il nome della tua band potrebbe essere: Roma Max

### Tabellina di un numero

Scrivi un programma che chieda un numero all'utente e stampi la sua tabellina fino a 10.

### Contare il numero di caratteri in una stringa

Scrivi un programma che chieda all'utente di inserire una stringa e poi conti e mostri il numero di caratteri in essa.

### Contare vocali in una stringa

Scrivi un programma che chieda una stringa e conti il numero di vocali presenti.

### Trova il massimo in una lista

Scrivi un programma che chieda all'utente una lista di numeri e trovi il massimo.

### Invertire una stringa

Scrivi un programma che chieda una stringa e la stampi al contrario.

### FizzBuzz

Scrivere un programma che stampi i primi 100 numeri ma al posto dei numeri divisibili per 3 stampi Fizz, al posto di quelli divisibili per 5 stampi Buzz e al posto di quelli divisibili sia per 3 che per 5 stampi FizzBuzz.

-   Esempio di output:

-   `1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, ...`

### Calcolo del fattoriale di un numero

Scrivi un programma che chieda all'utente di inserire un numero intero e calcoli il suo fattoriale.

### Generare la sequenza di Fibonacci

Scrivi un programma che chieda all'utente di inserire un numero n e generi i primi n numeri della sequenza di Fibonacci.

### Perimetri

Si scriva un programma in Python che in base alla scelta dellʼutente permetta di calcolare il perimetro di diverse figure geometriche (scegliete pure quelle che volete voi). Per la risoluzione dellʼesercizio abbiamo scelto:

-   Quadrato: `perimetro = lato * 4`
-   Cerchio: `circonferenza = 2 * pi_greco * r`
-   Rettangolo: `perimetro = base * 2 + altezza * 2`

### Calcolo della media, mediana e moda di una lista di numeri

Scrivi un programma che chieda all'utente di inserire una lista di numeri (separati da spazi) e calcoli la media, la mediana e la moda.

### Calcolo della media mobile

Scrivi una funzione che calcoli la media mobile di una lista di numeri.

La media mobile di un elemento è definita come la media degli ultimi n elementi della lista, inclusi l'elemento corrente.

-   Suggerimenti:

    -   usa slicing per ottenere gli ultimi n elementi
    -   usa la funzione `sum()` per calcolare la somma degli elementi e poi dividi per n.

-   Esempio di input:

    -   `numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]`
    -   `n = 3`

-   Esempio di output:
    -   `[1, 1.5, 2, 3, 4, 5, 6, 7, 8, 9]`

### Analisi delle parole

Scrivi un programma che analizzi una stringa di testo e restituisca un dizionario con il conteggio delle occorrenze di ciascuna parola.

Ignora la punteggiatura e considera le parole in modo case-insensitive.

-   Suggerimenti:

    -   usa il metodo `str.lower()` perconvertire il testo in minuscolo
    -   usa il modulo `re` per rimuovere la punteggiatura
    -   usa un dizionario per tenere traccia delle occorrenze delle parole

-   Esempio di input:
    -   `testo = "Ciao, ciao! Come stai? Stai bene?"`
-   Esempio di output:
    -   `{'ciao': 2, 'come': 1, 'stai': 2, 'bene': 1}`
