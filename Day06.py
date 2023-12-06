with open("Day06.txt", "r") as f:
    contents = f.read()
    
lines = contents.split(sep="\n")
# print(lines)

line1 = lines[0].split(sep=" ")
del(line1[0])

time= []
for l in line1:
    if l != "":
        time.append(int(l))

line2 = lines[1].split(sep=" ")
del(line2[0])

dist = []
for l in line2:
    if l != "":
        dist.append(int(l))
print(time)
print(dist)

sol = [[]]
msol = []
for i in range(len(time)):
    sol.append([])
    for j in range(time[i]):
        if j * (time[i] - j) > dist[i]:
            sol[i].append(1)
    msol.append(sum(sol[i]))

ssol = 1
for i in range(len(msol)):
    ssol *= msol[i]

print(ssol)