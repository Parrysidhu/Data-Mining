import pandas as pd
from efficient_apriori import apriori

#data imp
my_file = pd.read_csv("C:/Users/kjain/Desktop/major/input2.csv", delimiter = ':', header=None)

item = my_file[0]
item_uti = my_file[2]
trans_uti = my_file[1]

item=item.str.split()
item=item.tolist()
item=[list( map(int,i) ) for i in item]

item_uti=item_uti.str.split()
item_uti=item_uti.tolist()
item_uti=[list( map(int,i) ) for i in item_uti]


trans_uti=trans_uti.tolist()

thmin=100

#phase1


ubtu=[]

for i in item_uti:
    ubtuq=0
    for j in i:
        if j>0:
            ubtuq=ubtuq+j
    ubtu.append(ubtuq)
    
#tid
    
def index_2d(myList, v):
    p=[]
    for i in myList:
        if v in i:
            p.append(myList.index(i))
    return (p)
    
tidi=[]
tidt=[]
htwui=[]

for i in item:
    for j in i:
        if j not in tidi:
            tidi.append(j)
            tidt.append(index_2d(item,j))
#tid
            
rules = apriori(item, min_support=0.5,  min_confidence=1)

result=rules[0]
l=[]
j=[]
[l.extend([v]) for k,v in result.items()]
for i in l:
    j=list(i)
    for k in j:
        htwui.append(list(k))
        
htwuis=[]

for i in htwui:
    ubtwu=0
    for j in item:
        if i in j:
            ubtwu=ubtwu+ubtu[item.intdex(j)]
    
    if ubtwu>thmin:
       htwuis.append(i)
       
#phase 2:
    
huis=[]
 
for i in htwuis:
    u=0
    for j in item:
        uj=0
        if i in j:
            for k in i:
                indj=item.index(j)
                indk=j.index(k)
                p=item_uti[j]          
            uj=uj+p[k]
        u=u+uj
        
    if u>thmin:
        huis.append(i)
    
print(huis)       