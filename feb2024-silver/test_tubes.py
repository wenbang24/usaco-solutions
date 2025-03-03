testcases = int(input())
ans = []
for fhis in range(testcases):
    size, parameter = map(int, input().split())
    tube1 = []
    tube2 = []

    new = input() + "e"
    cur = new[0]
    count = 0
    for i in new:
        if i != cur:
            tube1.append({"type":cur, "count":count})
            count = 1
            cur = i
        else:
            count += 1
    
    new = input() + "e"
    cur = new[0]
    count = 0
    for i in new:
        if i != cur:
            tube2.append({"type":cur, "count":count})
            count = 1
            cur = i
        else:
            count += 1
    
    count = 0
    moves = []
    beaker = {"type": 0, "count": 0}
    while len(tube1) > 1 or len(tube2) > 1 or beaker["count"] > 0:
        if tube1[-1]["type"] == tube2[-1]["type"] and tube1[-1]["count"] < tube2[-1]["count"] and len(tube2) > 0:
            moves.append("2 1")
            tube1[-1]["count"] += tube2.pop()["count"]
        elif tube1[-1]["type"] == tube2[-1]["type"] and tube1[-1]["count"] >= tube2[-1]["count"] and len(tube1) > 0:
            moves.append("1 2")
            tube2[-1]["count"] += tube1.pop()["count"]

        elif beaker["count"] != 0:
            if tube1[-1]["type"] == beaker["type"]:
                moves.append("3 1")
                tube1[-1]["count"] += beaker["count"]
                beaker["count"] = 0
            else:
                moves.append("3 2")
                tube2[-1]["count"] += beaker["count"]
                beaker["count"] = 0
        elif tube1[-1]["count"] >= tube2[-1]["count"]:
            moves.append("1 3") # maybe make it 2 3
            beaker["type"] = tube1[-1]["type"]
            beaker["count"] += tube1.pop()["count"]
        else:
            moves.append("2 3") # maybe make it 1 3
            beaker["type"] = tube2[-1]["type"]
            beaker["count"] += tube2.pop()["count"]
        print(moves, tube1, tube2, beaker, sep="\n")
"""     ans.append(len(moves))
    if parameter != 1:
        ans.extend(moves)
print(*ans, sep="\n") """
