#include <stdio.h>

int main() {
    int a;
    int b;
    float media;

    printf("Inserisci il primo numero: ");
    scanf("%d", &a);

    printf("Inserisci il secondo numero: ");
    scanf("%d", &b);

    int sotto = 2;

    media = (a + b) / (float) sotto;

    printf("La media è: %.2f\n", media);
    printf("La media è: %g\n", media);
    
    return 0;
}