age=input("Enter Your Age:")
c=int(age)
if(c>=18):
    print("You Are Eligible For Voting!")
    b=input("Do You Have Voter ID?")
    if(b=="yes"):
        print("You Can Vote")
    else:
        print("You Can't Vote")
else:
    print("You Are Not Eligible For Voting!")
print("Thank You!!!")
