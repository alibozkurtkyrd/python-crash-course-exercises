import json
from  pygal.maps.world import World
from  country_codes import get_country_code

# Load the data into a List.
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)


# Build a dictionary of population data.

cc_populations = {}

# Build a dictionary of missing countries.

missing_counteries = {}
missing_counteries['Yemen, Rep.'] = 'ye'
missing_counteries['Venezuela, RB'] = 've'
missing_counteries['Vietnam'] = 'vn'
missing_counteries['Tanzania'] = 'tz'
missing_counteries['Libya'] = 'ly'
missing_counteries['Korea, Dem. Rep.'] = 'kp'

missing_counteries['Korea, Rep.'] = 'kr'
missing_counteries['Egypt, Arab Rep.'] = 'eg'
missing_counteries['Hong Kong SAR, China'] = 'hk'
missing_counteries['Iran, Islamic Rep.'] = 'ir'

# Print the 2010 population for each country
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population
        else:
            if (country_name in missing_counteries.keys()):
                code = missing_counteries[country_name]
                print(country_name)
                print(code)
                print(population)
                cc_populations[code] = population
wm = World()
wm.title = 'World Population in 2010, by Country'
wm.add('2010', cc_populations)

wm.render_to_file('Solution.svg')
