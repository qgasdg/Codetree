n = int(input())
commands = []
for _ in range(n):
    line = input().split()
    cmd = line[0]
    k = int(line[1])
    if cmd == "add":
        v = int(line[2])
        commands.append((cmd, k, v))
    else:
        commands.append((cmd, k))

# Please write your code here.
d = {}
for i in range(n):
    cmd = commands[i][0]
    if cmd == 'add':
        d[commands[i][1]] = commands[i][2]
    if cmd == 'remove':
        del d[commands[i][1]]
    if cmd == 'find':
        if d.get(commands[i][1]):
            print(d.get(commands[i][1]))
        else:
            print('None')
        
