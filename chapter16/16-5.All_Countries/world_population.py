#world_population.py

import json
from pygal.maps.world import World
from country_codes import get_country_code

from pygal.style import RotateStyle # 1st line

# Load the data into a list.
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f) # 1st line
    
# Build a dictionary of population data.

cc_populations = {} 
    
# Print the 2010 population for each country
for pop_dict in pop_data:   # 2nd line
    if pop_dict['Year'] == '2010':  
        country_name = pop_dict['Country Name']  
        population = int(float(pop_dict['Value']))   
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population 
        else :
            print(country_name)
                        
# Group the countries into 3 population levels.

cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {} # 1st line
for cc, pop in cc_populations.items():  
    if pop < 10000000: 
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop
    
wm_style = RotateStyle('#336699') # 2nd line
wm = World(style=wm_style) # 3rd line
wm.title = 'World Populations in 2010, by Country'
wm.add('0-10m', cc_pops_1) # 4th line
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('world_population.svg')
