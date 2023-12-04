import re 
import time
start_time = time.time()
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

with open("Day03.txt", "r") as f:
    contents = f.read()
    
lines = contents.split(sep="\n")

numbers = [None]*len(lines)
indices = [None]*len(lines)
numbers_len = []
boo = []
line_sum = []

for i in range(len(lines)):
    numbers[i], indices[i] = a(lines[i])
    numbers_len.append([len(str(number)) for number in numbers[i]])
    boo.append([0 for number in numbers[i]])

    for j in range(len(numbers[i])):
            for k in range(max(i-1,0), min(i+2, len(lines))):
                for l in range(max(indices[i][j]-1, 0), min(indices[i][j] + numbers_len[i][j] + 1, len(lines[i]))):
                    if lines[k][l] != "." and not lines[k][l].isdigit():
                        boo[i][j] += 1
            if boo[i][j] == 0:
                numbers[i][j] = 0
    line_sum.append(sum(numbers[i]))

print(sum(line_sum))
print("Process finished --- %s seconds ---" % (time.time() - start_time))