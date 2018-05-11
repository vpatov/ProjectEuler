import os
programs = [
  os.path.basename(os.path.splitext(fname)[0]) 
  for fname in os.listdir(os.path.join('..','projecteuler','complete'))
]

for p in programs:
  try:
    exec('import projecteuler.complete.%s' % p)
  except Exception as e:
    print(e)
    print("%s - Failure" % p)
    
