def addition(l1,l2,b):
    res = []
    total=0
    for i in range(len(l1),-1,-1):
        total=l1[i]+l2[i]
        if total>b:
            res.insert(i-1,total-b)
        else:
            res.insert(i,total)    
        return res

test1 = conversionBase(7,2)
test2 = conversionBase(8,2)

addition(test1,test2,2)

#Ce que j'avais commencé mais effacer car ce n'etait pas bon