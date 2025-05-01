N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.
targ = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == 1:
            targ.append((i, j))

ans = 0
dx = ((-2, -1, 1, 2), (-1, 0, 0, +1), (-1, +1, -1, +1))
dy = ((0, 0, 0, 0), (0, -1, +1, 0), (-1, -1, +1, +1))

def boom(n):
    global ans
    if n == len(targ):
        cnt = 0
        for i in range(N):
            for j in range(N):
                # print(grid[i][j], end=' ')
                if grid[i][j] > 0:
                    cnt += 1
            # print()
        # print()
        ans = max(ans, cnt)
        return
    x, y = targ[n]
    for d in range(3):
        for l in range(4):
            xx, yy = x + dx[d][l], y + dy[d][l]
            if xx < 0 or yy < 0:
                continue
            if xx >= N or yy >= N:
                continue
            grid[xx][yy] += 1
        boom(n + 1)
        for l in range(4):
            xx, yy = x + dx[d][l], y + dy[d][l]
            if xx < 0 or yy < 0:
                continue
            if xx >= N or yy >= N:
                continue
            grid[xx][yy] -= 1
    return

boom(0)
print(ans)