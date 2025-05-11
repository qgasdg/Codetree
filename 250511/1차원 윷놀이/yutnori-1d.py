n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.

score = [1] * k
ans = 0

def check():
    global ans
    cnt = 0
    for i in range(k):
        if score[i] >= m:
            cnt += 1
    ans = max(ans, cnt)

def f(x):
    if x == n:
        check()
        return
    for i in range(k):
        if score[i] >= m:
            continue
        score[i] += nums[x]
        f(x + 1)
        score[i] -= nums[x]

f(0)
print(ans)