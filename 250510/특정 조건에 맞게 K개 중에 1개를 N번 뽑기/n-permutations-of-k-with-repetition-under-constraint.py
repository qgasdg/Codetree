K, N = map(int, input().split())

# Please write your code here.
permutations = []

def print_per():
    for i in range(N):
        print(permutations[i], end=' ')
    print()

def find_permutations(n):
    if n == N:
        print_per()
        return
    for i in range(1, K + 1):
        if n >= 2 and permutations[-1] == i and permutations[-2] == i:
            continue
        permutations.append(i)
        find_permutations(n + 1)
        permutations.pop()

find_permutations(0)