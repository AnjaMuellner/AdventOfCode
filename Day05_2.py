with open("Day05.txt", "r") as f:
    contents = f.read()

lines = contents.split(sep="\n")

start_seed = lines[0].split(sep=" ")
del(start_seed[0])

ranges = []
i = 1
while i < len(start_seed):
    ranges.append(int(start_seed[i]))
    i += 2

del start_seed[1::2]

for i in range(len(start_seed)):
    start_seed[i] = int(start_seed[i])

def maps(s):
    output = []
    i = lines.index(s) + 1
    while lines[i] != "":
        output.append(lines[i].split(sep=" "))
        i += 1
    for j in range(len(output)):
        for k in range(len(output[j])):
            output[j][k] = int(output[j][k])
    return sorted(output, key=lambda item:item[1])
    
seed_to_soil = maps("seed-to-soil map:")
soil_to_fertilizer = maps("soil-to-fertilizer map:")
fertilizer_to_water = maps("fertilizer-to-water map:")
water_to_light = maps("water-to-light map:")
light_to_temperature = maps("light-to-temperature map:")
temperature_to_humidity = maps("temperature-to-humidity map:")
humidity_to_location = maps("humidity-to-location map:")


def map_it(x, r, x_to_y):
    y = []
    new_ranges = []
    
    j = 0
    while j < len(x):
        for i in range(len(x_to_y)):
            if x[j] >= x_to_y[i][1] and x[j] < x_to_y[i][2] + x_to_y[i][1]:
                if x[j] + r[j] <= x_to_y[i][2] + x_to_y[i][1]:
                    add = x[j] - x_to_y[i][1] + x_to_y[i][0]
                    y.append(add)
                    new_ranges.append(r[j])
                    
                else:
                    add = x[j] - x_to_y[i][1] + x_to_y[i][0]
                    y.append(add)
                    new_ranges.append(x_to_y[i][2] + x_to_y[i][1] - x[j])
                    
                    x.append(x_to_y[i][2] + x_to_y[i][1])
                    r.append(r[j] - (x_to_y[i][2] + x_to_y[i][1] - x[j]))
                    
            elif x[j] + r[j] <= x_to_y[i][2] + x_to_y[i][1] and x[j] + r[j] > x_to_y[i][1]:
                add = x_to_y[i][0]
                # r[j] = x_to_y[i][1] - x[j]
                y.append(x[j])
                new_ranges.append(x_to_y[i][1] - x[j])
                y.append(add)
                new_ranges.append(x[j] + r[j] - x_to_y[i][1])
                
            elif x_to_y[i][1] > x[j] and x_to_y[i][1] + x_to_y[i][2] < x[j] + r[j]:
                add = x_to_y[i][0]            
                y.append(x[j])
                new_ranges.append(x_to_y[i][1] - x[j])
                y.append(add)
                new_ranges.append(x_to_y[i][2])
                r.append(x[j] + r[j] - (x_to_y[i][2] + x_to_y[i][1]))
                x.append(x_to_y[i][2] + x_to_y[i][1])
                
            elif x[j] + r[j] <= x_to_y[i][1]:
                y.append(x[j])
                new_ranges.append(r[j])
                # print("4")
            
            elif x[j] >= x_to_y[i][1] + x_to_y[i][2]:
                continue
                
            break
        j += 1
    
    
    for j in range(len(x)):
        if x[j] >= x_to_y[-1][1] + x_to_y[-1][2]:
            y.append(x[j])
            new_ranges.append(r[j])
            
    return y, new_ranges
    
soil, soil_ranges = map_it(start_seed, ranges, seed_to_soil)
fertilizer, fert_ranges = map_it(soil, soil_ranges, soil_to_fertilizer)
water, water_ranges = map_it(fertilizer, fert_ranges, fertilizer_to_water)
light, light_ranges = map_it(water, water_ranges, water_to_light)
temperature, temp_ranges = map_it(light, light_ranges, light_to_temperature)
humidity, hum_ranges = map_it(temperature, temp_ranges, temperature_to_humidity)
location, loc_ranges = map_it(humidity, hum_ranges, humidity_to_location)

print(min(location))