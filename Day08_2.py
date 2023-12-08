import re
import math
import time
start_time = time.time()
with open("Day08_Jensi.txt", "r") as f:
    contents = f.read()
    
lines = contents.split(sep="\n")

instructions = lines[0]

pattern = r"([A-Z]{3})"

maps = []
for line in lines[2:]:
    matches = re.findall(pattern, line)
    maps.append(matches)
    
# print(maps)
starts = []
for map in maps:
    starts.append(map[0])
    del(map[0])

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