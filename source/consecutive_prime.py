def prime(n):
    s=0,t=0,l=0;
    for i in range(3,n):
        c=0;
        for j in range(1,i+1):
            if i%j==0:
                c=c+1;
        if c==2:
            s=s+i
            p=s;
            for k in range(1,p+1):
                if p%k==0:
                    t=t+1
                if t==2 and t<=n:
                    l=l+1
             print(t)
            
    
