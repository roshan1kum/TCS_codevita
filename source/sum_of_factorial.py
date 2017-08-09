def sum(n,k):
    s=0;
    for i in range(0,k+1):
        if i%2==0:
            a=fact(n)
            b=fact(i)
            c=fact(n-i)
            s=s+a/(b*c)
    return s;
def fact(p):
    f=1;
    if p==0:
        return 1
    else:
        for i in range(1,p+1):
            f=f*i;
        return f
        
