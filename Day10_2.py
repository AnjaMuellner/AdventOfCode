with open("Day10.txt", "r") as f:
    contents = f.read()
    
lines = contents.split(sep="\n")

loop = ["S"]

# Lines, rows
indices = []
for line in lines:
    if "S" in line:
        indices.append([lines.index(line), line.index("S")])
        break

# north, south, west, east
around_s = [lines[indices[0][0] - 1][indices[0][1]], lines[indices[0][0] + 1][indices[0][1]], lines[indices[0][0]][indices[0][1] - 1], lines[indices[0][0]][indices[0][1] + 1]]
# print(around_s)

def goto(lines, loop, indices):
    if indices[-1][0] > 0:
        north = lines[indices[-1][0] - 1][indices[-1][1]]
        north_index = [indices[-1][0] - 1, indices[-1][1]]
    if indices[-1][0] < len(lines) - 1:
        south = lines[indices[-1][0] + 1][indices[-1][1]]
        south_index = [indices[-1][0] + 1, indices[-1][1]]
    if indices[-1][1] > 0:
        west = lines[indices[-1][0]][indices[-1][1] - 1]
        west_index = [indices[-1][0], indices[-1][1] - 1]
    if indices[-1][1] < len(lines[0]) - 1:
        east = lines[indices[-1][0]][indices[-1][1] + 1]
        east_index = [indices[-1][0], indices[-1][1] + 1]

    if loop[-1] == "|":
        # from south, go north
        if indices[-1][0] == indices[-2][0] - 1:
            return [north, north_index]
        # from north, go south
        else:
            return [south, south_index]
    elif loop[-1] == "-":
        # from west, go east
        if indices[-1][1] == indices[-2][1] + 1:
            return [east, east_index]
        # from east, go west
        else:
            return [west, west_index]
    elif loop[-1] == "L":
        # from east, go north
        if indices[-1][1] == indices[-2][1] - 1:
            return [north, north_index]
        # from north, go east
        else:
            return [east, east_index]
    elif loop[-1] == "J":
        # from west, go north
        if indices[-1][1] == indices[-2][1] + 1:
            return [north, north_index]
        # from north, go west
        else:
            return [west, west_index]
    elif loop[-1] == "7":
        # from west, go south
        if indices[-1][1] == indices[-2][1] + 1:
            return [south, south_index]
        # from south, go west
        else:
            return [west, west_index]
    elif loop[-1] == "F":
        # from east, go south
        if indices[-1][1] == indices[-2][1] - 1:
            return [south, south_index]
        # from south, go east
        else:
            return [east, east_index]
    # return next loop, next index


i = 0
while (loop[i] != "S" or len(loop) == 1):
    if loop[i] == "S":
        # go north
        loop.append(lines[indices[i][0] - 1][indices[i][1]])
        indices.append([indices[i][0] - 1, indices[i][1]])
        # loop.append(lines[indices[-1][0]][indices[-1][1] + 1])
        # indices.append([indices[-1][0], indices[-1][1] + 1])
    else:
        new_loop, new_index = goto(lines, loop, indices)
        loop.append(new_loop)
        indices.append(new_index)
    i += 1


del(indices[-1])
del(loop[-1])
for i in range(len(lines)):
    if "S" in lines[i]:
        lines[i] = lines[i].replace("S", "|")
        break
    
sorted_indices = sorted(indices, key=lambda x: (x[0], x[1]))

enclosed = 0
i = 0
for i in range(len(lines)):
    counter = 0
    for k in range(len(lines[i])):
        if [i,k] in sorted_indices:
            if lines[i][k] == "|" or lines[i][k] == "L" or lines[i][k] == "J":
                counter += 1
        elif counter % 2 == 1:
            # print(i, counter)
            enclosed += 1
            
print(enclosed)