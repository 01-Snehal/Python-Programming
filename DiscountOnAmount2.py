a=input("Enter Amount:")
b=int(a)
if(b>10000) and (b<15000):
        print("7% discount")
        a=b*0.07
        x=b-a
        print("Total Payable Amount:",x)
elif (b>15000) and (b<20000):
        print("9% discount")
        a=b*0.09
        x=b-a
        print("Total Payable Amount:",x)
elif(b>20000) and (b<30000):
        print("10% discount")
        a=b*0.10
        x=b-a
        print("Total Payable Amount:",x)
elif(b>30000) and (b<40000):
        print("15% discount")
        a=b*0.15
        x=b-a
        print("Total Payable Amount:",x)
        
