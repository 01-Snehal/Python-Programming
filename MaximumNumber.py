a=[10,54,89,90,100]
#print(max(a))
m=a[0]
for i in range(len(a)):
    if(a[i]>m):
        m=a[i]
print("Maximum Number Is:",m)
