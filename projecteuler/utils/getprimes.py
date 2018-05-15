import numpy as np
import os
import pickle

def getprimes():
  with open(os.path.join(os.path.dirname(__file__),'largeprimes.npy'),'rb') as f:
    nums = np.load(f)
  return nums


def getprimeset():
  with open(os.path.join(os.path.dirname(__file__),'largeprimeset.pickle'),'rb') as f:
    nums = pickle.load(f)
  return nums

def makeprimeset():
  primes = getprimes()[:100000000]
  print("Loaded primes")
  primeset = set(primes)
  print("Created primeset")
  del primes
  print("Freed primelist from memory")
  with open(os.path.join(os.path.dirname(__file__),'largeprimeset.pickle'),'wb') as f:
    pickle.dump(primeset,f, protocol= pickle.HIGHEST_PROTOCOL)
  print("Serialized primeset")
