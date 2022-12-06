f = open("day6/buffer.txt", "r")
f = f.read()

for i in range(len(f)):
    if len(set(f[i:i+4])) == 4:
        print(f[i:i+4], i+4)
        break