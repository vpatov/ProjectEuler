#include <stdio.h>
/*
Leonhard Euler was born on 15 April 1707.

Consider the sequence 1504170715041707n mod 4503599627370517.
An element of this sequence is defined to be an Eulercoin if it 
is strictly smaller than all previously found Eulercoins.

For example, the first term is 1504170715041707 which is the first Eulercoin. 
The second term is 3008341430083414, which is greater than 1504170715041707,
so is not an Eulercoin.
However, the third term is 8912517754604 which is small enough to be a new Eulercoin.

The sum of the first 2 Eulercoins is therefore 1513083232796311.

Find the sum of all Eulercoins.
*/

int main(){
    unsigned long sum_eulercoins = 0;
    unsigned long modterm = 4503599627370517;
    unsigned long coeff =   1504170715041707;
    unsigned long smallest_eulercoin = modterm;

    // for (int n = 1; n < 10000; n++){
    unsigned long n = 1;
    while (1){
        unsigned long current_term = (coeff * n) % modterm;
        if (current_term < smallest_eulercoin){
            sum_eulercoins += current_term;
            smallest_eulercoin = current_term;
            printf("current_term: %lu\n", current_term);
            printf("%lu: %lu\n",n, sum_eulercoins);
        }
        n++;
    }

}