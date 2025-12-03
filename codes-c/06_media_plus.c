#include <stdio.h>

int main()
{
    int count;
    int number;
    int sum = 0;
    float mean;

    printf("Quanti sono i numeri? ");
    scanf("%d", &count);

    // int i = 0;
    // while (i < count)
    // {
    //     i++;
    //     printf("Inserisci il %d˚ numero: ", i);
    //     scanf("%d", &number);
    //     sum = sum + number;
    // }

    for (int i = 1; i <= count; i++)
    {
        printf("Inserisci il %d˚ numero: ", i);
        scanf("%d", &number);
        sum = sum + number;
    }

    mean = sum / (float)count;

    printf("La media è: %.2f\n", mean);
    printf("La media è: %g\n", mean);

    return 0;
}