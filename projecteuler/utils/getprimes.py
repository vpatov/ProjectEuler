import numpy as np
import os


def getprimes():
  with open(os.path.join(os.path.dirname(__file__),'primes.npy'),'rb') as f:
    nums = np.load(f)
  return nums


