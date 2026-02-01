no=input("Enter Year:")
b=int(no)
if(b%400==0):
    if(b%100==0):
        if(b%4==0):
            print("This Year Is Leap Year")
        else:
            print("This Year Is Not Leap Year")
    else:
        print("This Year Is Leap Year")
else:
    print("This Leap Year Is Not Leap Year")
    
