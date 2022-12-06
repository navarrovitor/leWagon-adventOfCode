f = open("day4/pairs.txt", "r")
f = f.read()

sum = 0
for pair in f.split():
    x = list(range(int(pair.split(',')[0].split('-')[0]),int(pair.split(',')[0].split('-')[1])+1))
    y = list(range(int(pair.split(',')[1].split('-')[0]),int(pair.split(',')[1].split('-')[1])+1))
    if all(item in x for item in y) or all(item in y for item in x):
        sum += 1
print(sum)