import pandas as pd
from efficient_apriori import apriori
import timeit
import matplotlib.pyplot as plt

pattern1=[]
dataset_size=[]

#data imp

for loop in range(1,6):
    if loop==1:
        my_file = pd.read_csv("C:/Users/kjain/Desktop/major/chess_utility_spmf.csv", delimiter = ':', header=None)
    elif loop==2:
        my_file = pd.read_csv("C:/Users/kjain/Desktop/major/connect_utility_spmf.csv", delimiter = ':', header=None)
    elif loop==3:
        my_file = pd.read_csv("C:/Users/kjain/Desktop/major/pumsb_utility_spmf.csv", delimiter = ':', header=None)
    elif loop==4:
        my_file = pd.read_csv("C:/Users/kjain/Desktop/major/retail_utility_spmf.csv", delimiter = ':', header=None)


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
    
    start = timeit.default_timer()
    
    num_trans=len(trans_uti)
    dataset_size.append(num_trans)

#phase1 apr

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
    stop = timeit.default_timer()
    time=stop-start
    pattern1.append(time)
    

plt.plot(dataset_size, pattern1, label="HUI_DTP")
plt.xlabel('dataset_size')
plt.ylabel('TIME')
plt.title('Time Complexcity')
plt.show()           