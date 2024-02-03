filein = open("shopin.txt")
fileout = open("shopout.txt", "w")
n, m = map(int,filein.readline().split())
houses = list(map(int,filein.readline().split()))
shops = list(map(int,filein.readline().split()))
prices = list(map(int,filein.readline().split()))
for i in houses:
    minbad = 9999999999
    for j in range(len(shops)):
        bad = abs(i-shops[j]) + prices[j]
        if bad < minbad:
            minbad = bad
    fileout.write(str(minbad) + " ")
