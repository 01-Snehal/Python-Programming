a=input("Enter Number:")
b=int(a)
flag=0
i=2
while(i<b):
    if(b%i==0):
        flag=1
        break
    i=i+1
if(flag==0):
    print("Number Is Prime")
else:
    print("Number Is Not Prime")
