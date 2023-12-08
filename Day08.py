import re
with open("Day08.txt", "r") as f:
    contents = f.read()
    
lines = contents.split(sep="\n")

instructions = lines[0]

pattern = r"([A-Z]{3})"

maps = []
i = 2
while i < len(lines):
    matches = re.findall(pattern, lines[i])
    maps.append(matches)
    i += 1
    
# print(maps)
start = []
for i in range(len(maps)):
    start.append(maps[i][0])
    del(maps[i][0])

# print(start)

goto = "AAA"
i = 0
while goto != "ZZZ":
    if instructions[i % len(instructions)] == "L":
        goto = maps[start.index(goto)][0]
        i += 1
    else:
        goto = maps[start.index(goto)][1]
        i += 1
    print(goto)

print(i)