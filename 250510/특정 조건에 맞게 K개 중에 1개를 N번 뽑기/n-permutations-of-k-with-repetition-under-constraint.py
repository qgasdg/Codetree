K, N = map(int, input().split())

# Please write your code here.
st = []
def f(n): # 0부터 시작
    if n == N:
        for i in range(N):
            print(st[i], end=' ')
        print()
        return
    if n < 2:
        for i in range(1, K + 1):
            st.append(i)
            f(n + 1)
            st.pop()
    else:
        for i in range(1, K + 1):
            if st[-1] == i and st[-2] == i:
                continue
            st.append(i)
            f(n + 1)
            st.pop()

f(0)
