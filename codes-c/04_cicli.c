#include <stdio.h>

int main()
{
    int number;

    printf("Inserisci il numero: ");
    scanf("%d", &number);

    // while (number > 0)
    // {
    //     printf("%d - ciao come stai\n", number);
    //     number--;
    // }

    int i = 1;
    while (i <= number)
    {
        printf("%d - ciao come stai\n", i);
        i++;
    }

    return 0;
}