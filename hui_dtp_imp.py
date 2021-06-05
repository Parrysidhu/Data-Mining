import pandas as pd
import pyfpgrowth

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
#phase1

#tid-list

ubtu=[]
thmin=100

for i in item_uti:
    ubtuq=0
    for j in i:
        if j>0:
            ubtuq=ubtuq+j
    ubtu.append(ubtuq)



htwui = list(pyfpgrowth.find_frequent_patterns(item, 100))

##output:[pattern]

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