with open("Day11.txt", "r") as f:
    contents = f.read()
    
lines = contents.split(sep="\n")

dot_line = []
for i  in range(len(lines)):
    if "#" not in lines[i]:
        dot_line.append(i)

boo_indices = []
boo = [0]*len(lines[0])
for j in range(len(lines[0])):
    for i in range(len(lines)):
        if lines[i][j] == "#":
            boo[j] = 1

for j in range(len(boo)):
    if boo[j] == 0:
        boo_indices.append(j)

dot_col = []
for j in range(len(lines[0])):
    if j in boo_indices:
        dot_col.append(j)
    
counter = 0
number_indices = []
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "#":
            number_indices.append([i,j])

steps = []
for i in range(len(number_indices)):
    j = i + 1
    while j < len(number_indices):
        steps.append(abs(number_indices[j][0] - number_indices[i][0]) + abs(number_indices[j][1] - number_indices[i][1]))
        for line_index in dot_line:
            if number_indices[i][0] < line_index and number_indices[j][0] > line_index:
                steps[-1] += 999999
        for col_index in dot_col:
            if (number_indices[i][1] < col_index and number_indices[j][1] > col_index) or (number_indices[j][1] < col_index and number_indices[i][1] > col_index):
                steps[-1] += 999999
        j += 1

print(sum(steps))