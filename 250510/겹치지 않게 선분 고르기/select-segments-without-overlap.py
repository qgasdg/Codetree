n = int(input())
x1, x2 = [], []

for _ in range(n):
    a, b = map(int, input().split())
    x1.append(a)
    x2.append(b)

# Please write your code here.
def check(l1, r1, l2, r2):
    if r1 < l2:
        return True
    if r2 < l1:
        return True
    return False

ans = 0
cnt = 0
line = []
def f(idx):
    global ans, cnt
    if idx == n:
        ans = max(ans, cnt)
        return
    c = True
    for e in line:
        c = check(e[0], e[1], x1[idx], x2[idx]) and c
    f(idx + 1)
    if c:
        cnt += 1
        line.append((x1[idx], x2[idx]))
        f(idx + 1)
        cnt -= 1
        line.pop()

f(0)
print(ans)