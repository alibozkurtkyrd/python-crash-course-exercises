import csv


dic = {} # store country name and 2014 year expenditure
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

for i, j in dic.items():
    print(i, j)
