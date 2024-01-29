# even without all the memorization stuff (the variable done and anything to do with it)
# i still got the exact same result
done = set()
n, s = map(int, input().split())
line = [list(map(int, input().split())) for i in range(n)]
line.insert(0, [-1, 0])
power = 1
increasing = True
broken = 0
newbreak = False
while s <= n and s > 0:
    if newbreak == True and (power, s) in done:
        break
    done.add((power, s))
    if line[s][0] == 1 and power >= line[s][1]:
        broken += 1
        line[s][0] = -1
        newbreak = True
        done = set()
    elif line[s][0] == 0:
        newbreak = False
        power += line[s][1]
        if increasing:
            increasing = False
        else:
            increasing = True
    else:
        newbreak = False
    if increasing:
        s += power
    else:
        s -= power
print(broken)
