#include <stdbool.h>
#include <pthread.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <ctype.h>


struct thread_info {    
    pthread_t thread_id;   
    long      start;
    long      end;
};

bool reversible(long input){
    long dec, digit, sum, reversed = 0;
    dec = input;
    if (input % 10 == 0)
        return false;
    while (dec > 0) { 
        reversed = reversed * 10 + dec % 10; 
        dec /= 10; 
    } 
    sum = input + reversed;
    while (sum > 0){
        digit = sum % 10;
        if (digit % 2 == 0){
            return false;
        }
        sum /= 10;
    }
    return true;
}

static void *
thread_fn(void *arg) {
    struct thread_info *tinfo = arg;
    unsigned long count = 0;

    for (unsigned long cur = tinfo->start; cur <= tinfo->end; cur++){
        if (reversible(cur))
            count++;
    }

    long *ret = malloc(sizeof(unsigned long));
    *ret = count;
    return ret;
}

// In any real application you'd want error-handling, but I didn't bother here.
int
main(int argc, char *argv[])
{
    int s, tnum, opt, num_threads;
    struct thread_info *tinfo;
    pthread_attr_t attr;
    void *res;

    num_threads = 24;
    long input_size = 1000000000;
    long chunksize = input_size / num_threads;

    pthread_attr_init(&attr);
    tinfo = calloc(num_threads, sizeof(struct thread_info));
    for (tnum = 0; tnum < num_threads; tnum++) {
        tinfo[tnum].start = (tnum * chunksize) + 1;
        tinfo[tnum].end = (tnum + 1)* chunksize;
        pthread_create(&tinfo[tnum].thread_id, &attr, &thread_fn, &tinfo[tnum]);
    }

    long agg = 0;
    for (tnum = 0; tnum < num_threads; tnum++) {
        pthread_join(tinfo[tnum].thread_id, &res);
        agg += *((long *) res);
    }
    printf("%ld\n\n", agg);
}

