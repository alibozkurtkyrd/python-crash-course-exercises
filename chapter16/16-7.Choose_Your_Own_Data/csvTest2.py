import csv
from pygal.maps.world import World
from country_codes import get_country_code

dic = {} # store country name and 2014 year expenditure
cc_expenditure = {}

with open("education.csv") as file:
    reader = csv.reader(file)

    #count=0

    for row in reader:
        
        if row[-6]:
             dic[row[0]] = row[-6]
            
        #print(row[-6]) # 2014 year
        
        #print(len(row))        
        #if count > 100:
        #    break 
        
        #count +=1

    for country, expenditure in dic.items():
        code = get_country_code(country)

        if code:
            cc_expenditure[code] =int(float(expenditure))

wm = World()
wm.title = 'World Governments expenditure on education'
wm.add('2014',cc_expenditure)
wm.render_to_file('world_expenditure.svg')
