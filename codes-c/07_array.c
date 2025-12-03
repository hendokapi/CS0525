#include <stdio.h>

int main()
{
    float prezzi[] = {1.2, 5.3, 4.4, 6.5};

    for (int i = 0; i < 4; i++)
    {
        printf("- Elemento in posizione %d: %f\n", i, prezzi[i]);
    }

    return 0;
}