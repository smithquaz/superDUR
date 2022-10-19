#include <stdio.h>
#include <stdlib.h>

int main(){

    // int height;

    // recursively get the height to ensure that height is between 1 and 8 inclusive
    // get user-input on the height of the pyramid
    do {
        printf("Enter Height: ");
        scanf("%d", &height);
    }

    while(height < 1 || height > 8);

    // settles the vertical height of the pyramid
    for (int i = 0 ; i < height ; i++){

        // prints left side space
        for (int j = 0 ; j < height - 1 - i ; j++){
            printf(" ");
        }


        // prints left pyramid hash
        for (int m = 0 ; m < i + 1; m++){
            printf("#");
        }


        // prints middle space
        for (int n = 0 ; n < 2 ; n++){
            printf(" ");
        }


        // prints right pyramid hash
        for (int w = 0 ; w < i + 1; w++){
            printf("#");
        }

        // new line for next pyramid level
        printf("\n");

    }

    return 0;
}