import array
arr=array.array("i",[10,5,7,60,87,70])
print(arr)
for i in arr:
    if(i%2==0):
        print("Number Is Even:",i)
    else:
        print("Number Is Odd:",i)
