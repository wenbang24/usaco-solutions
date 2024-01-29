n = int(input())
grass = list(map(int, input().split()))
count = 0
for i in range(n):
    if grass[i] != 0:
        change = [max(e, 0) for e in range(-i+1,n-i+1)]
        power = n - i
        increase = False
        if grass[i] < 0:
            increase = True
        num = abs(grass[i])
        count += num
        if increase:
            for j in range(n-power, n):
                grass[j] += change[j] * num
        else:
            for j in range(n-power, n):
                grass[j] -= change[j] * num
print(count)
