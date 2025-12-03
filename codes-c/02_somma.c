#include <stdio.h>

int main() {
    int a;
    int b;
    int somma;

    printf("Inserisci il primo numero: ");
    scanf("%d", &a);

    printf("Inserisci il secondo numero: ");
    scanf("%d", &b);

    somma = a + b;

    printf("La somma è: %d", somma);

    return 0;
}