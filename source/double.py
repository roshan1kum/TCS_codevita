n=input()
n1=input()
list=[];
s=0;
def prime_list():
    c=0;
    list=[];
    for i in range(2,n+1):
        c=0;
        for j in range(1,i+1):
            if i%j==0:
                c=c+1;
        if c==2:
            list.append(int(i));
    return list;

def double():
    list1=[];
    index=[];
    s=0;
    a=0;
    for i in prime_list():
        s=i;
        for j in range(0,n1):
            s=2*s+1;
            if s not in prime():
                break;
        if s in prime():
            list1.append(i)
    print list1
    
def prime():
    index=[];
    for i in range(2,1000+1):
        c=0;
        for j in range(1,i+1):
            if i%j==0:
                c=c+1;
        if c==2:
            index.append(int(i));
    return index;

double()

        
