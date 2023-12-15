# *xxxxxxxxxtttt
n, m = map(int, input().split())
cows = list(map(int, input().split()))
canes = list(map(int, input().split()))
for caneheight in canes:
    cane = [0, caneheight]
    #print(cane)
    for cow in range(len(cows)):
        #print(cows, cane)
        if cows[cow] > cane[1]:
            cows[cow] += cane[1]
            cane = [0,0]
        elif cows[cow] - cane[0] > 0:
            cows[cow], cane[0] = cows[cow] + cows[cow] - cane[0], cows[cow]
        #print(cows, cane)
        
print(*cows, sep = "\n")
