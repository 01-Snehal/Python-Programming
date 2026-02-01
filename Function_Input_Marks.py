def marks():
    sum=0
    for i in range(5):
        a=int(input("Enter Marks:"))
        sum=sum+a
        percentage=sum/5
    return sum,percentage
sum,percentage=marks()
print("Sum Is:",sum)
print("Percentage Is:",percentage)
if(percentage>35):
    print("YOU ARE PASS")
else:
    print("YOU ARE FAIL")
