filein = open("telein.txt")
fileout = open("teleout.txt", "w")
count = 0
maxcount = 0
mincount = 0
n = int(filein.readline())
moves = [i for i in filein.readline()]
for i in moves:
    if i == "T":
        count = 0
    elif i == "L":
        count -= 1
        if count < 0 and count < mincount:
            mincount = count
    elif i == "R":
        count += 1
        if count > 0 and count > maxcount:
            maxcount = count
filein.close()
fileout.write(str(abs(mincount)+maxcount+1))
fileout.close()
