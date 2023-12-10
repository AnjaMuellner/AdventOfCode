with open("Day07.txt", "r") as f:
    contents = f.read()
    
lines = contents.split(sep="\n")

cards = []
bids = []
for line in lines:
    cards.append(line.partition(" ")[0])
    bids.append(int(line.partition(" ")[2]))

custom_order = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

sorted_cards = []
for hand in cards:
    sorted_cards.append("".join(sorted(hand, key=lambda x: custom_order.index(x))))

def type(s):
    # Five of a kind (7)
    if s[0] == s[4]:
        i = 7
    # Four of a kind (6)
    elif s[0] == s[3] or s[1] == s[4]:
        i = 6
        if s[4] == "J":
            i = 7
    # Full House (5)
    elif (s[0] == s[2] and s[3] == s[4]) or (s[0] == s[1] and s[2] == s[4]):
        i = 5
        if s[4] == "J":
            i = 7
    # Three of a kind (4)
    elif (s[0] == s[2] and s[3] != s[4]) or (s[1] == s[3] and s[0] != s[4]) or (s[2] == s[4] and s[0] != s[1]):
        i = 4
        if s[4] == "J":
            i = 6
    # Two pair (3)
    elif (s[0] == s[1] and s[2] == s[3]) or (s[1] == s[2] and s[3] == s[4]) or (s[0] == s[1] and s[3] == s[4]):
        i = 3
        if s[4] == "J" and s[3] != "J":
            i = 5
        elif s[4] == "J":
            i = 6
    # One pair (2)
    elif s[0] == s[1] or s[1] == s[2] or s[2] == s[3] or s[3] == s[4]:
        i = 2
        if s[4] == "J":
            i = 4
    # High card (1)
    elif s[0] != s[1] != s[2] != s[3] != s[4]:
        i = 1
        if s[4] == "J":
            i = 2
    return i



types = []
counters = [0]*7
cards_bids_types = [None]*len(cards)

for i in range(len(sorted_cards)):
    types.append(type(sorted_cards[i]))
    if types[i] == 1:
        counters[0] += 1
    elif types[i] == 2:
        counters[1] += 1
    elif types[i] == 3:
        counters[2] += 1
    elif types[i] == 4:
        counters[3] += 1
    elif types[i] == 5:
        counters[4] += 1
    elif types[i] == 6:
        counters[5] += 1
    elif types[i] == 7:
        counters[6] += 1
    cards_bids_types[i] = [cards[i], bids[i], types[i]]

cards_bids_types.sort(key=lambda item:item[2])

for i in range(len(counters)):
    if i != 0:
        counters[i] += counters[i-1]
        ordered = sorted(cards_bids_types[counters[i-1]:counters[i]], key=lambda x: custom_order.index(str(x[0][0])), reverse=True)
        cards_bids_types[counters[i-1]:counters[i]] = ordered
    else:
        ordered = sorted(cards_bids_types[0:counters[i]], key=lambda x: custom_order.index(str(x[0][0])), reverse=True)
        cards_bids_types[0:counters[i]] = ordered
    
    
i = 0
while i < len(cards_bids_types) - 1:
    j = i
    c = 0
    while cards_bids_types[j][0][0] == cards_bids_types[j+1][0][0]:
        j += 1
        c += 1
    ordered = sorted(cards_bids_types[i:j+1], key=lambda x: custom_order.index(str(x[0][1])), reverse=True)
    cards_bids_types[i:j+1] = ordered
    if c != 0:
        i += c
    else: 
        i += 1


i = 0
while i < len(cards_bids_types) - 1:
    j = i
    c = 0
    while cards_bids_types[j][0][0] == cards_bids_types[j+1][0][0] and cards_bids_types[j][0][1] == cards_bids_types[j+1][0][1]:
        j += 1
        c += 1
    ordered = sorted(cards_bids_types[i:j+1], key=lambda x: custom_order.index(str(x[0][2])), reverse=True)
    cards_bids_types[i:j+1] = ordered
    if c != 0:
        i += c
    else: 
        i += 1
        
i = 0
while i < len(cards_bids_types) - 1:
    j = i
    c = 0
    while cards_bids_types[j][0][0] == cards_bids_types[j+1][0][0] and cards_bids_types[j][0][1] == cards_bids_types[j+1][0][1] and cards_bids_types[j][0][2] == cards_bids_types[j+1][0][2]:
        j += 1
        c += 1
    ordered = sorted(cards_bids_types[i:j+1], key=lambda x: custom_order.index(str(x[0][3])), reverse=True)
    cards_bids_types[i:j+1] = ordered
    if c != 0:
        i += c
    else: 
        i += 1

i = 0
while i < len(cards_bids_types) - 1:
    j = i
    c = 0
    while cards_bids_types[j][0][0] == cards_bids_types[j+1][0][0] and cards_bids_types[j][0][1] == cards_bids_types[j+1][0][1] and cards_bids_types[j][0][2] == cards_bids_types[j+1][0][2] and cards_bids_types[j][0][3] == cards_bids_types[j+1][0][3]:
        j += 1
        c += 1
    ordered = sorted(cards_bids_types[i:j+1], key=lambda x: custom_order.index(str(x[0][4])), reverse=True)
    cards_bids_types[i:j+1] = ordered
    if c != 0:
        i += c
    else: 
        i += 1

prod = []
for i in range(len(cards_bids_types)):
    prod.append((i + 1) * cards_bids_types[i][1])

print(cards_bids_types)    

print(sum(prod))