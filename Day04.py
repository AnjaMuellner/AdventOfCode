import re
def numb(s):
    pattern_number = r"(\d+)"
    matches = re.finditer(pattern_number, s)
    
    numbers = []
    
    for match in matches:
        number = int(match.group())
        numbers.append(number)
    return numbers

with open("Day04.txt", "r") as f:
    contents = f.read()

cards = contents.split(sep="\n")

only_numbers = []
points = [0]*len(cards)
matches = [0]*len(cards)
winning_numbers = [None]*len(cards)
my_numbers = [None]*len(cards)
copies = [1]*len(cards)
mult = [1]*len(cards)
for i in range(len(cards)):
    only_numbers.append(cards[i].split(" | "))
    only_numbers[i][0] = only_numbers[i][0].split(": ")
    only_numbers[i][0] = only_numbers[i][0][1]
    winning_numbers[i] = numb(only_numbers[i][0])
    my_numbers[i] = numb(only_numbers[i][1])
    for j in range(len(my_numbers[i])):
        if my_numbers[i][j] in winning_numbers[i]:
            matches[i] += 1
    if matches[i] != 0:
        for k in range(matches[i]):
            if i+k+1 < len(cards):
                copies[i+k+1] += copies[i]
        # points[i] = (2 ** (matches[i] - 1))

print(sum(copies))
# print(sum(points))