import numpy as np
import csv
ds = {}

with open("placement_readiness.csv","r",encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for col in reader.fieldnames:
             ds[col] = []
    for row in reader:
        for col in reader.fieldnames:           
                 if(row[col].isdigit()) : 
                     ds[col].append(int(row[col]))
                 else :
                     ds[col].append(row[col])

data = np.array(list(ds.values())).T
print(data)

#average of python_score (1st column)
py_avg = np.mean(data[:,2].astype(int))
print(py_avg)

#highest and lowest aptitude score (3rd column)
high_aps = np.max(data[:,4].astype(int))
lowst_aps = np.min(data[:,4].astype(int))

print(high_aps,lowst_aps)

#students with score above 70 in communication (4th column)
list = (data[:,5].astype(int))

print(list[list>70])

#diff btw strongest skill and weakest skill for every student

for row in data:
    a = row[2:6].astype(int)
    print(row[0],a.max() - a.min())