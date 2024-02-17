from sys import exit

testcases = int(input())
for refergih in range(testcases):
    marbles, turns, posmoves = map(int, input().split())
    moves = [list(map(int, input().split())) for i in range(turns)]
    possible = []
    for i in range(2**turns):
        n = bin(i)[2:]
        length = len(n)
        possible.append("0"*(turns-length)+n)
    print(possible)
    for path in possible:
        for move in range(turns):
            try:
                maxodd = max(x for x in moves[move] if x % 2)
            except: # no odd numbers
                if path[move] == 0:
                    marbles += min(move[moves])
                else:
                    marbles -= max(move[moves])
                continue
            try:
                maxeven = max(x for x in moves[move] if x % 2 == 1)
            except: # no even numbers
                if path[move] == 1:
                    marbles += min(move[moves])
                else:
                    marbles -= max(move[moves])
                continue

            # a mix of odd and even
            if path[move] == 0: # even
                marbles -= maxodd
            else:
                marbles -= maxeven
