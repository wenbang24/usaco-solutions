# ****x*x****x
from math import ceil

n = int(input())
cows = [int(i) for i in input()] + [0]
groups = []
count = 0
infected = 0
for i in cows:
    if i == 0:
        if count != 0:
            groups.append(count)
            count = 0
    else:
        count += 1
try:
    ming = min(groups)
    if (ming == groups[0] and cows[0] != 0) or (ming == groups[-1] and cows[-2] != 0): # -2 because we added a 0
        nights = ming - 1
    else:
        nights = ming//2 - (ming + 1) % 2
    #print(nights)

    max1 = 2*nights + 1
    for i in range(len(groups)):
        infected += ceil(groups[i]/max1)
    print(infected)
except:
    print(0)
