n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
adj = [[0] * n for _ in range(16)]

for edge in edges:
    adj[edge[1] - 1][edge[0] - 1] = 1

# for i in range(15):
#     print(*adj[i])

def start():
    p = [i for i in range(n)]
    for i in range(4):
        tmp = i
        for j in range(16):
            if adj[j][tmp]:
                tmp += 1
            elif tmp > 0 and adj[j][tmp - 1]:
                tmp -= 1
        p[i] = tmp
    return p

# print(start())
prime = start()
ans = m

def f(k, num):
    if k == m:
        if prime == start():
            global ans
            ans = min(ans, num)
        return
    a, b = edges[k]
    f(k + 1, num)
    adj[b - 1][a - 1] = 0
    f(k + 1, num - 1)
    adj[b - 1][a - 1] = 1
    return

f(0, m)
print(ans)
