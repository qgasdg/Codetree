n, m = map(int, input().split())
arr = list(map(int, input().split()))
nums = list(map(int, input().split()))

# Please write your code here.
d = {}
for e in arr:
    if d.get(e):
        d[e] += 1
    else:
        d[e] = 1

for e in nums:
    if d.get(e):
        print(d[e], end=' ')
    else:
        print(0, end=' ')