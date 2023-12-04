with open("Day01.txt", "r") as f:
    contents = f.read()
words = contents.split(sep="\n")

d = {"one": "o1e", "two": "t2o", "three": "th3ee", "four": "f4ur", "five": "f5ve", "six": "s6x", "seven": "se7en", "eight": "ei8ht", "nine": "n9ne"}

for i in range(len(words)):
    for key, value in d.items():
        words[i] = words[i].replace(key, value)

words
    

mirror = [None]*len(words)
i = 0
for word in words:
    mirror[i] = word[::-1]
    i += 1

# mirror

def custom_partition(s, keywords):
    for character in s:
        if character in keywords:
            return s.partition(character)

my_keywords = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

parts1 = [None]*len(words)
parts2 = [None]*len(words)

i = 0
for word in words:
    parts1[i] = custom_partition(word, my_keywords)
    i += 1

# parts1

i = 0
for mir in mirror:
    parts2[i] = custom_partition(mir, my_keywords)
    i += 1

# parts2

double_digits = [None]*len(words)

for i in range(len(words)):
    double_digits[i] = parts1[i][1] + parts2[i][1]

# print(double_digits)
int_sol = [int(item) for item in double_digits]
int_sol

print(sum(int_sol))