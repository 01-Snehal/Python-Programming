import array
arr=array.array("i",[[10,30,50][70,80,90]])
print(arr)
s=arr[0]
for i in range(len(arr)):
    if(arr[i]>s):
        s=arr[i]
print("Maximum Number Is:",arr[i])