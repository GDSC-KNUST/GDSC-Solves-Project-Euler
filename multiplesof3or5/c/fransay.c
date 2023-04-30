// Author: Fransay
// Date: 29/04/23
// Description : Project Euler ( Multiples of 3 or 5)
#include <stdio.h>
#define LIMIT 1000
int SUM;

int main(){
    for (int i=0; i < LIMIT; i++){
        if (multipleOfThree(i) || multipleOfFive(i)){
            SUM = SUM + i;
        }
        // printf("%d\n", i);
    }
    printf("%d", SUM);

}
// checks if a number is a multiple of three or not
int multipleOfThree(int number){
    if (number % 3 == 0){
        return 1;
    }
    return 0;
}

// checks if a number is a multiple of five or not
int multipleOfFive(int number){
    if (number % 5 == 0){
        return 1;
    }
    return 0;
}