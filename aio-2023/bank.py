import math
filein = open("bankin.txt")
fileout = open("bankout.txt", "w")
n = int(filein.readline())
fileout.write(str(((n//2)+1)*(math.ceil(n/2))))
