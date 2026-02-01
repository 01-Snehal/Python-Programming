marks=[89,65,55,4,28,70]
sum=0
flag=0
for i in marks:
    if(i<35):
        flag=flag+1
    sum=sum+i
print("Addition Is:",sum)
per=sum/5
print("Percentage Is:",per)
if(flag>0 and flag<3):
    print("Passed With ATKT")
elif(flag>2):
    print("Fail")
elif(per>=75 and per<=100):
    print("Congrats!!You Got Distinction!")
elif(per>=50 and  per<=75):
    print("Congrats!!You Got First Class!")
elif(per >=35 and  per<=50):
    print("Congrats!!You Are Pass!")
elif(per>=0 and per<=35):
    print("You Are Fail!")
else:
    print("Invalid Input")
print("Thank You!!")


