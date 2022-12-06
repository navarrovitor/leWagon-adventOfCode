s1 = ["B","V","W","T","Q","N","H","D"]
s2 = ["B","W","D"]
s3 = ["C","J","W","Q","S","T"]
s4 = ["P","T","Z","N","R","J","F"]
s5 = ["T","S","M","J","V","P","G"]
s6 = ["N","T","F","W","B"]
s7 = ["N","V","H","F","Q","D","L","B"]
s8 = ["R","F","P","H"]
s9 = ["H","P","N","L","B","M","S","Z"]

s1.reverse()
s2.reverse()
s3.reverse()
s4.reverse()
s5.reverse()
s6.reverse()
s7.reverse()
s8.reverse()
s9.reverse()

crates = [s1,s2,s3,s4,s5,s6,s7,s8,s9]

f = open("day5/crates.txt", "r")
f = f.read()

for instruction in f.split("\n"):
    code = instruction.replace("move ","").replace("from ","").replace("to ","").split()
    crates[int(code[2])-1] += crates[int(code[1])-1][-int(code[0]):]
    crates[int(code[1])-1] = crates[int(code[1])-1][:-int(code[0])]
print(crates)
for i in crates:
    print(i[-1],end="")