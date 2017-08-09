l=input();
u=input();
a=[]
for i in range(l,u):
    c=0;
    k=0;
    list=[]
    s=""
    for g in range(1,4):
        s=s+str(i*g)
        p=s.replace('0','')
    for h in p:
        c=c+1;
    if c==9:
        for j in p:
            if j not in list:
                if p.count(j)==1:
                    list.append(j)
                    k=k+1
        if k==9:
            a.append(i)
print a
                  
        
                
        

