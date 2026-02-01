def add(a,*b):
    print(a,b)
    for i in b:
        a=a+i
    return a
s=add(10,30,80,60)
print(s)
