n = int(input())

cmd = []
k = []
v = []

for _ in range(n):
    line = input().split()
    cmd.append(line[0])
    if line[0] == "add":
        k.append(int(line[1]))
        v.append(int(line[2]))
    elif line[0] == "remove" or line[0] == "find":
        k.append(int(line[1]))
        v.append(0)
    else:
        k.append(0)
        v.append(0)

# Please write your code here.
from sortedcontainers import SortedDict

sd = SortedDict()
for i in range(n):
    c = cmd[i]
    if c == 'add':
        sd[k[i]] = v[i]
    elif c == 'remove':
        del sd[k[i]]
    elif c == 'find':
        if sd.get(k[i]):
            print(sd.get(k[i]))
        else:
            print("None")
    else:
        if sd.items():
            for _, value in sd.items():
                print(value, end=' ')
            print()
        else:
            print("None")

