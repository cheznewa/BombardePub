import sys
from random import choice
from os import listdir
pubperline = int(sys.argv[1])
n=0
listpubs = listdir("pubs")
for e in sys.stdin:
 if (n % pubperline) == 0:
  sys.stdout.write(e)
  pub = choice(listpubs)
  sys.stdout.write("<img src=\"pubs/%s\">" %(pub))
 else:
  sys.stdout.write(e)
 n = n+1