# a little jank but it works :)
t = int(input())
for i in range(t):
    n = int(input())
    cows = list(map(int, input().split()))
    ok = set([cows[i] for i in range(len(cows)-2) if cows[i+1] == cows[i] or cows[i+2]==cows[i]])
    if cows[-1] == cows[-2]:
        ok.add(cows[-2])
    if len(ok) > 0:
        print(*sorted(ok))
    else:
        print(-1)
