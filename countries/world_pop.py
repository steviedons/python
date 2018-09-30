import json
from pygal.maps.world import World
from countries import get_country_code

filename = "population_data.json"

with open(filename) as f:
    pop_data = json.load(f)

# Build a dictionary of world populations
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == "2010":
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population


wm = World()
wm.force_uri_protocol = 'http'

#wm.title("World population in 2010, by country")
wm.add('2010', cc_populations)

wm.render_to_file('world_pop.svg')