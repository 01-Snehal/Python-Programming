marks=input("Enter Your Marks:")
a=float(marks)
if(a>=35)and(a<50):
    print("You are Pass Only!")
elif(a>=50)and(a<60):
    print("You Got Second Class!")
elif(a>=60)and(a<75):
    print("You Got First Class!")
elif(a>=75)and(a<100):
    print("You Got Distinction!")
else:
    print("Thank You")
