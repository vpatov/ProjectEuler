#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <assert.h>



void sieve_atkin(unsigned long long *primes, unsigned short *sieve, size_t limit){
  long i, x, y, n, p, primes_index, sqrt_limit;
  size_t total_length;
  primes_index = 0;

  primes[primes_index++] = 2;
  primes[primes_index++] = 3;
  sqrt_limit = (long)(sqrt(limit));
  
  for (x = 1; x < sqrt_limit + 1; x++){
    for (y = 1; y < sqrt_limit + 1; y++){
      n = (4*x*x) + (y*y);
      if (n <= limit && (n % 12 == 1 || n % 12 == 5)){
        sieve[n] = !sieve[n];
      }

      n = (3*x*x) + (y*y);
      if (n <= limit && n % 12 == 7){
        sieve[n] = !sieve[n];
      }

      n = (3*x*x) - (y*y);
      if (x > y && n <= limit && n % 12 == 11){
        sieve[n] = !sieve[n]; 
      }

    }
  }
  for (x = 5; x < sqrt_limit; x++){
    if (sieve[x]){
      for (y = x*x; y < limit+1; y += x*x){
        sieve[y] = 0;
      }
    }
  }
 
  for (p = 5; p < limit; p++){
    if (sieve[p]){
      primes[primes_index++] = p;
    }
  }
  total_length = primes_index;

  printf("Primes calculation successful.\n");
  
  char filename[256];
  char dictionary[256];
  FILE *write_ptr;
  unsigned short int header_len;
  unsigned short int base_header_len;
  size_t padding_len;
  //assert(sizeof(header_len) == 2);

  sprintf(filename, "primes.npy");
  write_ptr = fopen(filename,"wb");    
 
  //create dictionary string
  sprintf(dictionary,"{'descr': '<i8', 'fortran_order': False, 'shape': (%zu,), }",total_length); 

    

  //magic string and version number
  char numpy_magic[] = "\x93NUMPY";
  char version_num[] = "\x01\x00";

  //calculate padding - there is a more elegant way to do this using modulus
  base_header_len = strlen(dictionary);
  padding_len = 0;
  while ((base_header_len + 4 + 6 + padding_len) % 64 != 0){
    padding_len++;
  }


  header_len = base_header_len + padding_len;


  // Write numpy magic
  fwrite(numpy_magic,sizeof(numpy_magic)-1,1,write_ptr);
  // Write version number
  fwrite(version_num,sizeof(version_num)-1,1,write_ptr);
  // Write HEADER_LEN

  fwrite((char*)(&header_len),1,1,write_ptr);
  fwrite((char*)(&header_len) + 1,1,1,write_ptr);
  // Write the dictionary
  fwrite(dictionary,strlen(dictionary),1,write_ptr);

 
  //write space padding
  for (i = 0; i < padding_len-1; i++){
    fwrite(" ",1,1,write_ptr);
  } 
  //terminate header with newline
  fwrite("\n",1,1,write_ptr);


  //write the actual data
  for(i = 0; i < total_length; i++){
    fwrite(&primes[i],sizeof(primes[i]),1,write_ptr);
  }

  printf("Serialized primes to %s\n", filename);
}



int main(int argc, char **argv){
  int i;
  long limit, approx_num_primes;
  unsigned short *sieve;
  unsigned long long *primes;
  
  if (argc < 2){
    printf("Must provide limit for prime calculations. Usage: sieve LIMIT\n");
    return 1;
  }
  
  limit = atoll(argv[1]);

  if (limit < 5){
    printf("limit is too small.\n");
  }
 
  approx_num_primes = (unsigned long)((limit / log(limit)) * (1 + (1.2762 / log(limit))));
  
  primes =  calloc(approx_num_primes, sizeof(unsigned long));
  sieve =   calloc(limit+1, sizeof(unsigned short));  
  sieve_atkin(primes, sieve, limit);

  /*
  for (i = 0; i < 50; i++){
    printf("%llu\n", primes[i]);
  }
  */
 
}
