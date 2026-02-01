def primeno():
    a=int(input("Enter A number"))
    flag=0
    i=2
    while(i<a):
        if(a%i==0):
            flag=1
            break
        i=i+1
    if(flag==0):
        print("number is prime")
    else:
        print("number is not prime")
primeno()   
