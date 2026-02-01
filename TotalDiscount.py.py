i=0
sum=0
while(i<100):
    a=int(input("Enter Amount:"))
    sum=sum+a
    state=input("Do You Want To Continue?")
    if(state=="No"):
        break
print('Total',sum)
if(sum>1000 and sum<1500):
    tp=sum*0.03
    total=sum-tp
    print("Total Percentage Is:",tp)
    print("Total Payable Amount Is:",total)
if(sum>1500 and sum<2000):
    tp=sum*0.05
    total=sum-tp
    print("Total Percentage Is:",tp)
    print("Total Amount Is:",total)
if(sum>2000 and sum<2500):
    tp=sum*0.09
    total=sum-tp
    print("Total Percentage Is:",tp)
    print("Total Amount Is:",total)
if(sum>2500):
    tp=sum*0.09
    total=sum-tp
    print("Total Percentage Is:",tp)
    print("Total Amount Is:",total)
else:
    print("Thank You!!Visit Again!!")
        
    
    
    
