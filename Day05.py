with open("Day05.txt", "r") as f:
    contents = f.read()

lines = contents.split(sep="\n")

seed = lines[0].split(sep=" ")
del(seed[0])

def maps(s):
    output = []
    i = lines.index(s) + 1
    while lines[i] != "":
        output.append(lines[i].split(sep=" "))
        i+= 1
    return output
    
seed_to_soil = maps("seed-to-soil map:")
soil_to_fertilizer = maps("soil-to-fertilizer map:")
fertilizer_to_water = maps("fertilizer-to-water map:")
water_to_light = maps("water-to-light map:")
light_to_temperature = maps("light-to-temperature map:")
temperature_to_humidity = maps("temperature-to-humidity map:")
humidity_to_location = maps("humidity-to-location map:")


def map_it(x, x_to_y):
    y = []
    index_added = []
    for i in range(len(x_to_y)):
        for j in range(len(x)):
            if int(x[j]) >= int(x_to_y[i][1]) and int(x[j]) <= int(x_to_y[i][2]) + int(x_to_y[i][1]):
                add = int(x[j]) - int(x_to_y[i][1]) + int(x_to_y[i][0])
                y.append(add)
                index_added.append(j)
    
    for j in range(len(x)):
        if j not in index_added:
            y.append(int(x[j]))
    return y
    
soil = map_it(seed, seed_to_soil)
fertilizer = map_it(soil, soil_to_fertilizer)
water = map_it(fertilizer, fertilizer_to_water)
light= map_it(water, water_to_light)
temperature = map_it(light, light_to_temperature)
humidity = map_it(temperature, temperature_to_humidity)
location = map_it(humidity, humidity_to_location)

print(min(location))