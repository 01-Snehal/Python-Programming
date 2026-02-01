a=input("Enter Amount:")
b=int(a)
if(b>5000):
    print("5% discount")
    a=b*0.05
    y=b-a
    print("Total Payable Amount",y)
else:
    print("No Discoount")
    
