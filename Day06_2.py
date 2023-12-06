with open("Day06.txt", "r") as f:
    contents = f.read()
    
lines = contents.split(sep="\n")
# print(lines)

line1 = lines[0].split(sep=" ")
del(line1[0])

time = ""
for l in line1:
    if l != "":
        time = time + l
time = int(time)

line2 = lines[1].split(sep=" ")
del(line2[0])

dist = ""
for l in line2:
    if l != "":
        dist = dist + l
dist = int(dist)        
        
# print(time)
# print(dist)

sol = 0

for j in range(time):
    if j * (time - j) > dist:
        sol += 1

print(sol)