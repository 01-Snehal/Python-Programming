def primeno():
    flag=0
    i=2
    a=int(input("Enter Number:"))
    while(i<a):
        if(a%i==0):
            flag=1
            break
        i=i+1
    if(flag==0):
        print("Number Is Prime")
    else:
        print("Number Is Not Prime")
primeno()
