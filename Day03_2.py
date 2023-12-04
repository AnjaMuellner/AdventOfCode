import re
def a(s):
    pattern_number = r"(\d+)"
    matches = re.finditer(pattern_number, s)
    
    numbers = []
    indices = []
    
    for match in matches:
        number = int(match.group())
        index = match.start()
        numbers.append(number)
        indices.append(index)
    return numbers, indices

def b(s):
    pattern_number = r"\*"
    matches = re.finditer(pattern_number, s)
    
    star_indices = []
    
    for match in matches:
        star_index = match.start()
        star_indices.append(star_index)
    return star_indices
        
with open("Day03.txt", "r") as f:
    contents = f.read()
    
lines = contents.split(sep="\n")

numbers = [None]*len(lines)
indices = [None]*len(lines)
star_indices = [None]*len(lines)
numbers_len = []
boo = []
line_sum = []

for i in range(len(lines)):
    numbers[i], indices[i] = a(lines[i])
    star_indices[i] = b(lines[i])
    numbers_len.append([len(str(number)) for number in numbers[i]])
    boo.append([0 for number in numbers[i]])
    
gear_numbers = [[[]for i in range(7)] for j in range(150)]

for i in range(len(lines)):
    if len(star_indices[i]) > 0:
        for j in range(len(star_indices[i])):
            for k in range(max(i-1,0), min(i+2, len(lines))):
                l = max(star_indices[i][j]-1, 0)
                while l < min(star_indices[i][j] + 2, len(lines[i])):
                    if l in indices[k]:
                        gear_numbers[i][j].append(numbers[k][indices[k].index(l)])
                        l += numbers_len[k][indices[k].index(l)]
                    elif lines[k][l].isdigit() and lines[k][l+1].isdigit():
                        gear_numbers[i][j].append(numbers[k][indices[k].index(l-1)])
                        l += 2
                    elif lines[k][l].isdigit() and lines[k][l+1] == "*":
                        if l-1 in indices[k]:
                            gear_numbers[i][j].append(numbers[k][indices[k].index(l-1)])
                        elif l-2 in indices[k]:
                            gear_numbers[i][j].append(numbers[k][indices[k].index(l-2)])
                        else:
                            print("Oh no")
                        l += 2
                    elif lines[k][l].isdigit() and lines[k][l+1] == ".":
                        if l-1 in indices[k]:
                            gear_numbers[i][j].append(numbers[k][indices[k].index(l-1)])
                        elif l-2 in indices[k]:
                            gear_numbers[i][j].append(numbers[k][indices[k].index(l-2)])
                        else:
                            print("Oh no")
                        l += 1
                    else:
                        l += 1

prod = []
for i in range(len(gear_numbers)):
    for j in range(len(gear_numbers[i])):
        if len(gear_numbers[i][j]) == 2:
            prod.append(gear_numbers[i][j][0] * gear_numbers[i][j][1])
        else:
            for k in range(len(gear_numbers[i][j])):
                gear_numbers[i][j][k] = 0
print(sum(prod))