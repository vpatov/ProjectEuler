import os

def getinput(problem_num):
  input_dir = os.path.join(os.path.dirname(__file__),'..','input')
  return open(os.path.join(input_dir,str(problem_num) + '.txt'),'r')

def getmisc(filename):
  input_dir = os.path.join(os.path.dirname(__file__),'..','input')
  return open(os.path.join(input_dir,filename),'r')
