filename = '2023/input/day5.txt'
lines = open(filename, 'r').readlines()

seeds = [79, 14, 55, 13] # test
seeds = "858905075 56936593 947763189 267019426 206349064 252409474 660226451 92561087 752930744 24162055 75704321 63600948 3866217991 323477533 3356941271 54368890 1755537789 475537300 1327269841 427659734".split()

def parse_line(line):
    return list(map(int, line.strip().split()))

seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []

locations = []

current_map = None
for line in lines:
    if line.startswith('seed-to-soil map'):
        current_map = seed_to_soil
    elif line.startswith('soil-to-fertilizer map'):
        current_map = soil_to_fertilizer
    elif line.startswith('fertilizer-to-water map'):
        current_map = fertilizer_to_water
    elif line.startswith('water-to-light map'):
        current_map = water_to_light
    elif line.startswith('light-to-temperature map'):
        current_map = light_to_temperature
    elif line.startswith('temperature-to-humidity map'):
        current_map = temperature_to_humidity
    elif line.startswith('humidity-to-location map'):
        current_map = humidity_to_location
    elif line.strip() == '':
        continue
    else:
        current_map.append(parse_line(line))

for seed in seeds:
    seed = int(seed)
    soil = seed
    for map in seed_to_soil:
        destination_start, source_start, length = map
        if source_start < seed < source_start + length:
            soil = destination_start + seed - source_start
    
    fert = soil
    for map in soil_to_fertilizer:
        destination_start, source_start, length = map
        if source_start < soil < source_start + length:
            fert = destination_start + soil - source_start

    water = fert
    for map in fertilizer_to_water:
        destination_start, source_start, length = map
        if source_start < fert < source_start + length:
            water = destination_start + fert - source_start
    
    light = water
    for map in water_to_light:
        destination_start, source_start, length = map
        if source_start < water < source_start + length:
            light = destination_start + water - source_start

    temp = light
    for map in light_to_temperature:
        destination_start, source_start, length = map
        if source_start < light < source_start + length:
            temp = destination_start + light - source_start

    hum = temp
    for map in temperature_to_humidity:
        destination_start, source_start, length = map
        if source_start < temp < source_start + length:
            hum = destination_start + temp - source_start
    
    location = hum
    for map in humidity_to_location:
        destination_start, source_start, length = map
        if source_start < hum < source_start + length:
            location = destination_start + hum - source_start

    locations.append(location)

print(min(locations))