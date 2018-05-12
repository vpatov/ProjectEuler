#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <assert.h>



void sieve_atkin(unsigned long long *primes, unsigned short *sieve, size_t limit){
  int i, x, y, n, p, primes_index, sqrt_limit;
  size_t total_length;
  primes_index = 0;

  primes[primes_index++] = 2;
  primes[primes_index++] = 3;
  sqrt_limit = (int)(sqrt(limit)) + 1;
  
  for (x = 1; x < sqrt_limit; x++){
    for (y = 1; y < sqrt_limit; y++){
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
  for (x = 5; x < sqrt_limit - 1; x++){
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

  /*
The first 6 bytes are a magic string: exactly “x93NUMPY”.

The next 1 byte is an unsigned byte: the major version number of the file format, e.g. x01.

The next 1 byte is an unsigned byte: the minor version number of the file format, e.g. x00. Note: the version of the file format is not tied to the version of the numpy package.

The next 2 bytes form a little-endian unsigned short int: the length of the header data HEADER_LEN.

The next HEADER_LEN bytes form the header data describing the array’s format. It is an ASCII string which contains a Python literal expression of a dictionary. It is terminated by a newline (‘n’) and padded with spaces (‘x20’) to make the total length of the magic string + 4 + HEADER_LEN be evenly divisible by 64 for alignment purposes.

The dictionary contains three keys:

“descr” : dtype.descr
An object that can be passed as an argument to the numpy.dtype() constructor to create the array’s dtype.
“fortran_order” : bool
Whether the array data is Fortran-contiguous or not. Since Fortran-contiguous arrays are a common form of non-C-contiguity, we allow them to be written directly to disk for efficiency.
“shape” : tuple of int
The shape of the array.
For repeatability and readability, this dictionary is formatted using pprint.pformat() so the keys are in alphabetic order.

Following the header comes the array data. If the dtype contains Python objects (i.e. dtype.hasobject is True), then the data is a Python pickle of the array. Otherwise the data is the contiguous (either C- or Fortran-, depending on fortran_order) bytes of the array. Consumers can figure out the number of bytes by multiplying the number of elements given by the shape (noting that shape=() means there is 1 element) by dtype.itemsize.
  */
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
  int i, limit;
  unsigned short *sieve;
  unsigned long long *primes;
  
  if (argc < 2){
    printf("Must provide limit for prime calculations. Usage: sieve LIMIT\n");
    return 1;
  }
  
  limit = atoi(argv[1]);

  if (limit < 5){
    printf("limit is too small.\n");
  }
  
  primes =  calloc(limit*1, sizeof(unsigned long long));
  sieve =   calloc(limit+1, sizeof(unsigned short));  
  sieve_atkin(primes, sieve, limit);

  /*
  for (i = 0; i < 50; i++){
    printf("%llu\n", primes[i]);
  }
  */
 
}
