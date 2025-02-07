import math

def replacedigits(value, old,new):#takes in three strings, and creates a list where each element is a list where the first entry is the first string with some of the values of old replaced with new, and the second entry is a list of the places that were changed.
    tempout=value
    tempind=-1
    out=[]
    x=""
    l=0
    while l<len(tempout):
        if tempind>=0:
            x=x+tempout[l]
        elif tempout[l]==old:
            tempind=l
            x=x+new
        else:
            x=x+tempout[l]
        l+=1
    if x!=value:
        out.append([x,[tempind]])#replaces the first instance of old in value with new but does not replace any other value
        z=replacedigits(x,old,new)#recursively finds all the strings with the first instance of old replaced with new and at least one other instance of old replaced with new
        w=[]#w will contain all the strings made from value where the first entry of of old is not replaced.
        for y in z:
            w.append([y[0],y[1][:]])#creates a copy of z
            y[1].append(tempind)#records that the elements of z have also had the first instance of old changed to new
        out=out+z
        for entry in w:
            entry[0]=entry[0][:tempind]+old+entry[0][tempind+1:]#changes the first replacement back to old in each element of w
        out=out+w
    return out
#make a list of the first several primes
seive=[]
i=0
while i<1000000:
    seive.append(i+1)
    i+=1
i=2
for x in seive:
    if x!=1:
        while i<len(seive)/x:
            seive[(x*i)-1]=1
            i+=1
        i=2
testprimes=[]
for y in seive:
    if y!=1:
        testprimes.append(f"{y}")
currentlist=[]
candidates=[]
candidatesbytype=[]
#start testing which primes fit into the family
i=9000
while i<len(testprimes)-1:
    candidates=[]
    j=0
    #make a list of all possible numbers which can be in the same family as the starting prime
    while j<=2:#j=2 since for there to be a family of 8 one of *=0,1,2 must be a prime
        candidates=[[testprimes[i],-1]]
        candidatesbytype=[]
        currentlist=[]
        ind=j+1#changing a digit to a larger one can only increase the number, so only need to check the primes larger than the current prime
        while ind<10:
            candidates = candidates+replacedigits(testprimes[i],f"{j}",f"{ind}")
            ind+=1
        s=0
        #remove duplicates from candidates
        while s<len(candidates)-1:
            t=s+1
            while t<len(candidates):
                if candidates[s][0]==candidates[t][0]:
                    candidates.pop(t)
                t+=1
            s+=1
        #sort the candidates into the families where the same positions are changed
        templist=[]
        for x in candidates:
            templist.append(x[1])
        a=0
        b=0
        while a<len(templist)-1:
            b=a+1
            while b<len(templist):
                if templist[a]==templist[b]:
                    templist.pop(b)
                b+=1
            a+=1
        temptemplist=[]
        for x in templist:
            for y in candidates:
                if y[1]==x or y[1]==[-1]:
                    temptemplist.append(y[0])
            candidatesbytype.append(temptemplist)
            temptemplist=[]
        #go through the families and see which entries are primes
        k=i
        for y in candidatesbytype:
            y.append(testprimes[i])
            currentlist=list(set(y[:]))#will go through the list and remove entries which are not prime
            m=0
            while m<len(currentlist):
                x=currentlist[m]
                k=i
                while k<len(testprimes):
                    if x==testprimes[k]:
                        break
                    if int(x)<int(testprimes[k]):#removes entry if it is not prime
                        currentlist.pop(m)
                        m=m-1
                        break
                    k+=1
                if m>=8:#means we have found the right answer
                    break
                m+=1
                if len(currentlist)<8:#time saving check, if the list is less than 8 we know we cannot have the right list
                    m=0
                    break
                if m>=8:
                    break
            if len(currentlist)>=8:
                break
        if len(currentlist)>=8:
            break
        j+=1
    if len(currentlist)>=8:
        break
    i+=1
print(currentlist)