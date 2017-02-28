'''
Created on Jun 26, 2016

@author: akhila
'''
import itertools
import sys


def generate_sets(i,j):
    mysets=tuple(itertools.combinations(i,j))
    return mysets
            
def computehash1(k):
    sum1=0
    for i in k:
        sum1=sum1 + item_to_int[i]
    return sum1 % bucketsize

def computehash2(k):
    sum1=0
    for i in k:
        sum1=abs(sum1-item_to_int[i])
    return sum1 % bucketsize




def generate_bitmap(stage_table):
    bitmap=[]
    for i in stage_table:
        if stage_table[i] >support:
            bitmap.append(1)
        else:
            bitmap.append(0)
    return bitmap


def generate_frequent_items():
    tmplist=[]
    for i in itemcount:
        if itemcount[i]>=support:
            tmplist.append(i)
            
    tmplist=sorted(tmplist)
    return tmplist   

     
def check_all_subsets_frequent(k,mc):
    #print "checking subsets",k,"frequents is",next_frequent_items,"counter is",mc
    flag=True
    pop=[]
    #print "again k is",type(k)
    if(mc-1==1):
        for pp in k:
            pop.append(pp)
    else:
        pop=list(itertools.combinations(k,mc-1))
    #print "p is",pop
    for i in pop:
       
        #print "i is",i
        if i not in next_frequent_items:
            flag=False
    #print "final flag",flag
    return flag
            
                
fp=open(sys.argv[1],'r')
counter=1
item_to_int={}
itemcount={}
stage_1_hashtable1={}
stage_1_hashtable2={}
support=4
bucketsize=5
for i in range(0,bucketsize):
    stage_1_hashtable1[i]=0
    stage_1_hashtable2[i]=0
for i in fp:
    tmplist=[]
    for j in i:
        if j!=',' and j!='\n':
            tmplist.append(j)
    tmplist=sorted(tmplist)
    #print "tmp list here is",tmplist
    for j in tmplist:
        if j not in  itemcount and j!=',' and j!='\n':
            itemcount[j]=1
        elif j!=',' and j!='\n':
            itemcount[j]=itemcount[j]+1
        if(j!=',') and j!='\n' and j not in item_to_int:
            item_to_int[j]=counter
            counter+=1
    allsets=generate_sets(tmplist,2)
    #print "generated sets",allsets
    for k in allsets:
        value1=computehash1(k)
        value2=computehash2(k)
        stage_1_hashtable1[value1]=stage_1_hashtable1[value1]+1
        stage_1_hashtable2[value2]=stage_1_hashtable2[value2]+1
#eligible_nextstage=see_eligible_nextstage()
bitmap1=generate_bitmap(stage_1_hashtable1)
bitmap2=generate_bitmap(stage_1_hashtable1)
frequent_items=generate_frequent_items()



"""print "item to int",item_to_int
print "item count",itemcount

#print "elgible list",eligible_nextstage
print "bitmap is",bitmap"""
#print "frequent items",frequent_items
#print "stage_1_hashtable",stage_1_hashtable

maincounter=2
nextbitmap1=bitmap1
nextbitmap2=bitmap2
#print "nextbitmap is",nextbitmap
next_frequent_items=frequent_items
hashtable_prevlevel1=stage_1_hashtable1
hashtable_prevlevel2=stage_1_hashtable2
#print "next frequent items",next_frequent_items
while (len(next_frequent_items)!=0):
    print next_frequent_items
    #print hashtable_nextlevel
    final_frequent_pairs_count={}
    hashtable1_nextlevel={}
    hashtable2_nextlevel={}
    fp=open(sys.argv[1],'r')
    for i in fp:
        tmplist=[]
        #print "i is",i
        for j in i:
            if j!=',' and j!='\n':
                tmplist.append(j)
        #print "tmplist is",tmplist
        allsets=generate_sets(tmplist,maincounter)
        #print "allsets",allsets
        nextsets=generate_sets(tmplist,maincounter+1)
        #print "nextsets",nextsets
        
        #print "all sets is",allsets
        for k in allsets:
            #print "type of k is",type(k)
            value1=computehash1(k)
            value2=computehash2(k)
            #print "value is",value
            #print "k is",k,"allsets is",allsets
            #print "bitmap[value]",bitmap[value]
            k=sorted(k)
             
            #print "k is",k,"bit value of nextbitmap[" , value , "]=", nextbitmap
            if nextbitmap1[value1]==1 and nextbitmap2[value2]==1  and check_all_subsets_frequent(k,maincounter)==True:
                #print "candidate it is",k
                if (tuple(k)) in final_frequent_pairs_count.keys():
                    final_frequent_pairs_count[tuple(k)]=final_frequent_pairs_count[tuple(k)]+1
                else:
                    final_frequent_pairs_count[tuple(k)]=1
                    #print "nextsets is",nextsets
        for p in nextsets:
            val1=computehash1(p)
            hashtable1_nextlevel.setdefault(val1,0)
            hashtable1_nextlevel[val1]=hashtable1_nextlevel[val1]+1
            val2=computehash2(p)
            hashtable2_nextlevel.setdefault(val2,0)
            hashtable2_nextlevel[val2]=hashtable2_nextlevel[val2]+1
        
            
    final_frequent_pairs=[]            
    for i in final_frequent_pairs_count:
        if final_frequent_pairs_count[i]>=support:
            final_frequent_pairs.append(i)                
    final_frequent_pairs=sorted(final_frequent_pairs)
    nextbitmap1=generate_bitmap(hashtable1_nextlevel) 
    nextbitmap2=generate_bitmap(hashtable2_nextlevel)       
    next_frequent_items=final_frequent_pairs
    if(next_frequent_items!=[]):
        print hashtable_prevlevel1
        print hashtable_prevlevel2
    
    hashtable_prevlevel1=hashtable1_nextlevel
    hashtable_prevlevel2=hashtable2_nextlevel
    
    
    maincounter+=1
    

