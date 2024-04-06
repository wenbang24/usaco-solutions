def substrings(s, lensub):
    global n
    for i in range(n - lensub + 1):
        yield s[i:i+lensub]

def lexmin(s, lensub):
    minStr = s[:lensub]
    index = 0
    i = 0
    for i in range(1, len(s) - lensub + 1):
        if s[i:i+lensub] < minStr:
            minStr = s[i:i+lensub]
            index = i
    return index


n = int(input())
s = input()
numwinning = [0] * n
winners = []
for len_mer in range(1,n+1):
    #print(list(substrings(s, len_mer)))
    for lensubstr in range(1,len_mer+1):
        #print(lensubstr)
        wins = set()
        for shift, substr in enumerate(substrings(s, len_mer)):
            ind = lexmin(substr, lensubstr)
            #print(ind+shift, s[ind+shift:ind+shift+lensubstr])
            wins.add(ind+shift)
        winners.append(wins)
    #print()
#print(winners)
for i in winners:
    numwinning[len(i)-1] += 1
print(*numwinning, sep="\n")
