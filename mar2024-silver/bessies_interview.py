import sys
from collections import deque
from itertools import permutations
sys.setrecursionlimit(10**6)

def replace_zeros(original_list, replacement_list):
    replacement_iter = iter(replacement_list)
    return [x if x != 0 else next(replacement_iter) for x in original_list]

def popmult(cows, num):
    for i in range(num):
        yield cows.popleft()

def search(count, cows, farmers, start=False):
    global caninterview, possible
    #print(count, cows, farmers, start)
    if farmers.count(0) != 0 and not start:
        return
    #print(count, cows, farmers)
    count += 1
    for cow in range(k):
        farmers[cow] -= 1
    zeros = farmers.count(0)
    if len(cows) == 0:
        #print(count + min(farmers), farmers.index(min(farmers)))
        possible.add(count + min(farmers))
        caninterview[farmers.index(min(farmers))] = '1'
        return
    if zeros > 1:
        interview = popmult(cows, zeros)
        for perm in permutations(interview, zeros):
            search(count, cows, replace_zeros(farmers, perm))
    elif zeros == 1:
        farmers[farmers.index(0)] = cows.popleft()
    search(count, cows, farmers)

n, k = map(int, input().split())
cows = deque(map(int, input().split()))
farmers = [0] * k
caninterview = ['0'] * k
possible = set()
count = 0
for i in range(min(n, k)):
    farmers[i] = cows.popleft()
#print(cows, farmers)
search(count, cows, farmers, start=True)
print(min(possible))
print(''.join(caninterview))
""" while True:
    print(count, cows, farmers)
    count += 1
    for cow in range(k):
        farmers[cow] -= 1
    if len(cows) == 0 and farmers.count(0) >= 1:
        print(count)
        break
    if farmers.count(0) > 1:
        for i in range(k):
            if farmers[i] == 0:
                farmers[i] = cows.popleft()
    elif farmers.count(0) == 1:
        farmers[farmers.index(0)] = cows.popleft() """
