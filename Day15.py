with open("Day15.txt", "r") as f:
    contents = f.read()

parts = contents.split(sep=",")

def hash(s):
    current_value = 0
    for c in s:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    return current_value

sol = []
for part in parts:
    sol.append(hash(part))

print(sum(sol))