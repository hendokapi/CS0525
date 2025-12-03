#include <stdio.h>

int main() {
    int number;
    int resto;

    printf("Inserisci il numero: ");
    scanf("%d", &number);

    resto = number % 2;

    if (resto == 0)
    {
        printf("%d è pari", number);
    }
    else 
    {
        printf("%d è dispari", number);
    }
    
    return 0;
}