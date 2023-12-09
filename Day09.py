import re
with open("Day09.txt", "r") as f:
    contents = f.read()

lines = contents.split(sep="\n")

pattern_number = r"(-?\d+)"

sequences = []
for line in lines:
    seq = re.findall(pattern_number, line)
    sequences.append(seq)

def get_sequence(a):
    sequence = []
    for i in range(len(a) - 1):
        sequence.append(int(a[i+1]) - int(a[i]))
    return sequence

lower_sequences = [None]*len(sequences)
for i in range(len(sequences)):
    if lower_sequences[i] == None:
        lower_sequences[i] = [get_sequence(sequences[i])]
    if lower_sequences[i] != None:
        j = 0
        while lower_sequences[i][-1] != [0]*(len(sequences[i])-len(lower_sequences[i])):
            lower_sequences[i].append(get_sequence(lower_sequences[i][j]))
            j += 1


for i in range(len(lower_sequences)):
    for j in range(len(lower_sequences[i])-2, -1, -1):
        lower_sequences[i][j].append(lower_sequences[i][j][-1] + lower_sequences[i][j+1][-1])


sol = []
for i in range(len(sequences)):
    sol.append(int(sequences[i][-1]) + lower_sequences[i][0][-1])

print(sum(sol))