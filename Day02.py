import re
def rgb(s):
    pattern_red = r"(\d{1,2})\s[r]"
    pattern_green = r"(\d{1,2})\s[g]"
    pattern_blue = r"(\d{1,2})\s[b]"
    
    red_matches = re.findall(pattern_red, s)
    green_matches = re.findall(pattern_green, s)
    blue_matches = re.findall(pattern_blue, s)
    
    red = int(red_matches[0]) if red_matches else 0
    green = int(green_matches[0]) if green_matches else 0
    blue = int(blue_matches[0]) if blue_matches else 0
    return red, green, blue

with open("Day02.txt", "r") as f:
    contents = f.read()
    
games = contents.split(sep="\n")
# print(games)

separated = []
for game in games:
    separated.append(game.rsplit(sep = ";"))
    
# print(separated)
# print(separated[0][0])
# print(rgb(separated[0][0]))

game_number = [None]*len(games)
red_cubes = [[0 for i in range(6)] for i in range(len(games))]
green_cubes = [[0 for i in range(6)] for i in range(len(games))]
blue_cubes = [[0 for i in range(6)] for i in range(len(games))]
game_power = [None]*len(games)
# print(red_cubes)
for i in range(len(games)):
    for j in range(len(separated[i])):
        game_number[i] = i+1
        red_cubes[i][j], green_cubes[i][j], blue_cubes[i][j] = rgb(separated[i][j])
        # if red_cubes[i][j] > 12 or green_cubes[i][j] > 13 or blue_cubes[i][j] > 14:
        #     game_number[i] = 0
        #     break
    game_power[i] = max(red_cubes[i]) * max(green_cubes[i]) * max(blue_cubes[i])

# print(game_number[3])
# print(sum(game_number))
print(sum(game_power))