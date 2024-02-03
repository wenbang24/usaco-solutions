from collections import Counter
filein = open("rafflein.txt")
fileout = open("raffleout.txt", "w")
eee = filein.readline()
subs = list(map(int,filein.readline().split()))
subs = [e for e, v in Counter(subs).items() if v == 1]
if len(subs) == 0:
    fileout.write("-1")
else:
    fileout.write(str(min(subs)))
