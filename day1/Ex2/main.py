f = open("day1\elves.txt", "r")
f = f.read()

elves = []
for elf in f.split("\n\n"):
    x = []
    for calory in elf.split("\n"):
        x.append(int(calory))
    elves.append(x)

print(elves)

elvesCalories = []

for i in elves:
    elvesCalories.append(sum(i))

sum = 0
for i in range(3):
    print(max(elvesCalories))
    sum += max(elvesCalories)
    elvesCalories.remove(max(elvesCalories))
print(sum)