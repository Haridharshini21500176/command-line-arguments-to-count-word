import sys
with open(sys.argv[1]) as fp:
  para=fp.read()
  word=para.split()
  print("total number of words:",len(word))
