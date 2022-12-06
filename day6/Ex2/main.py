f = open("day6/buffer.txt", "r")
f = f.read()

for i in range(len(f)):
    if len(set(f[i:i+14])) == 14:
        print(f[i:i+14], i+14)
        break