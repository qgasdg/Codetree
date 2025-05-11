n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]
move_dir = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.
d = ((0, 0), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def f(x, y, prev):
    if num[x][y] <= prev:
        return float('-inf')
    xx, yy = x + d[move_dir[x][y]][0], y + d[move_dir[x][y]][1]
    ret = 1
    while 0 <= xx < n and 0 <= yy < n:
        ret = max(ret, f(xx, yy, num[x][y]) + 1)
        xx, yy = xx + d[move_dir[x][y]][0], yy + d[move_dir[x][y]][1]
    return ret

print(f(r - 1, c - 1, float('-inf')) - 1)
