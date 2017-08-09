n=input("");
def prime_list():
    c=0;
    list=[];
    for i in range(2,n+1):
        c=0;
        for j in range(1,i+1):
            if i%j==0:
                c=c+1;
        if c==2:
            list.append(i);
    return list;
def concatenate_list():
    arr=[];
    for i in prime_list():
        for j in prime_list():
            arr.append(str(i)+str(j))
    return arr
def concatenate_prime(n):
    a=[];
    k=0;
    for i in concatenate_list():
        k=0;
        for j in range(1,int(i)+1):
            if int(i)%j==0:
                k=k+1;
        if k==2:
            if int(i) not in a:
                a.append(int(i))
    print len(a)


concatenate_prime(n);
