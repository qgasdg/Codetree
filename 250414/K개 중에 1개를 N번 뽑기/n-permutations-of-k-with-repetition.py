K, N = map(int, input().split())

# Please write your code here.
arr = [0] * N
def choose(num):
    if num == N:
        print(*arr, sep=' ')
        return
    for i in range(1, K + 1):
        arr[num] = i
        choose(num + 1)

choose(0)