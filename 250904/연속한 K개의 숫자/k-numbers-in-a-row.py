N, K, B = map(int, input().split())
missing = [int(input()) for _ in range(B)]

# Please write your code here.

m = set(missing)
# idx = 0
prefix = 0

for i in range(1, K + 1):
    if i in m:
        # idx += 1
        prefix += 1

ans = prefix

for i in range(K + 1, N + 1):
    if i in m:
        # idx += 1
        prefix += 1
    if i - K in m:
        prefix -= 1
    ans = min(ans, prefix)

print(ans)