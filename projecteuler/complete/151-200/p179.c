#include <math.h>
#include <stdio.h>
/*
Find the number of integers 1 < n < 10^7, 
for which n and n + 1 have the same number of positive divisors. 

For example, 14 has the positive divisors 1, 2, 7, 14 while 15 has 1, 3, 5, 15.
*/

int number_divisors(int num){
    int count = 2;
    int i = 2;
    double limit = sqrt(num);
    for (; i < limit; i++){
        if (num % i == 0){
            count+=2;
        }
    }
    // printf("limit: %f longlimit: %lu\n", limit, (long)limit);
    if (i == limit && num % i == 0){
        count++;
    }
    return count;
}

int main() {
    long n = 4;
    long count = 1;
    int prevDivisors = 2;
    while (n < 10000000){
    // while (n < 100){
        long numDivisors = number_divisors(n);
        // printf("numDivisors(%lu)=%lu\n",n, numDivisors);

        if (numDivisors == prevDivisors){
            // printf("numDivisors=%lu, n=%lu and n+1=%lu\n", numDivisors, n-1, n);
            count++;
        }
        prevDivisors = numDivisors;
        n++;    
    }

    printf("%lu\n\n",count);
}
