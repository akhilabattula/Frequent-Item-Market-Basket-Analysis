'''
Created on Jun 27, 2016

@author: akhila
'''

import random
import sys
import itertools

def generate_sample():
    slen=int(round((samplesize*len(allsets))/100))
    sample=[]
    for i in range(0,slen):
        if random.choice(allsets) in sample:
            i+=1
        else:
            sample.append(random.choice(allsets))
            i+=1
    return sample   
def generate_sets(j,val):
    rsets=list(itertools.combinations(j,val))
    return rsets

def generate_freq_items(itmcount):
    mysupport=int(round(((samplesize+1)*support*0.8)/(125)))
    print "my suport",mysupport
    mylist=[]
    print itmcount
    for i in itmcount:
        if itmcount[i]>=mysupport:
            mylist.append(i)
    print "mylist",mylist
    return mylist      
fp=open(sys.argv[1],'r')
itemcount={}
samplesize=50
support=20
allsets=[]
for i in fp:
    allsets.append(i.replace('\n',"").split(','))
    
sset=generate_sample()
samplesize-=1

print "random sample",sset
for i in sset:
    for j in i:
        if j in itemcount:
            itemcount[j]+=1
        else:
            itemcount[j]=1
counter=2
freq_items=generate_freq_items(itemcount)
print "freq here is",freq_items
mypairs=itemcount
while(mypairs!={}):
    mypairs={}
    for i in sset:
        pair1=generate_sets(i,counter)
        for pair in pair1:
            pair=sorted(pair)
            if (tuple(pair)) in mypairs.keys():
                mypairs[tuple(pair)]=mypairs[tuple(pair)]+1
            else:
                mypairs[tuple(pair)]=1
    x=generate_freq_items(mypairs)
    freq_items.append(x)
    print "freq items is",freq_items
    counter+=1
    
    


print "freqitems",freq_items