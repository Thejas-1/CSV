import re
import csv

with open('analyze.txt') as f:
    print sum(1 for _ in f)

f = open("analyze.txt","r+")
d = f.readlines()
f.seek(0)
#print d
inf = {}
for i in d:
    k = re.split(('\t'),i)
    k.remove(k[2])
    l = dict((k,))
    inf.update(l)
    #print l
print inf
print inf["NATIONAL INSTITUTES OF HEALTH NIH USA"]

name = raw_input("File name:")
with open(name,'wb') as f:
    w = csv.DictWriter(f, inf.keys())
    w.writeheader()
    w.writerow(inf)

with open('harvard.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
