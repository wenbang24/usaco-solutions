filein = open("dealin.txt")
fileout = open("dealout.txt", "w")
n, m = map(int,filein.readline().split())
votesnocount = list(map(int,filein.readline().split()))
votes = [0 for i in range(n+1)]
moneyspent = 0
for i in votesnocount:
    votes[-i] += 1
while votes.index(max(votes)) != n:
    moneyspent += 1
    votes[votes.index(max(votes))] -= 1
    votes[n] += 1
fileout.write(str(moneyspent))
