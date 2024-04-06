from functools import lru_cache

@lru_cache
def between(start, middle, end):
    if ((start[0] == middle[0] and middle[0] == end[0]) and (start[1] < middle[1] and middle[1] < end[1]) or (start[1] > middle[1] and middle[1] > end[1])) or ((start[1] == middle[1] and middle[1] == end[1]) and (start[0] < middle[0] and middle[0] < end[0]) or (start[0] > middle[0] and middle[0] > end[0])):
        return True
    return False

@lru_cache
def dist(start, end):
    return abs(start[0]-end[0]) + abs(start[1]-end[1])

n, p = map(int, input().split())
rawposts = [tuple(map(int, input().split())) for i in range(p)]
cows = [tuple(map(int, input().split())) for i in range(n)]
alltouches = {i:0 for i in rawposts}

# sort posts
posts = [rawposts[-1]]
rawposts.pop()
while len(rawposts) > 0:
    for i in rawposts:
        if i[0] == posts[-1][0] or i[1] == posts[-1][1]:
            posts.append(i)
            rawposts.remove(i)

for cow in cows:
    print("new cow:", cow)
    # find start(s)
    starts = []
    if cow[:2] in posts:
        print(cow[:2])
        starts.append(cow[:2])
    for i in range(1,p):
        if between(posts[i-1], cow[:2], posts[1]):
            print(posts[i-1], posts[i])
            starts.append(posts[i-1])
            starts.append(posts[i])
            break
    # find end(s)
    ends = []
    if cow[2:] in posts:
        print(cow[2:])
        ends.append(cow[2:])
    for i in range(1,p):
        if between(posts[i-1], cow[2:], posts[1]):
            print(posts[i-1], posts[i])
            ends.append(posts[i-1])
            ends.append(posts[i])
            break
    
    if cow[2:] == cow[:2]:
        if cow[:2] in posts:
            alltouches[cow[:2]] += 1
        continue

    if sorted(starts) == sorted(ends):
        continue

    # direction 1
    start = starts[0]
    end = ends[-1]
    touches1 = {i:0 for i in posts}
    dist1 = dist(cow[:2], start) + dist(cow[2:], end)
    startind = posts.index(start)
    endind = posts.index(end)
    if startind > endind:
        startind, endind = endind, startind
    for i in range(startind, endind):
        print(i, posts[i])
        dist1 += dist(posts[i], posts[(i+1) % p])
        touches1[posts[i]] += 1
    if cow[2:] == end:
        touches1[cow[2:]] += 1
    print(dist1, touches1)

    # direction 2
    start = starts[-1]
    end = ends[0]
    touches2 = {i:0 for i in posts}
    dist2 = dist(cow[:2], start) + dist(cow[2:], end)
    startind = posts.index(start)
    endind = posts.index(end)
    if startind < endind:
        startind, endind = endind, startind
    for i in range(startind, endind, -1):
        print(i, posts[i])
        dist2 += dist(posts[i], posts[(i+1) % p])
        touches2[posts[i]] += 1
    if cow[2:] == end:
        touches2[cow[2:]] += 1
    print(dist2, touches2)
