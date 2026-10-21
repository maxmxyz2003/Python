def func(a,b):
    i=2
    res=1
    while a>=i or b>=i:
        if a%i==0 and b%i==0:
            a//=i
            b//=i
            res*=i
        elif a%i==0:
            a//=i
            res*=i
        elif b%i==0:
            b//=i
            res*=i
        if a%i!=0 and b%i!=0:
            i+=1
    print(res)

func(15,50)

