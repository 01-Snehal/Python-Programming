#Program of checking whether the number is prime or not. 
x=input("Enter Any Number:")
z=int(x)
a=0
b=2
while(b<=z/2):
    if (z%b==0):
        a=1
        break
    b=b+1
if(a==0):
    print("Number Is Prime!!")
else:
    print("Number Is Not Prime!!")
    
