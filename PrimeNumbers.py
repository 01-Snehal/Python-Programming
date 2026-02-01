a=int(input("Enter Number:"))
i=2
flag=0
while(i<a):
    if(a%i==0):
        flag=1
        break
    i=i+1
if(flag==0):
    print("Number Is Prime")
else:
    print("Number Not Prime")
    
