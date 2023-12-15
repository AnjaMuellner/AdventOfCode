with open("Day15.txt", "r") as f:
    contents = f.read()

parts = contents.split(sep=",")

for i in range(len(parts)):
    if "=" in parts[i]:
        new_string = parts[i][:parts[i].index("=")] + " " + parts[i][parts[i].index("=")+1:]
        parts[i] = new_string
    elif "-" in parts[i]:
        new_string = parts[i][:parts[i].index("-")]
        parts[i] = new_string

def hash(s):
    current_value = 0
    for c in s:
        if c == " ":
            break
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    return current_value

hashes = []
for part in parts:
    hashes.append(hash(part))

boxes = [[] for _ in range(256)]
for i in range(len(parts)):
    if " " in parts[i]:
        if boxes[hashes[i]] == []:
            boxes[hashes[i]].append(parts[i])
        else:
            for j in range(len(boxes[hashes[i]])):
                if parts[i][:parts[i].index(" ")] in boxes[hashes[i]][j]:
                    boxes[hashes[i]][j] = parts[i]
                    break
            else:
                boxes[hashes[i]].append(parts[i])
    else:
        for j in range(len(boxes[hashes[i]])):
            if parts[i] in boxes[hashes[i]][j]:
                del(boxes[hashes[i]][j])
                break


box_worth = [0 for _ in range(len(boxes))]
for i in range(len(boxes)):
    if boxes != []:
        for j in range(len(boxes[i])):
            box_worth[i] += (i + 1) * (j + 1) * int(boxes[i][j][boxes[i][j].index(" ")+1:])

print(sum(box_worth))