class target:
    def __init__(self, minx, miny, maxy, maxx):
        self.minx = minx
        self.miny = miny
        self.maxx = maxx
        self.maxy = maxy


testcases = int(input())
for ugfk in range(testcases):
    n, x = map(int, input().split())
    targets = []
    for i in range(n):
        a, b, c = map(int, input().split())
        targets.append(target(x, a, b, c))
    cows = [list(map(int, input().split()))]
