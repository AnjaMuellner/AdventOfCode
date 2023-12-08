import re
import math
import time
start_time = time.time()
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
starts = []
for i in range(len(maps)):
    starts.append(maps[i][0])
    del(maps[i][0])

# print(start)

goto = []
end = []
for start in starts:
    if start[2] == "A":
        goto.append(start)
    if start[2] == "Z":
        end.append(start)
    
print(goto)

def kgV(array):
    result = array[0]
    for zahl in array[1:]:
        result = abs(result * zahl) // math.gcd(result, zahl)
    return result

counter_gotos = []
sorted_ends = []
for gos in goto:
    i = 0
    while gos not in end:
        if instructions[i % len(instructions)] == "L":
            gos = maps[starts.index(gos)][0]
            i += 1
        else:
            gos = maps[starts.index(gos)][1]
            i += 1
    counter_gotos.append(i)
    sorted_ends.append(gos)

print(sorted_ends)
print(counter_gotos)
print(kgV(counter_gotos))
print("Process finished --- %s seconds ---" % (time.time() - start_time))