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
    unsigned long long sum_eulercoins = 0;
    unsigned long long modterm = 4503599627370517;
    unsigned long long coeff =   1504170715041707;
    // unsigned long long modterm = 5119;
    // unsigned long long coeff =   1901;
    unsigned long long smallest_eulercoin = 99999999999999999;

    // for (int n = 1; n < 10000; n++){
    unsigned long long n = 1;
    while (n <= modterm){
        unsigned long long current_term = (coeff * n) % modterm;
        if (current_term == 0){
            // printf("reached 0. n: %llu\n", n);
            break;
        }
        if (current_term < smallest_eulercoin){
            sum_eulercoins += current_term;
            printf("diff %llu\n", smallest_eulercoin - current_term);
            smallest_eulercoin = current_term;
            printf("current_term: %-8llu n: %llu\n", current_term, n);
            // printf("n=%llu: sum=%llu\n",n, sum_eulercoins);
        }
        n++;
    }

}