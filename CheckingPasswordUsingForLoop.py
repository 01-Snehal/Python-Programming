a=input("Enter The Password:")
b=0
c=0
d=0
ny=0
l=0
for i in a:
    asc=ord(i)
    if(asc>=65 and asc<=90):
        b=1
    elif(asc>=97 and asc<=122):
        c=1
    elif(asc>=48 and asc<57):
        d=1
    elif(asc>=58 and asc<=64):
        ny=1
if(len(a)>=8):
    l=1
if(b==1 and c==1 and d==1 and ny==1 and l==1):
    print("The Password Is Valid!!!")
else:
    print("Password Is Invalid!!!")
